#Modul Importe
from pathlib import Path
import openpyxl
import pandas as pd

import warnings
import os
import glob

# Get Data from excel File
dataFolder = Path(__file__).resolve().parent.parent.parent # Absoluter Pfad zum Ordner dieser Datei, findet ihn automatisch heraus
import sys; sys.path.append(str(dataFolder.parent)) # Füge Ordner zur Laufzeitumgebung damit die selbst erstellte Module gefunden werden

def getdataZHI18K1P():
    #print(os.listdir(dataFolder))
    ZHI18K1P_raw_csv = dataFolder/ '03_Code' / 'Input_Data' /'Data' / 'ZHI18K1P-TFM_10C_R410A.xlsx'
    rawdata_ZHI18K1P = pd.read_excel(ZHI18K1P_raw_csv)
    return rawdata_ZHI18K1P

def getdata_R410A():
    rawdata_R410A_dic = dataFolder/ '03_Code'/'Input_Data'  / 'Data' / 'R410A_erweitert.csv'
    rawdata_R410A = pd.read_csv(rawdata_R410A_dic)
    #print(rawdata_R410A)

    return rawdata_R410A

def getdata_R32():
    rawdata_R32_dic = dataFolder/ '03_Code'/'Input_Data'  / '03_MeanData' / 'R32_MeanData.csv'
    rawdata_R32 = pd.read_csv(rawdata_R32_dic)

    return rawdata_R32

def getdata_R290():
    rawdata_R290_dic = dataFolder/ '03_Code'/'Input_Data'  / '03_MeanData' / 'R290_MeanData.csv'
    rawdata_R290 = pd.read_csv(rawdata_R290_dic)

    return rawdata_R290

def getdata_R454C():
    rawdata_R454C_dic = dataFolder/ '03_Code'/'Input_Data'  / '03_MeanData' / 'R454C_MeanData.csv'
    rawdata_R454C = pd.read_csv(rawdata_R454C_dic)

    return rawdata_R454C

def getdataZHI18K1P_Temp_old():
    #print(os.listdir(dataFolder))
    ZHI18K1P_raw_csv = dataFolder/ '03_Code' / 'Data' / 'ZHI18K1P-TFM_10C_R410A.xlsx'
    rawdata_ZHI18K1P = pd.read_excel(ZHI18K1P_raw_csv)
    coolcap_Cdata = rawdata_ZHI18K1P.iloc[0]
    power_Cdata= rawdata_ZHI18K1P.iloc[1]
    current_Cdata = rawdata_ZHI18K1P.iloc[2]
    sucmassflow_Cdata = rawdata_ZHI18K1P.iloc[3]

    return rawdata_ZHI18K1P, coolcap_Cdata,power_Cdata,current_Cdata,sucmassflow_Cdata

def getdata_R32_PI25():
    rawdata_R32_PI25_dic = dataFolder/'03_Code'/'Input_Data'/'05_Quasistationär_csv'/'R32' /'R32_pi_25.csv'
    rawdata_R32_PI_25 = pd.read_csv(rawdata_R32_PI25_dic)
    return rawdata_R32_PI_25

def getdata_R32_PI3():
    rawdata_R32_PI3_dic = dataFolder/'03_Code'/'Input_Data'/'05_Quasistationär_csv'/'R32' /'R32_pi_3.csv'
    rawdata_R32_PI_3 = pd.read_csv(rawdata_R32_PI3_dic)
    return rawdata_R32_PI_3

def getdata_R32_PI35():
    rawdata_R32_PI35_dic = dataFolder/'03_Code'/'Input_Data'/'05_Quasistationär_csv'/'R32' /'R32_pi_35.csv'
    rawdata_R32_PI_35 = pd.read_csv(rawdata_R32_PI35_dic)
    return rawdata_R32_PI_35

def getdata_R32_PI4():
    rawdata_R32_PI4_dic = dataFolder/'03_Code'/'Input_Data'/'05_Quasistationär_csv'/'R32' /'R32_pi_4.csv'
    rawdata_R32_PI_4 = pd.read_csv(rawdata_R32_PI4_dic)
    return rawdata_R32_PI_4

