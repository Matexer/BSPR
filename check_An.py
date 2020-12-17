import matplotlib.pyplot as plt
import math
from app.head.database import Database


f_name1 = "RNDSI-5k"
A1 = 5.452 * 10**(-6), 5.796 * 10**(-6)
n1 = 0.467, 0.466
density1 = 1560

dmins1 = 0.0073, 0.0078, 0.008, 0.0084
times1 = 248, 279, 283, 305

f_name2 = "Bazalt 2a"
A2 = 1.370 * 10**(-5), 1.038 * 10**(-5)
n2 = 0.442, 0.454
density2 = 1620

dmins2 = 0.0098, 0.010
times2 = 96, 98, 103


db = Database()
surveys1 = db.load_surveys(f_name1, "pressthru")
surveys2 = db.load_surveys(f_name2, "pressthru")

def show_plot(dmin, pr_ch, pr_sr, size, p_time, surveys, f_name):
    survey = None
    for s in surveys:
        if round(s.jet_diameter / 1000, 4) == dmin:
            survey = s
    if not survey:
        print("Brak pomiaru")
        return

    press_values = survey.values[0]
    time = tuple((survey.sampling_time * i for i in range(len(press_values))))

    t0 = survey.t0
    tk = survey.tk

    plot = plt.subplot(size)
    plt.plot(time, press_values)
    plt.axhline(pr_ch, color="red")
    plt.axhline(pr_sr, color="black")
    plt.axvline(t0, color="green", linestyle="--")
    plt.axvline(tk, color="pink", linestyle="--")
    plt.axvline(p_time, color="orange", linestyle="--")
    plt.axis(xmin=survey.t0 - 10, ymin=0,
    ymax=max(pr_sr ,pr_ch, max(press_values)) * 1.05, xmax=survey.tk * 1.1)
    plot.set_title(f"{f_name} dla ŚKD = {survey.jet_diameter} mm".replace(".", ","))
    plot.set_xlabel("Czas [ms]")
    plot.set_ylabel("Ciśnienie [MPa]")
    legend = ["ciśnienie", f"ciśnienie robocze\nn. p. ch. w. = {str(round(pr_ch,2)).replace('.', ',')} MPa",
    f"ciśnienie robocze\nn. p. śr. w. = {str(round(pr_sr,2)).replace('.', ',')} MPa",
    f"t0 = {int(round(t0, 0))} ms", f"tk = {int(round(tk, 0))} ms", f"t = {p_time} ms"]
    plot.legend(legend)


def get_pr(dmin, f_name, density, A, n):
    f = db.load_fuel(f_name)
    D = f.outer_diameter / 1000
    d = f.inner_diameter / 1000
    L = f.length / 1000
    fp = f.strength * 1000_000
    k = f.k
    S = (2 * math.pi * (D**2 - d**2) / 4) + (2 * math.pi * L * (D + d) / 2)
    K0 = ((2 / (k + 1))**(1/(k-1))) * math.sqrt((2*k)/(k+1))
    c = K0 / math.sqrt(fp)
    Fm = (math.pi * dmin ** 2) / 4
    p_r = ((density * S * A) / (c * Fm)) ** (1 / (1 - n))
    return p_r

fig = plt.figure(figsize=(9, 27))
sizes = 321, 322, 323, 324, 325, 326

plt.subplots_adjust(left=0.071, bottom=0.048, right=1,
    top=0.971, wspace=0.145, hspace=0.283)

for dmin, size, time in zip(dmins1, sizes[:4], times1):
    pr_ch = get_pr(dmin, f_name1, density1, A1[0], n1[0]) / 1000_000
    pr_sr = get_pr(dmin, f_name1, density1, A1[1], n1[1]) / 1000_000
    show_plot(dmin, pr_ch, pr_sr, size, time, surveys1, f_name1)

for dmin, size, time in zip(dmins2, sizes[4:], times2):
    pr_ch = get_pr(dmin, f_name2, density2, A2[0], n2[0]) / 1000_000
    pr_sr = get_pr(dmin, f_name2, density2, A2[1], n2[1]) / 1000_000
    show_plot(dmin, pr_ch, pr_sr, size, time, surveys2, f_name2)

plt.show()