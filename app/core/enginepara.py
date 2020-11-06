from typing import List, NamedTuple
import math
import scipy.optimize as spo
from .template import DesignationTemplate, Data, Config


class EngineParaOutput(NamedTuple):
    fi1: float  #[-]
    fi2: float  #[-]
    lam: float  #[-]

    K0_k: float  #[-]
    zeta_a: float  #[-]
    Xa: float  #[-]
    Fw: float  #[-]
    K_k: float  #[m^(1/2)/s]
    Fmin: float  #[mm2]
    R: float  #[N*s]
    P: float  #[MPa*s]


class EnginePara(DesignationTemplate):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_results(self):
        fuel = self.data.variables.fuel
        survey = self.data.surveys[0]

        k = fuel.k
        fp = self.MJ_to_J(fuel.strength)
        dmin = self.mm_to_m(survey.jet_diameter)
        mp = self.g_to_kg(survey.fuel_mass)
        tc = self.ms_to_s(survey.tc)

        da = self.mm_to_m(self.data.variables.da)
        pz = self.hPa_to_Pa(self.data.variables.pz)
        I1 = self.kN_to_N(self.data.variables.I1)
        g = self.data.variables.g

        K0_k = self.K0_k(k)
        zeta_a = da / dmin
        Xa = self.Xa(k, K0_k, zeta_a)
        Fw = self.Fw(k, Xa)
        K_k = self.K_k(k, g)
        P = self.P(survey)
        fi2 = self.fi2(K_k, fp, Fw, mp, P)

        Fmin = self.Fmin(dmin)
        R = self.R(survey)
        fi1fi2 = self.fi1fi2(K0_k, Fw, g, Fmin, R, P, tc, Xa, zeta_a)
        print(f"fi1fi2 = {fi1fi2}")
        fi1 = self.fi1(fi1fi2, fi2)

        f0 = self.MJ_to_J(fp / k)
        fi1_lam = self.fi1_lam(
            K0_k, I1, f0, g, Fw, zeta_a, fi1fi2, Xa, pz, tc, P)
        lam = self.lam(fi1, fi1_lam)
        return EngineParaOutput(
            fi1, fi2, lam, K0_k, zeta_a, Xa, Fw, K_k, 
            self.m2_to_mm2(Fmin), R, self.Pa_to_MPa(P))

    @staticmethod
    def K0_k(k):
        return math.sqrt((k-1)/(k+1)) * (2/(k+1))**(1/(k-1))

    @staticmethod
    def Xa(k, K0_k, zeta_a):
        A = K0_k / (zeta_a**2)
        a = 1 / k
        b = (k+1) / k

        def equation(x):
            return math.sqrt(x**a - x**b) - A

        return spo.fsolve(equation, x0=0)[0]

    @staticmethod
    def Fw(k, Xa):
        return math.sqrt((2*k)/(k-1) * (1 - Xa**((k-1)/k)))

    @staticmethod
    def K_k(k, g):
        A = 2 / (k+1)
        B = 1 / (k - 1)
        C = math.sqrt((2*g*k) / (k+1))
        return (A**B)*C

    def P(self, survey):
        smp_time = self.ms_to_s(survey.sampling_time)
        times = (survey.t0, survey.tk, survey.tc)
        press_values = self.cut_values(
            survey.values[0], survey.sampling_time,
            times, 2)
        press_values = self.MPa_to_Pa(press_values)
        return self.integrate(press_values, smp_time)

    @staticmethod
    def fi2(K_k, fp, Fw, mp, P):
        print(f"""fi2:
K_k = {K_k}
fp = {fp} J/kg
Fw = {Fw} 
mp = {mp} kg
P = {P} Pa*s
-------------------""")
        A = (K_k * Fw * P)
        return mp * math.sqrt(fp) / A

    @staticmethod
    def Fmin(dmin):
        return math.pi * (dmin**2) / 4

    def R(self, survey):
        smp_time = self.ms_to_s(survey.sampling_time)
        times = (survey.t0, survey.tk, survey.tc)
        thrust_values = self.cut_values(
            survey.values[1], survey.sampling_time,
            times, 2)
        thrust_values = self.kN_to_N(thrust_values)
        return self.integrate(thrust_values, smp_time)

    @staticmethod
    def fi1fi2(K0_k, Fw, g, Fmin, R, P, tc, Xa, zeta_a):
        print(f"""fi1fi2:
K0_k = {K0_k}
g = {g} m/s2
Fmin = {Fmin} m2
R = {R} N*s
tc = {tc} s
Xa = {Xa}
zeta_a = {zeta_a}
-------------------""")
        A = g / (K0_k * Fw)
        B = R / (Fmin * P)
        C = (zeta_a**2 * Xa * tc) / P
        D = zeta_a**2 * Xa
        return A * (B + C - D)

    @staticmethod
    def fi1(fi1fi2, fi2):
        return fi1fi2 / fi2

    @staticmethod
    def fi1_lam(K0_k, I1, f0, g, Fw, zeta_a, fi1fi2, Xa, pz, tc, P):
        return (K0_k * I1 / math.sqrt(f0)) / ((K0_k * Fw / g) +
         (zeta_a**2 * Xa / fi1fi2) - (zeta_a**2 * pz * tc / (fi1fi2 * P)))

    @staticmethod
    def lam(fi1, f1_lam):
        return (f1_lam / fi1)**2