def getdata_R32_PI45():
    rawdata_R32_PI45_dic = dataFolder/'03_Code'/'Input_Data'/'05_Quasistationär_csv'/'R32' /'R32_pi_45.csv'
    rawdata_R32_PI_45 = pd.read_csv(rawdata_R32_PI45_dic)
    return rawdata_R32_PI_45

def getdata_R290_PI25():
    rawdata_R290_PI25_dic = dataFolder/'03_Code'/'Input_Data'/'05_Quasistationär_csv'/'R290' /'R290_pi_25.csv'
    rawdata_R290_PI_25 = pd.read_csv(rawdata_R290_PI25_dic)
    return rawdata_R290_PI_25


def getdata_R290_PI3():
    rawdata_R290_PI3_dic = dataFolder/'03_Code'/'Input_Data'/'05_Quasistationär_csv'/'R290' /'R290_pi_3.csv'
    rawdata_R290_PI_3 = pd.read_csv(rawdata_R290_PI3_dic)
    return rawdata_R290_PI_3

def getdata_R290_PI35():
    rawdata_R290_PI35_dic = dataFolder/'03_Code'/'Input_Data'/'05_Quasistationär_csv'/'R290' /'R290_pi_35.csv'
    rawdata_R290_PI_35 = pd.read_csv(rawdata_R290_PI35_dic)
    return rawdata_R290_PI_35

def getdata_R290_PI4():
    rawdata_R290_PI4_dic = dataFolder/'03_Code'/'Input_Data'/'05_Quasistationär_csv'/'R290' /'R290_pi_4.csv'
    rawdata_R290_PI_4 = pd.read_csv(rawdata_R290_PI4_dic)
    return rawdata_R290_PI_4

def getdata_R290_PI45():
    rawdata_R290_PI45_dic = dataFolder/'03_Code'/'Input_Data'/'05_Quasistationär_csv'/'R290' /'R290_pi_45.csv'
    rawdata_R290_PI_45 = pd.read_csv(rawdata_R290_PI45_dic)
    return rawdata_R290_PI_45

def getdata_R290_PI5():
    rawdata_R290_PI5_dic = dataFolder/'03_Code'/'Input_Data'/'05_Quasistationär_csv'/'R290' /'R290_pi_5.csv'
    rawdata_R290_PI_5 = pd.read_csv(rawdata_R290_PI5_dic)
    return rawdata_R290_PI_5

def getdata_R290_PI55():
    rawdata_R290_PI55_dic = dataFolder/'03_Code'/'Input_Data'/'05_Quasistationär_csv'/'R290' /'R290_pi_55.csv'
    rawdata_R290_PI_55 = pd.read_csv(rawdata_R290_PI55_dic)
    return rawdata_R290_PI_55

def getdata_R290_PI6():
    rawdata_R290_PI6_dic = dataFolder/'03_Code'/'Input_Data'/'05_Quasistationär_csv'/'R290' /'R290_pi_6.csv'
    rawdata_R290_PI_6 = pd.read_csv(rawdata_R290_PI6_dic)
    return rawdata_R290_PI_6

def getdata_R290_PI65():
    rawdata_R290_PI65_dic = dataFolder/'03_Code'/'Input_Data'/'05_Quasistationär_csv'/'R290' /'R290_pi_65.csv'
    rawdata_R290_PI_65 = pd.read_csv(rawdata_R290_PI65_dic)
    return rawdata_R290_PI_65
def getdata_R410A_PI3():
    rawdata_R410A_PI3_dic = dataFolder/'03_Code'/'Input_Data'/'05_Quasistationär_csv'/'R410A' /'R410A_pi_3.csv'
    rawdata_R410A_PI_3 = pd.read_csv(rawdata_R410A_PI3_dic)
    return rawdata_R410A_PI_3
def getdata_R410A_PI35():
    rawdata_R410A_PI35_dic = dataFolder/'03_Code'/'Input_Data'/'05_Quasistationär_csv'/'R410A' /'R410A_pi_35.csv'
    rawdata_R410A_PI_35 = pd.read_csv(rawdata_R410A_PI35_dic)
    return rawdata_R410A_PI_35
