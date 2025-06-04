# -*- coding: utf-8 -*-
"""
Created on 19.05.2020

@author: Christoph Hoeges

Test self-defined fluids with RefProp
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

    # fluids = ["PROPANE", "ISOBUTAN"]
    # mixture = "|".join([f + ".FLD" for f in fluids])
    mixture = "N2|R1234yf"
    # mixture = "R32.FLD|R125.FLD"
    mol_frac = [0.5, 0.5]

    setup = RP.SETUPdll(len(mol_frac), mixture, 'HMX.BNC', 'DEF')
    setref = RP.SETREFdll('DEF', 1, mol_frac, 0, 0, 0, 0)
    # SETUP Error 117
    print("Setup error: Number:", setup.ierr, "\nMessage:", setup.herr)
    setup = RP.SETUPdll(len(mol_frac), "PROPANE|BUTANE", 'HMX.BNC', 'DEF')
    setref = RP.SETREFdll('DEF', 1, mol_frac, 0, 0, 0, 0)

    # SETUP Error 117
    print("Setup error: Number:", setup.ierr, "\nMessage:", setup.herr)

    setup = RP.SETUPdll(len(mol_frac), mixture, 'HMX.BNC', 'DEF')
    setref = RP.SETREFdll('DEF', 1, mol_frac, 0, 0, 0, 0)

    # SETUP Error 117
    print("Setup error: Number:", setup.ierr, "\nMessage:", setup.herr)


    rpdll = RP.REFPROPdll("", "QT", "M;P", MOLAR_BASE_SI, 0, 0, 1.0, 260.15, mol_frac)
    M = rpdll.Output[0]
    print("Error number:", rpdll.ierr, "\nError code:", rpdll.herr)

    mass_frac = RP.XMASSdll(mol_frac).xkg
    print(mass_frac)

    # Values from GUI (Saturated vapor)
    T = 273.15
    P = 237690
    D = 5.7383
    U = 523910
    H = 565330
    S = 2357.4
    Q = 1.0

    pqflsh = RP.PQFLSHdll(P/1000, Q, mol_frac, 0)
    print("PQFLSH values:")
    print("Error number:", pqflsh.ierr, "\nError code:", pqflsh.herr)
    print("h=", round(pqflsh.h / M))
    print("s=", round(pqflsh.s / M))
