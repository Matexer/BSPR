from typing import List
from .template import InterfaceTemplate, Data, Config


class EnginePara(InterfaceTemplate):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.details: float

    def K0_k(self):
        ...
    
    def K_k(self):
        ...
    
    def Fw(self):
        ...

    def Xa(self):
        ...

    def fi_2(self):
       ... 
