import matplotlib.pyplot as plt
import math
from app.head.database import Database


f_name = "RNDSI-5k"
TIME = 0
A = 4.862 * 10**(-6)     # [m/s*Pa^n]
n = 0.477                # [-]
density = 1560

dmins = 0.0073, 0.0078, 0.008
times = 241.8, 280.2, 287.3


db = Database()
surveys = db.load_surveys(f_name, "pressthru")

def show_plot(dmin, pr, size, p_time):
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
    plt.axhline(pr, color="red")
    plt.axvline(t0, color="green", linestyle="--")
    plt.axvline(tk, color="pink", linestyle="--")
    if TIME:
        plt.axvline(p_time, color="orange", linestyle="--")
    plt.axis(xmin=0, ymin=0, ymax=max(pr, max(press_values)) * 1.05)
    plot.set_title(f"Dla ŚKD = {survey.jet_diameter} mm".replace(".", ","))
    plot.set_xlabel("Czas [ms]")
    plot.set_ylabel("Ciśnienie [MPa]")
    legend = ["ciśnienie", f"ciśnienie robocze\n{round(pr,2)} MPa".replace(".", ","),
    f"t0 = {int(round(t0, 0))} ms", f"tk = {int(round(tk, 0))} ms"]
    if TIME:
        legend.append(f"t = {p_time} ms")
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


fig = plt.figure(figsize=(9, 9))
sizes = 221, 222, 223
plt.subplots_adjust(left=0.062, bottom=0.057, right=0.983,
    top=0.964, wspace=0.162, hspace=0.25)

for dmin, size, time in zip(dmins, sizes, times):
    pr = get_pr(dmin, f_name, density, A, n) / 1000_000
    show_plot(dmin, pr, size, time)

plt.show()