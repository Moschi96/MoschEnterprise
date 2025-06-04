# -*- coding: utf-8 -*-
"""
Created on 22.05.2020

@author: Christoph Hoeges

Testing script for RefProp transport properties


Further notes to general refprop.py script:
-------------------------------------------
- Ian Bell says in several Git-Issues that in REFPROPdll molar_base and i_mass=0 (for molar returns) shall be used I
    might have to adapt the function later on
- Same as above goes for ALLPROPSdll function
"""
# ======================================================================================================================
#                                                     Imports
# ======================================================================================================================
import os
from ctREFPROP.ctREFPROP import REFPROPFunctionLibrary

# ======================================================================================================================
#                                                     Settings
# ======================================================================================================================


# ======================================================================================================================
#                                                       Main
# ======================================================================================================================
if __name__ == "__main__":
    cwd = os.getcwd()
    root = os.environ["RPPREFIX"]
    RP = REFPROPFunctionLibrary(cwd+r"\\REFPRP64.DLL")
    RP.SETPATHdll(root)
    MOLAR_BASE_SI = RP.GETENUMdll(0, "MOLAR BASE SI").iEnum
    print("Version:", RP.RPVersion())
    mix = 'R410A.MIX'
    sm = RP.SETMIXdll(mix, 'HMX.BNC', 'DEF')
    RP.SETREFdll('DEF', 2, sm.z, 0, 0, 0, 0)

    # Get M
    rpdll = RP.REFPROPdll("", "QT", "M", MOLAR_BASE_SI, 0, 0, 1.0, 273.15, sm.z)
    M = rpdll.Output[0]
    # Get transport props
    T = 273.15  # in K
    D = 30.576  # in kg/m^3
    print("-------------- AllPROPSdll --------------")
    res = RP.ALLPROPSdll("PRANDTL;VIS;TCX;TD;KV;P;CV;CP;BETA", MOLAR_BASE_SI, 0, 0, T, D/M, sm.z)
    print("Pr=", res.Output[0])
    print("Vis=", res.Output[1])
    print("Lambda=", res.Output[2])
    print("TD=", res.Output[3])
    print("KV=", res.Output[4])
    print("p=", res.Output[5])
    print("cv=", res.Output[6]/M)
    print("cp=", res.Output[7]/M)
    print("Beta=", res.Output[8])

    print("-------------- REFPROPdll --------------")
    res = RP.REFPROPdll("", "DT", "PRANDTL;VIS;TCX;TD;KV;P;CV;CP;BETA", MOLAR_BASE_SI, 0, 0, D/M, 273.15, sm.z)
    print("Pr=", res.Output[0])
    print("Vis=", res.Output[1])
    print("Lambda=", res.Output[2])
    print("TD=", res.Output[3])
    print("KV=", res.Output[4])
    print("p=", res.Output[5])
    print("cv=", res.Output[6])
    print("cp=", res.Output[7])
    print("Beta=", res.Output[8])
