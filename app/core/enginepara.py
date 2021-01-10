from typing import List, NamedTuple
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
        return 1

    @staticmethod
    def Xa(k, K0_k, zeta_a):
        return 1

    @staticmethod
    def Fw(k, Xa):
        return 1

    @staticmethod
    def K_k(k, g):
        return 1

    @staticmethod
    def fi2(K_k, fp, Fw, mp, P):
        return 1

    @staticmethod
    def Fmin(dmin):
        return 1

    def R(self, survey):
        return 1

    def P(self, survey):
        return 1

    @staticmethod
    def fi1fi2(K0_k, Fw, g, Fmin, R, P, tc, Xa, zeta_a):
        return 1

    @staticmethod
    def fi1(fi1fi2, fi2):
        return 1

    @staticmethod
    def fi1_lam(K0_k, I1, f0, g, Fw, zeta_a, fi1fi2, Xa, pz, tc, P):
        return 1

    @staticmethod
    def lam(fi1, f1_lam):
        return 1
