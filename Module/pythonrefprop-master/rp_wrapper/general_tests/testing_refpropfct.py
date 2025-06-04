# -*- coding: utf-8 -*-
"""
Created on 29.05.2020

@author: Christoph Hoeges
"""
# ======================================================================================================================
#                                                     Imports
# ======================================================================================================================


# ======================================================================================================================
#                                                     Settings
# ======================================================================================================================


# ======================================================================================================================
#                                                       Main
# ======================================================================================================================
import os
from ctREFPROP.ctREFPROP import REFPROPFunctionLibrary
if __name__ == "__main__":
    cwd = os.getcwd()
    root = os.environ["RPPREFIX"]
    RP = REFPROPFunctionLibrary(cwd+r"\\REFPRP64.DLL")
    RP.SETPATHdll(root)
    MOLAR_BASE_SI = RP.GETENUMdll(0, "MOLAR BASE SI").iEnum
    print("Version:", RP.RPVersion())
    fluid = 'R32'
    sm = RP.SETFLUIDSdll(fluid)
    z = [1]
    rpdll = RP.REFPROPdll("", "TQ", "M;D;H;P", MOLAR_BASE_SI, 0, 0, 273.15, 1.0, z)
    print(rpdll.Output[0:4])
    M = RP.REFPROPdll("", "TQ", "M", MOLAR_BASE_SI, 0, 0, 0, 0, z).Output[0]
    print(M)
    rpdll = RP.REFPROPdll("", "TQ", "P,DLIQ,DVAP,SLIQ,SVAP,HLIQ,HVAP,STN,DPDTSAT,DDDPLIQ,DDDPVAP,DDDTLIQ,DDDTVAP,DHDP_TLIQ,DHDP_TVAP,DHDT_PLIQ,DHDT_PVAP", MOLAR_BASE_SI, 0, 0, 273.15, 0.0, z)
    print(rpdll.Output[0:17])
    print(rpdll.Output[0:18])
