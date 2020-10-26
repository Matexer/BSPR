from typing import List, NamedTuple
import math
import sympy as sp
from .template import InterfaceTemplate, Data, Config


class EngineParaOutput(NamedTuple):
    fi1: float  #[-]
    fi2: float  #[-]
    lam: float  #[-]

    K0_k: float  #[-]
    zeta_a: float  #[-]
    Xa: float  #[-]
    Fw: float  #[-]
    K_k: float  #[-]
    Fmin = float  #[mm2]
    R = float  #[kN*s]
    P = float  #[MPa*s]


class EnginePara(InterfaceTemplate):
    END_TIME_INDEX = 2


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_results(self):
        fuel = self.data.variables.fuel
        survey = self.data.surveys[0]

        k = fuel.k
        fp = self.to_J(fuel.strength)
        dmin = self.to_m(survey.jet_diameter)
        mp = self.to_kg(survey.fuel_mass)
        tc = self.to_s(survey.tc)

        da = self.to_m(self.data.variables.da)
        pz = self.hPa_to_Pa(self.data.variables.pz)
        I1 = self.to_N(self.data.variables.I1)
        f0 = self.to_J(self.data.variables.f0)
        g = self.data.variables.g

        K0_k = self.K0_k(k)
        zeta_a = self.zeta_a(da, dmin)
        Xa = self.Xa(k, K0_k, zeta_a)
        Fw = self.Fw(k, Xa)
        K_k = self.K_k(k)
        P = self.P(survey)
        fi2 = self.fi2(K_k, fp, Fw, mp, P)

        Fmin = self.Fmin(dmin)
        R = self.R(survey)
        fi1fi2 = self.fi1fi2(K0_k, Fw, g, Fmin, R, P, tc, Xa, zeta_a)
        fi1 = self.fi1(fi1fi2, fi2)

        fi1_lam = self.fi1_lam(
            K0_k, I1, f0, g, Fw, zeta_a, fi1fi2, Xa, pz, tc, P)
        lam = self.lam(fi1, fi1_lam)
        return EngineParaOutput(
            fi1, fi2, lam, K0_k, zeta_a, Xa, Fw, K_k, 
            self.to_mm2(Fmin), self.N_to_kN(R), self.to_MPa(P))

    @staticmethod
    def K0_k(k):
        return math.sqrt((k-1)/(k+1)) * (2/(k+1))**(1/(k-1))
    
    @staticmethod
    def zeta_a(da, dmin):
        return da / dmin

    @staticmethod
    def Xa(k, K0_k, zeta_a):
        x = sp.Symbol('x')
        A = K0_k / (zeta_a**2)
        a = 1 / k
        b = (k+1) / k

        equation = sp.Poly((x**a - x**b)**(1/2) - A, x, domain="QQ")
        output = sp.solve(equation)
        return output

    @staticmethod
    def Fw(k, Xa):
        return math.sqrt((2*k)/(k-1) * (1 - Xa**((k-1)/k)))

    @staticmethod
    def K_k(k):
        return (2/(k+1)**(1/(k-1))) * math.sqrt(2*k / (k+1))

    def P(self, survey):
        smp_time = self.to_s(survey.sampling_time)
        times = (survey.t0, survey.tk, survey.tc)
        press_values = self.cut_values(
            survey.values[0], survey.sampling_time, times)
        press_values = self.to_Pa(press_values)
        return self.integrate(press_values, smp_time)

    @staticmethod
    def fi2(K_k, fp, Fw, mp, P):
        return mp / (K_k / math.sqrt(fp) * Fw * P)

    @staticmethod
    def Fmin(dmin):
        return math.pi * (dmin**2) / 4

    def R(self, survey):
        smp_time = self.to_s(survey.sampling_time)
        times = (survey.t0, survey.tk, survey.tc)
        thrust_values = self.cut_values(
            survey.values[1], survey.sampling_time, times)
        thrust_values = self.to_N(thrust_values)
        return self.integrate(thrust_values, smp_time)

    @staticmethod
    def fi1fi2(K0_k, Fw, g, Fmin, R, P, tc, Xa, zeta_a):
        return (g / (K0_k * Fw)) * ((R / (Fmin * P)) +
         ((zeta_a**2 * Xa * tc) / P) - (zeta_a**2 * Xa))

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