def getdata_R410A_PI4():
    rawdata_R410A_PI4_dic = dataFolder/'03_Code'/'Input_Data'/'05_Quasistationär_csv'/'R410A' /'R410A_pi_4.csv'
    rawdata_R410A_PI_4 = pd.read_csv(rawdata_R410A_PI4_dic)
    return rawdata_R410A_PI_4
def getdata_R410A_PI45():
    rawdata_R410A_PI45_dic = dataFolder/'03_Code'/'Input_Data'/'05_Quasistationär_csv'/'R410A' /'R410A_pi_45.csv'
    rawdata_R410A_PI_45 = pd.read_csv(rawdata_R410A_PI45_dic)
    return rawdata_R410A_PI_45
def getdata_R410A_PI5():
    rawdata_R410A_PI5_dic = dataFolder/'03_Code'/'Input_Data'/'05_Quasistationär_csv'/'R410A' /'R410A_pi_5.csv'
    rawdata_R410A_PI_5 = pd.read_csv(rawdata_R410A_PI5_dic)
    return rawdata_R410A_PI_5

def getdata_R410A_PI55():
    rawdata_R410A_PI55_dic = dataFolder/'03_Code'/'Input_Data'/'05_Quasistationär_csv'/'R410A' /'R410A_pi_55.csv'
    rawdata_R410A_PI_55 = pd.read_csv(rawdata_R410A_PI55_dic)
    return rawdata_R410A_PI_55
def getdata_R410A_PI6():
    rawdata_R410A_PI6_dic = dataFolder/'03_Code'/'Input_Data'/'05_Quasistationär_csv'/'R410A' /'R410A_pi_6.csv'
    rawdata_R410A_PI_6 = pd.read_csv(rawdata_R410A_PI6_dic)
    return rawdata_R410A_PI_6
def getdata_R410A_PI65():
    rawdata_R410A_PI65_dic = dataFolder/'03_Code'/'Input_Data'/'05_Quasistationär_csv'/'R410A' /'R410A_pi_65.csv'
    rawdata_R410A_PI_65 = pd.read_csv(rawdata_R410A_PI65_dic)
    return rawdata_R410A_PI_65


def getdata_R454C_PI35():
    rawdata_R454C_PI35_dic = dataFolder/'03_Code'/'Input_Data'/'05_Quasistationär_csv'/'R454C' /'R454C_pi_35.csv'
    rawdata_R454C_PI_35 = pd.read_csv(rawdata_R454C_PI35_dic)
    return rawdata_R454C_PI_35


def getdata_R454C_PI45():
    rawdata_R454C_PI45_dic = dataFolder/'03_Code'/'Input_Data'/'05_Quasistationär_csv'/'R454C' /'R454C_pi_45.csv'
    rawdata_R454C_PI_45= pd.read_csv(rawdata_R454C_PI45_dic)
    return rawdata_R454C_PI_45

def getdata_R454C_PI5():
    rawdata_R454C_PI5_dic = dataFolder/'03_Code'/'Input_Data'/'05_Quasistationär_csv'/'R454C' /'R454C_pi_5.csv'
    rawdata_R454C_PI_5 = pd.read_csv(rawdata_R454C_PI5_dic)
    return rawdata_R454C_PI_5

def getdata_R454C_PI55():
    rawdata_R454C_PI55_dic = dataFolder/'03_Code'/'Input_Data'/'05_Quasistationär_csv'/'R454C' /'R454C_pi_55.csv'
    rawdata_R454C_PI_55 = pd.read_csv(rawdata_R454C_PI55_dic)
    return rawdata_R454C_PI_55

def getdata_R454C_PI6():
    rawdata_R454C_PI6_dic = dataFolder/'03_Code'/'Input_Data'/'05_Quasistationär_csv'/'R454C' /'R454C_pi_6.csv'
    rawdata_R454C_PI_6 = pd.read_csv(rawdata_R454C_PI6_dic)
    return rawdata_R454C_PI_6

def getdata_R454C_PI65():
    rawdata_R454C_PI65_dic = dataFolder/'03_Code'/'Input_Data'/'05_Quasistationär_csv'/'R454C' /'R454C_pi_65.csv'
    rawdata_R454C_PI_65 = pd.read_csv(rawdata_R454C_PI65_dic)
    return rawdata_R454C_PI_65

