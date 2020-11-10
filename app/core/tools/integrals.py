import numpy as np


class Integrals:
    @staticmethod
    def rect(prep_p_sur, smp_time):
        return sum((v*smp_time for v in prep_p_sur))

    @staticmethod
    def trapeze(prep_p_sur, smp_time):
        val_1 = smp_time * (prep_p_sur[0] + prep_p_sur[-1]) / 2
        val_2 = sum((v * smp_time for v in prep_p_sur[1:-1]))
        return val_1 + val_2

    @staticmethod
    def simpson(prep_p_sur, smp_time):
        h_smp_time = smp_time / 2
        x = [h_smp_time * i for i in range(2 * len(prep_p_sur) - 1)]
        y = [prep_p_sur[0]]
        sum = 0

        for val in prep_p_sur[1:]:
            y.append((val + y[-1]) / 2)
            y.append(val)

        for v in range(len(prep_p_sur) - 1):
            j = 2 * v

            y_1 = y[j]
            y_2 = y[j + 1]
            y_3 = y[j + 2]

            f_1 = [x[j] ** 2, x[j], 1]
            f_2 = [x[j + 1] ** 2, x[j + 1], 1]
            f_3 = [x[j + 2] ** 2, x[j + 2], 1]

            f_m = np.array([f_1, f_2, f_3])
            y_m = np.array([y_1, y_2, y_3])

            f_r = np.linalg.inv(f_m)
            para = f_r @ y_m

            a = para[0]
            b = para[1]
            c = para[2]

            x_p = x[j]
            x_k = x[j + 2]

            P = a * ((x_k ** 3) - (x_p ** 3)) / 3 + b * ((x_k ** 2) - (x_p ** 2)) / 2 + c * (x_k - x_p)
            sum += P
        return sum
