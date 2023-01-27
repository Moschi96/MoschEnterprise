import pandas as pd

from Data_handling.load_data import getdata_R410A
from Data_handling.load_data import getdata_R32
from Data_handling.load_data import getdata_R290
from Data_handling.load_data import getdata_R454C
from Data_handling.load_data import getdataZHI18K1P


from Data_handling.load_data import getdata_R32_PI25
from Data_handling.load_data import getdata_R32_PI3
from Data_handling.load_data import getdata_R32_PI35
from Data_handling.load_data import getdata_R32_PI4
from Data_handling.load_data import getdata_R32_PI45

from Data_handling.load_data import getdata_R290_PI25
from Data_handling.load_data import getdata_R290_PI3
from Data_handling.load_data import getdata_R290_PI35
from Data_handling.load_data import getdata_R290_PI4
from Data_handling.load_data import getdata_R290_PI45
from Data_handling.load_data import getdata_R290_PI5
from Data_handling.load_data import getdata_R290_PI55
from Data_handling.load_data import getdata_R290_PI6
from Data_handling.load_data import getdata_R290_PI65

from Data_handling.load_data import getdata_R410A_PI3
from Data_handling.load_data import getdata_R410A_PI35
from Data_handling.load_data import getdata_R410A_PI4
from Data_handling.load_data import getdata_R410A_PI45
from Data_handling.load_data import getdata_R410A_PI5
from Data_handling.load_data import getdata_R410A_PI55
from Data_handling.load_data import getdata_R410A_PI6
from Data_handling.load_data import getdata_R410A_PI65

from Data_handling.load_data import getdata_R454C_PI35

from Data_handling.load_data import getdata_R454C_PI45
from Data_handling.load_data import getdata_R454C_PI5
from Data_handling.load_data import getdata_R454C_PI55
from Data_handling.load_data import getdata_R454C_PI6
from Data_handling.load_data import getdata_R454C_PI65


R32_PI25_Df_raw = getdata_R32_PI25()
R32_PI3_Df_raw = getdata_R32_PI3()
R32_PI35_Df_raw = getdata_R32_PI35()
R32_PI4_Df_raw = getdata_R32_PI4()
R32_PI45_Df_raw = getdata_R32_PI45()

R290_PI25_Df_raw = getdata_R290_PI25()
R290_PI3_Df_raw = getdata_R290_PI3()
R290_PI35_Df_raw = getdata_R290_PI35()
R290_PI4_Df_raw = getdata_R290_PI4()
R290_PI45_Df_raw = getdata_R290_PI45()
R290_PI5_Df_raw = getdata_R290_PI5()
R290_PI55_Df_raw = getdata_R290_PI55()
R290_PI6_Df_raw = getdata_R290_PI6()
R290_PI65_Df_raw = getdata_R290_PI65()

R410A_PI3_Df_raw = getdata_R410A_PI3()
R410A_PI35_Df_raw = getdata_R410A_PI35()
#
R410A_PI4_Df_raw , R410A_PI42_Df_raw= getdata_R410A_PI4()
R410A_PI45_Df_raw = getdata_R410A_PI45()
R410A_PI5_Df_raw = getdata_R410A_PI5()
R410A_PI55_Df_raw = getdata_R410A_PI55()
R410A_PI6_Df_raw = getdata_R410A_PI6()
R410A_PI65_Df_raw = getdata_R410A_PI65()





R454C_PI35_Df_raw = getdata_R454C_PI35()

R454C_PI45_Df_raw = getdata_R454C_PI45()
R454C_PI5_Df_raw = getdata_R454C_PI5()
R454C_PI55_Df_raw = getdata_R454C_PI55()
R454C_PI6_Df_raw = getdata_R454C_PI6()
R454C_PI65_Df_raw = getdata_R454C_PI65()







#Übergibt die Werte der Funktionen in eine neue Variabel.

R410A_Df_raw = getdata_R410A()
R32_Df_raw = getdata_R32()
R290_Df_raw = getdata_R290()
R454C_Df_raw = getdata_R454C()
ZHI18K1P_raw = getdataZHI18K1P()


def clean_ZHI18K1P():
    ZHI18K1P_Df = pd.DataFrame()
    ZHI18K1P_Df = ZHI18K1P_raw.transpose()
    #ZHI18K1P_Df = ZHI18K1P_Df
    #print(ZHI18K1P_Df)
    ZHI18K1P_Df.drop([ 'Einheiten', 'Übersicht'] , axis=0 , inplace= True)
    return ZHI18K1P_Df



def clean_R410A_DF():
    'Choose the rows for the data of Interest. I need: P1_Process, P2_Process, T1_Process, T2_Process, T_Amb_Process, Power, MF_Suc, Dens_Suc , h1 , s1, v1,cp1, h2, s2, v2, cp2, tc, PI_Set, T_Evaps, T_Conds '
    R410A_Df= pd.DataFrame()
    R410A_Df['P1_Process'] = R410A_Df_raw['P1_Process']
    R410A_Df['P1_Set'] = R410A_Df_raw['P1_Set']
    R410A_Df['P2_Set'] = R410A_Df_raw['P2_Set']
    R410A_Df['P2_Process'] = R410A_Df_raw['P2_Process']
    R410A_Df['T1_Process'] = R410A_Df_raw['T1_Process']
    R410A_Df['T2_Process'] = R410A_Df_raw['T2_Process']
    R410A_Df['T_Amb_Process'] = R410A_Df_raw['T_Amb_Process']
    R410A_Df['Power'] = R410A_Df_raw['Power']
    R410A_Df['MF_Suc'] = R410A_Df_raw['MF_Suc']
    R410A_Df['Dens_Suc'] = R410A_Df_raw['Dens_Suc']
    R410A_Df['h1'] = R410A_Df_raw['h1']
    R410A_Df['s1'] = R410A_Df_raw['s1']
    R410A_Df['v1'] = R410A_Df_raw['v1']
    R410A_Df['cp1'] = R410A_Df_raw['cp1']
    R410A_Df['h2'] = R410A_Df_raw['h2']
    R410A_Df['h2is'] = R410A_Df_raw['h2is']
    R410A_Df['s2'] = R410A_Df_raw['s2']
    R410A_Df['cp2'] = R410A_Df_raw['cp2']
    R410A_Df['tc'] = R410A_Df_raw['tc']
    R410A_Df['PI_Set'] = R410A_Df_raw['PI_Set']
    R410A_Df['T_Evaps'] = R410A_Df_raw['T_Evaps']
    R410A_Df['T_Conds'] = R410A_Df_raw['T_Conds']
    R410A_Df['eta_is'] = R410A_Df_raw['eta_is']

    return R410A_Df

def clean_R32_DF():
    'Choose the rows for the data of Interest. I need: P1_Process, P2_Process, T1_Process, T2_Process, T_Amb_Process, Power, MF_Suc, Dens_Suc , h1 , s1, v1,cp1, h2, s2, v2, cp2, tc, PI_Set, T_Evaps, T_Conds '
    R32_Df= pd.DataFrame()
    R32_Df['P1_Process'] = R32_Df_raw['P1_Process']
    R32_Df['P1_Set'] = R32_Df_raw['P1_Set']
    R32_Df['P2_Set'] = R32_Df_raw['P2_Set']
    R32_Df['P2_Process'] = R32_Df_raw['P2_Process']
    R32_Df['T1_Process'] = R32_Df_raw['T1_Process']
    R32_Df['T2_Process'] = R32_Df_raw['T2_Process']
    R32_Df['T_Amb_Process'] = R32_Df_raw['T_Amb_Process']
    R32_Df['Power'] = R32_Df_raw['Power']
    R32_Df['MF_Suc'] = R32_Df_raw['MF_Suc']
    R32_Df['Dens_Suc'] = R32_Df_raw['Dens_Suc']
    R32_Df['h1'] = R32_Df_raw['h1']
    R32_Df['s1'] = R32_Df_raw['s1']
    R32_Df['v1'] = R32_Df_raw['v1']
    R32_Df['cp1'] = R32_Df_raw['cp1']
    R32_Df['h2'] = R32_Df_raw['h2']
    R32_Df['h2is'] = R32_Df_raw['h2is']
    R32_Df['s2'] = R32_Df_raw['s2']
    R32_Df['cp2'] = R32_Df_raw['cp2']
    R32_Df['tc'] = R32_Df_raw['tc']
    R32_Df['PI_Set'] = R32_Df_raw['PI_Set']
    #R32_Df['T_Evaps'] = R32_Df_raw['T_Evaps']
    #R32_Df['T_Conds'] = R32_Df_raw['T_Conds']
    R32_Df['eta_is'] = R32_Df_raw['eta_is']

    return R32_Df

def clean_R290_DF():
    'Choose the rows for the data of Interest. I need: P1_Process, P2_Process, T1_Process, T2_Process, T_Amb_Process, Power, MF_Suc, Dens_Suc , h1 , s1, v1,cp1, h2, s2, v2, cp2, tc, PI_Set, T_Evaps, T_Conds '
    R290_Df= pd.DataFrame()
    R290_Df['P1_Process'] = R290_Df_raw['P1_Process']
    R290_Df['P1_Set'] = R290_Df_raw['P1_Set']
    R290_Df['P2_Set'] = R290_Df_raw['P2_Set']
    R290_Df['P2_Process'] = R290_Df_raw['P2_Process']
    R290_Df['T1_Process'] = R290_Df_raw['T1_Process']
    R290_Df['T2_Process'] = R290_Df_raw['T2_Process']
    R290_Df['T_Amb_Process'] = R290_Df_raw['T_Amb_Process']
    R290_Df['Power'] = R290_Df_raw['Power']
    R290_Df['MF_Suc'] = R290_Df_raw['MF_Suc']
    R290_Df['Dens_Suc'] = R290_Df_raw['Dens_Suc']
    R290_Df['h1'] = R290_Df_raw['h1']
    R290_Df['s1'] = R290_Df_raw['s1']
    R290_Df['v1'] = R290_Df_raw['v1']
    R290_Df['cp1'] = R290_Df_raw['cp1']
    R290_Df['h2'] = R290_Df_raw['h2']
    R290_Df['h2is'] = R290_Df_raw['h2is']
    R290_Df['s2'] = R290_Df_raw['s2']
    R290_Df['cp2'] = R290_Df_raw['cp2']
    R290_Df['tc'] = R290_Df_raw['tc']
    R290_Df['PI_Set'] = R290_Df_raw['PI_Set']
    #R290_Df['T_Evaps'] = R290_Df_raw['T_Evaps']
    #R290_Df['T_Conds'] = R290_Df_raw['T_Conds']
    R290_Df['eta_is'] = R290_Df_raw['eta_is']

    return R290_Df

def clean_R454C_DF():
    'Choose the rows for the data of Interest. I need: P1_Process, P2_Process, T1_Process, T2_Process, T_Amb_Process, Power, MF_Suc, Dens_Suc , h1 , s1, v1,cp1, h2, s2, v2, cp2, tc, PI_Set, T_Evaps, T_Conds '
    R454C_Df= pd.DataFrame()
    R454C_Df['P1_Process'] = R454C_Df_raw['P1_Process']
    R454C_Df['P1_Set'] = R454C_Df_raw['P1_Set']
    R454C_Df['P2_Set'] = R454C_Df_raw['P2_Set']
    R454C_Df['P2_Process'] = R454C_Df_raw['P2_Process']
    R454C_Df['T1_Process'] = R454C_Df_raw['T1_Process']
    R454C_Df['T2_Process'] = R454C_Df_raw['T2_Process']
    R454C_Df['T_Amb_Process'] = R454C_Df_raw['T_Amb_Process']
    R454C_Df['Power'] = R454C_Df_raw['Power']
    R454C_Df['MF_Suc'] = R454C_Df_raw['MF_Suc']
    R454C_Df['Dens_Suc'] = R454C_Df_raw['Dens_Suc']
    R454C_Df['h1'] = R454C_Df_raw['h1']
    R454C_Df['s1'] = R454C_Df_raw['s1']
    R454C_Df['v1'] = R454C_Df_raw['v1']
    R454C_Df['cp1'] = R454C_Df_raw['cp1']
    R454C_Df['h2'] = R454C_Df_raw['h2']
    R454C_Df['h2is'] = R454C_Df_raw['h2is']
    R454C_Df['s2'] = R454C_Df_raw['s2']
    R454C_Df['cp2'] = R454C_Df_raw['cp2']
    R454C_Df['tc'] = R454C_Df_raw['tc']
    R454C_Df['PI_Set'] = R454C_Df_raw['PI_Set']
    #R32_Df['T_Evaps'] = R32_Df_raw['T_Evaps']
    #R32_Df['T_Conds'] = R32_Df_raw['T_Conds']
    R454C_Df['eta_is'] = R454C_Df_raw['eta_is']

    return R454C_Df


def clean_R32_PI25_DF():
    R32_PI25_Df = pd.DataFrame()
    R32_PI25_Df['P1_Process'] =R32_PI25_Df_raw['P1_Process']
    R32_PI25_Df['P1_Process'] = R32_PI25_Df_raw['P1_Process']
    R32_PI25_Df['P1_Set'] = R32_PI25_Df_raw['P1_Set']
    R32_PI25_Df['P2_Set'] = R32_PI25_Df_raw['P2_Set']
    R32_PI25_Df['P2_Process'] = R32_PI25_Df_raw['P2_Process']
    R32_PI25_Df['T1_Process'] = R32_PI25_Df_raw['T1_Process']
    R32_PI25_Df['T2_Process'] = R32_PI25_Df_raw['T2_Process']
    R32_PI25_Df['T_Amb_Process'] = R32_PI25_Df_raw['T_Amb_Process']
    R32_PI25_Df['Power'] = R32_PI25_Df_raw['Power']
    R32_PI25_Df['MF_Suc'] = R32_PI25_Df_raw['MF_Suc']
    R32_PI25_Df['Dens_Suc'] = R32_PI25_Df_raw['Dens_Suc']
    R32_PI25_Df['h1'] = R32_PI25_Df_raw['h1']
    R32_PI25_Df['s1'] = R32_PI25_Df_raw['s1']
    R32_PI25_Df['v1'] = R32_PI25_Df_raw['v1']
    R32_PI25_Df['cp1'] = R32_PI25_Df_raw['cp1']
    R32_PI25_Df['h2'] = R32_PI25_Df_raw['h2']
    R32_PI25_Df['h2is'] = R32_PI25_Df_raw['h2is']
    R32_PI25_Df['s2'] = R32_PI25_Df_raw['s2']
    R32_PI25_Df['cp2'] = R32_PI25_Df_raw['cp2']
    R32_PI25_Df['tc'] = R32_PI25_Df_raw['tc']

    # R32_Df['T_Evaps'] = R32_Df_raw['T_Evaps']
    # R32_Df['T_Conds'] = R32_Df_raw['T_Conds']


    return R32_PI25_Df

def clean_R32_PI3_DF():
    R32_PI25_Df = pd.DataFrame()
    R32_PI25_Df['P1_Process'] =R32_PI25_Df_raw['P1_Process']
    R32_PI25_Df['P1_Process'] = R32_PI25_Df_raw['P1_Process']
    R32_PI25_Df['P1_Set'] = R32_PI25_Df_raw['P1_Set']
    R32_PI25_Df['P2_Set'] = R32_PI25_Df_raw['P2_Set']
    R32_PI25_Df['P2_Process'] = R32_PI25_Df_raw['P2_Process']
    R32_PI25_Df['T1_Process'] = R32_PI25_Df_raw['T1_Process']
    R32_PI25_Df['T2_Process'] = R32_PI25_Df_raw['T2_Process']
    R32_PI25_Df['T_Amb_Process'] = R32_PI25_Df_raw['T_Amb_Process']
    R32_PI25_Df['Power'] = R32_PI25_Df_raw['Power']
    R32_PI25_Df['MF_Suc'] = R32_PI25_Df_raw['MF_Suc']
    R32_PI25_Df['Dens_Suc'] = R32_PI25_Df_raw['Dens_Suc']
    R32_PI25_Df['h1'] = R32_PI25_Df_raw['h1']
    R32_PI25_Df['s1'] = R32_PI25_Df_raw['s1']
    R32_PI25_Df['v1'] = R32_PI25_Df_raw['v1']
    R32_PI25_Df['cp1'] = R32_PI25_Df_raw['cp1']
    R32_PI25_Df['h2'] = R32_PI25_Df_raw['h2']
    R32_PI25_Df['h2is'] = R32_PI25_Df_raw['h2is']
    R32_PI25_Df['s2'] = R32_PI25_Df_raw['s2']
    R32_PI25_Df['cp2'] = R32_PI25_Df_raw['cp2']
    R32_PI25_Df['tc'] = R32_PI25_Df_raw['tc']

    # R32_Df['T_Evaps'] = R32_Df_raw['T_Evaps']
    # R32_Df['T_Conds'] = R32_Df_raw['T_Conds']


    return R32_PI25_Df


def clean_R32_PI3_DF():
    R32_PI3_Df = pd.DataFrame()
    R32_PI3_Df['P1_Process'] =R32_PI3_Df_raw['P1_Process']
    R32_PI3_Df['P1_Process'] = R32_PI3_Df_raw['P1_Process']
    R32_PI3_Df['P1_Set'] = R32_PI3_Df_raw['P1_Set']
    R32_PI3_Df['P2_Set'] = R32_PI3_Df_raw['P2_Set']
    R32_PI3_Df['P2_Process'] = R32_PI3_Df_raw['P2_Process']
    R32_PI3_Df['T1_Process'] = R32_PI3_Df_raw['T1_Process']
    R32_PI3_Df['T2_Process'] = R32_PI3_Df_raw['T2_Process']
    R32_PI3_Df['T_Amb_Process'] = R32_PI3_Df_raw['T_Amb_Process']
    R32_PI3_Df['Power'] = R32_PI3_Df_raw['Power']
    R32_PI3_Df['MF_Suc'] = R32_PI3_Df_raw['MF_Suc']
    R32_PI3_Df['Dens_Suc'] = R32_PI3_Df_raw['Dens_Suc']
    R32_PI3_Df['h1'] = R32_PI3_Df_raw['h1']
    R32_PI3_Df['s1'] = R32_PI3_Df_raw['s1']
    R32_PI3_Df['v1'] = R32_PI3_Df_raw['v1']
    R32_PI3_Df['cp1'] = R32_PI3_Df_raw['cp1']
    R32_PI3_Df['h2'] = R32_PI3_Df_raw['h2']
    R32_PI3_Df['h2is'] = R32_PI3_Df_raw['h2is']
    R32_PI3_Df['s2'] = R32_PI3_Df_raw['s2']
    R32_PI3_Df['cp2'] = R32_PI3_Df_raw['cp2']
    R32_PI3_Df['tc'] = R32_PI3_Df_raw['tc']

    # R32_Df['T_Evaps'] = R32_Df_raw['T_Evaps']
    # R32_Df['T_Conds'] = R32_Df_raw['T_Conds']


    return R32_PI3_Df

def clean_R32_PI35_DF():
    R32_PI35_Df = pd.DataFrame()
    R32_PI35_Df['P1_Process'] =R32_PI35_Df_raw['P1_Process']
    R32_PI35_Df['P1_Process'] = R32_PI35_Df_raw['P1_Process']
    R32_PI35_Df['P1_Set'] = R32_PI35_Df_raw['P1_Set']
    R32_PI35_Df['P2_Set'] = R32_PI35_Df_raw['P2_Set']
    R32_PI35_Df['P2_Process'] = R32_PI35_Df_raw['P2_Process']
    R32_PI35_Df['T1_Process'] = R32_PI35_Df_raw['T1_Process']
    R32_PI35_Df['T2_Process'] = R32_PI35_Df_raw['T2_Process']
    R32_PI35_Df['T_Amb_Process'] = R32_PI35_Df_raw['T_Amb_Process']
    R32_PI35_Df['Power'] = R32_PI35_Df_raw['Power']
    R32_PI35_Df['MF_Suc'] = R32_PI35_Df_raw['MF_Suc']
    R32_PI35_Df['Dens_Suc'] = R32_PI35_Df_raw['Dens_Suc']
    R32_PI35_Df['h1'] = R32_PI35_Df_raw['h1']
    R32_PI35_Df['s1'] = R32_PI35_Df_raw['s1']
    R32_PI35_Df['v1'] = R32_PI35_Df_raw['v1']
    R32_PI35_Df['cp1'] = R32_PI35_Df_raw['cp1']
    R32_PI35_Df['h2'] = R32_PI35_Df_raw['h2']
    R32_PI35_Df['h2is'] = R32_PI35_Df_raw['h2is']
    R32_PI35_Df['s2'] = R32_PI35_Df_raw['s2']
    R32_PI35_Df['cp2'] = R32_PI35_Df_raw['cp2']
    R32_PI35_Df['tc'] = R32_PI35_Df_raw['tc']

    # R32_Df['T_Evaps'] = R32_Df_raw['T_Evaps']
    # R32_Df['T_Conds'] = R32_Df_raw['T_Conds']


    return R32_PI35_Df


def clean_R32_PI4_DF():
    R32_PI4_Df = pd.DataFrame()
    R32_PI4_Df['P1_Process'] =R32_PI4_Df_raw['P1_Process']
    R32_PI4_Df['P1_Process'] = R32_PI4_Df_raw['P1_Process']
    R32_PI4_Df['P1_Set'] = R32_PI4_Df_raw['P1_Set']
    R32_PI4_Df['P2_Set'] = R32_PI4_Df_raw['P2_Set']
    R32_PI4_Df['P2_Process'] = R32_PI4_Df_raw['P2_Process']
    R32_PI4_Df['T1_Process'] = R32_PI4_Df_raw['T1_Process']
    R32_PI4_Df['T2_Process'] = R32_PI4_Df_raw['T2_Process']
    R32_PI4_Df['T_Amb_Process'] = R32_PI4_Df_raw['T_Amb_Process']
    R32_PI4_Df['Power'] = R32_PI4_Df_raw['Power']
    R32_PI4_Df['MF_Suc'] = R32_PI4_Df_raw['MF_Suc']
    R32_PI4_Df['Dens_Suc'] = R32_PI4_Df_raw['Dens_Suc']
    R32_PI4_Df['h1'] = R32_PI4_Df_raw['h1']
    R32_PI4_Df['s1'] = R32_PI4_Df_raw['s1']
    R32_PI4_Df['v1'] = R32_PI4_Df_raw['v1']
    R32_PI4_Df['cp1'] = R32_PI4_Df_raw['cp1']
    R32_PI4_Df['h2'] = R32_PI4_Df_raw['h2']
    R32_PI4_Df['h2is'] = R32_PI4_Df_raw['h2is']
    R32_PI4_Df['s2'] = R32_PI4_Df_raw['s2']
    R32_PI4_Df['cp2'] = R32_PI4_Df_raw['cp2']
    R32_PI4_Df['tc'] = R32_PI4_Df_raw['tc']

    # R32_Df['T_Evaps'] = R32_Df_raw['T_Evaps']
    # R32_Df['T_Conds'] = R32_Df_raw['T_Conds']


    return R32_PI4_Df


def clean_R32_PI45_DF():
    R32_PI45_Df = pd.DataFrame()
    R32_PI45_Df['P1_Process'] =R32_PI45_Df_raw['P1_Process']
    R32_PI45_Df['P1_Process'] = R32_PI45_Df_raw['P1_Process']
    R32_PI45_Df['P1_Set'] = R32_PI45_Df_raw['P1_Set']
    R32_PI45_Df['P2_Set'] = R32_PI45_Df_raw['P2_Set']
    R32_PI45_Df['P2_Process'] = R32_PI45_Df_raw['P2_Process']
    R32_PI45_Df['T1_Process'] = R32_PI45_Df_raw['T1_Process']
    R32_PI45_Df['T2_Process'] = R32_PI45_Df_raw['T2_Process']
    R32_PI45_Df['T_Amb_Process'] = R32_PI45_Df_raw['T_Amb_Process']
    R32_PI45_Df['Power'] = R32_PI45_Df_raw['Power']
    R32_PI45_Df['MF_Suc'] = R32_PI45_Df_raw['MF_Suc']
    R32_PI45_Df['Dens_Suc'] = R32_PI45_Df_raw['Dens_Suc']
    R32_PI45_Df['h1'] = R32_PI45_Df_raw['h1']
    R32_PI45_Df['s1'] = R32_PI45_Df_raw['s1']
    R32_PI45_Df['v1'] = R32_PI45_Df_raw['v1']
    R32_PI45_Df['cp1'] = R32_PI45_Df_raw['cp1']
    R32_PI45_Df['h2'] = R32_PI45_Df_raw['h2']
    R32_PI45_Df['h2is'] = R32_PI45_Df_raw['h2is']
    R32_PI45_Df['s2'] = R32_PI45_Df_raw['s2']
    R32_PI45_Df['cp2'] = R32_PI45_Df_raw['cp2']
    R32_PI45_Df['tc'] = R32_PI45_Df_raw['tc']

    # R32_Df['T_Evaps'] = R32_Df_raw['T_Evaps']
    # R32_Df['T_Conds'] = R32_Df_raw['T_Conds']


    return R32_PI45_Df

def clean_R290_PI25_DF():
    R290_PI25_Df = pd.DataFrame()
    R290_PI25_Df['P1_Process'] =R290_PI25_Df_raw['P1_Process']
    R290_PI25_Df['P1_Process'] = R290_PI25_Df_raw['P1_Process']
    R290_PI25_Df['P1_Set'] = R290_PI25_Df_raw['P1_Set']
    R290_PI25_Df['P2_Set'] = R290_PI25_Df_raw['P2_Set']
    R290_PI25_Df['P2_Process'] = R290_PI25_Df_raw['P2_Process']
    R290_PI25_Df['T1_Process'] = R290_PI25_Df_raw['T1_Process']
    R290_PI25_Df['T2_Process'] = R290_PI25_Df_raw['T2_Process']
    R290_PI25_Df['T_Amb_Process'] = R290_PI25_Df_raw['T_Amb_Process']
    R290_PI25_Df['Power'] = R290_PI25_Df_raw['Power']
    R290_PI25_Df['MF_Suc'] = R290_PI25_Df_raw['MF_Suc']
    R290_PI25_Df['Dens_Suc'] = R290_PI25_Df_raw['Dens_Suc']
    R290_PI25_Df['h1'] = R290_PI25_Df_raw['h1']
    R290_PI25_Df['s1'] = R290_PI25_Df_raw['s1']
    R290_PI25_Df['v1'] = R290_PI25_Df_raw['v1']
    R290_PI25_Df['cp1'] = R290_PI25_Df_raw['cp1']
    R290_PI25_Df['h2'] = R290_PI25_Df_raw['h2']
    R290_PI25_Df['h2is'] = R290_PI25_Df_raw['h2is']
    R290_PI25_Df['s2'] = R290_PI25_Df_raw['s2']
    R290_PI25_Df['cp2'] = R290_PI25_Df_raw['cp2']
    R290_PI25_Df['tc'] = R290_PI25_Df_raw['tc']

    # R32_Df['T_Evaps'] = R32_Df_raw['T_Evaps']
    # R32_Df['T_Conds'] = R32_Df_raw['T_Conds']


    return R290_PI25_Df

def clean_R290_PI3_DF():
    R290_PI3_Df = pd.DataFrame()
    R290_PI3_Df['P1_Process'] =R290_PI3_Df_raw['P1_Process']
    R290_PI3_Df['P1_Process'] = R290_PI3_Df_raw['P1_Process']
    R290_PI3_Df['P1_Set'] = R290_PI3_Df_raw['P1_Set']
    R290_PI3_Df['P2_Set'] = R290_PI3_Df_raw['P2_Set']
    R290_PI3_Df['P2_Process'] = R290_PI3_Df_raw['P2_Process']
    R290_PI3_Df['T1_Process'] = R290_PI3_Df_raw['T1_Process']
    R290_PI3_Df['T2_Process'] = R290_PI3_Df_raw['T2_Process']
    R290_PI3_Df['T_Amb_Process'] = R290_PI3_Df_raw['T_Amb_Process']
    R290_PI3_Df['Power'] = R290_PI3_Df_raw['Power']
    R290_PI3_Df['MF_Suc'] = R290_PI3_Df_raw['MF_Suc']
    R290_PI3_Df['Dens_Suc'] = R290_PI3_Df_raw['Dens_Suc']
    R290_PI3_Df['h1'] = R290_PI3_Df_raw['h1']
    R290_PI3_Df['s1'] = R290_PI3_Df_raw['s1']
    R290_PI3_Df['v1'] = R290_PI3_Df_raw['v1']
    R290_PI3_Df['cp1'] = R290_PI3_Df_raw['cp1']
    R290_PI3_Df['h2'] = R290_PI3_Df_raw['h2']
    R290_PI3_Df['h2is'] = R290_PI3_Df_raw['h2is']
    R290_PI3_Df['s2'] = R290_PI3_Df_raw['s2']
    R290_PI3_Df['cp2'] = R290_PI3_Df_raw['cp2']
    R290_PI3_Df['tc'] = R290_PI3_Df_raw['tc']

    # R32_Df['T_Evaps'] = R32_Df_raw['T_Evaps']
    # R32_Df['T_Conds'] = R32_Df_raw['T_Conds']


    return R290_PI3_Df

def clean_R290_PI35_DF():
    R290_PI35_Df = pd.DataFrame()
    R290_PI35_Df['P1_Process'] =R290_PI35_Df_raw['P1_Process']
    R290_PI35_Df['P1_Process'] = R290_PI35_Df_raw['P1_Process']
    R290_PI35_Df['P1_Set'] = R290_PI35_Df_raw['P1_Set']
    R290_PI35_Df['P2_Set'] = R290_PI35_Df_raw['P2_Set']
    R290_PI35_Df['P2_Process'] = R290_PI35_Df_raw['P2_Process']
    R290_PI35_Df['T1_Process'] = R290_PI35_Df_raw['T1_Process']
    R290_PI35_Df['T2_Process'] = R290_PI35_Df_raw['T2_Process']
    R290_PI35_Df['T_Amb_Process'] = R290_PI35_Df_raw['T_Amb_Process']
    R290_PI35_Df['Power'] = R290_PI35_Df_raw['Power']
    R290_PI35_Df['MF_Suc'] = R290_PI35_Df_raw['MF_Suc']
    R290_PI35_Df['Dens_Suc'] = R290_PI35_Df_raw['Dens_Suc']
    R290_PI35_Df['h1'] = R290_PI35_Df_raw['h1']
    R290_PI35_Df['s1'] = R290_PI35_Df_raw['s1']
    R290_PI35_Df['v1'] = R290_PI35_Df_raw['v1']
    R290_PI35_Df['cp1'] = R290_PI35_Df_raw['cp1']
    R290_PI35_Df['h2'] = R290_PI35_Df_raw['h2']
    R290_PI35_Df['h2is'] = R290_PI35_Df_raw['h2is']
    R290_PI35_Df['s2'] = R290_PI35_Df_raw['s2']
    R290_PI35_Df['cp2'] = R290_PI35_Df_raw['cp2']
    R290_PI35_Df['tc'] = R290_PI35_Df_raw['tc']

    # R32_Df['T_Evaps'] = R32_Df_raw['T_Evaps']
    # R32_Df['T_Conds'] = R32_Df_raw['T_Conds']


    return R290_PI35_Df

def clean_R290_PI4_DF():
    R290_PI4_Df = pd.DataFrame()
    R290_PI4_Df['P1_Process'] =R290_PI4_Df_raw['P1_Process']
    R290_PI4_Df['P1_Process'] = R290_PI4_Df_raw['P1_Process']
    R290_PI4_Df['P1_Set'] = R290_PI4_Df_raw['P1_Set']
    R290_PI4_Df['P2_Set'] = R290_PI4_Df_raw['P2_Set']
    R290_PI4_Df['P2_Process'] = R290_PI4_Df_raw['P2_Process']
    R290_PI4_Df['T1_Process'] = R290_PI4_Df_raw['T1_Process']
    R290_PI4_Df['T2_Process'] = R290_PI4_Df_raw['T2_Process']
    R290_PI4_Df['T_Amb_Process'] = R290_PI4_Df_raw['T_Amb_Process']
    R290_PI4_Df['Power'] = R290_PI4_Df_raw['Power']
    R290_PI4_Df['MF_Suc'] = R290_PI4_Df_raw['MF_Suc']
    R290_PI4_Df['Dens_Suc'] = R290_PI4_Df_raw['Dens_Suc']
    R290_PI4_Df['h1'] = R290_PI4_Df_raw['h1']
    R290_PI4_Df['s1'] = R290_PI4_Df_raw['s1']
    R290_PI4_Df['v1'] = R290_PI4_Df_raw['v1']
    R290_PI4_Df['cp1'] = R290_PI4_Df_raw['cp1']
    R290_PI4_Df['h2'] = R290_PI4_Df_raw['h2']
    R290_PI4_Df['h2is'] = R290_PI4_Df_raw['h2is']
    R290_PI4_Df['s2'] = R290_PI4_Df_raw['s2']
    R290_PI4_Df['cp2'] = R290_PI4_Df_raw['cp2']
    R290_PI4_Df['tc'] = R290_PI4_Df_raw['tc']

    # R32_Df['T_Evaps'] = R32_Df_raw['T_Evaps']
    # R32_Df['T_Conds'] = R32_Df_raw['T_Conds']


    return R290_PI4_Df

def clean_R290_PI45_DF():
    R290_PI45_Df = pd.DataFrame()
    R290_PI45_Df['P1_Process'] =R290_PI45_Df_raw['P1_Process']
    R290_PI45_Df['P1_Process'] = R290_PI45_Df_raw['P1_Process']
    R290_PI45_Df['P1_Set'] = R290_PI45_Df_raw['P1_Set']
    R290_PI45_Df['P2_Set'] = R290_PI45_Df_raw['P2_Set']
    R290_PI45_Df['P2_Process'] = R290_PI45_Df_raw['P2_Process']
    R290_PI45_Df['T1_Process'] = R290_PI45_Df_raw['T1_Process']
    R290_PI45_Df['T2_Process'] = R290_PI45_Df_raw['T2_Process']
    R290_PI45_Df['T_Amb_Process'] = R290_PI45_Df_raw['T_Amb_Process']
    R290_PI45_Df['Power'] = R290_PI45_Df_raw['Power']
    R290_PI45_Df['MF_Suc'] = R290_PI45_Df_raw['MF_Suc']
    R290_PI45_Df['Dens_Suc'] = R290_PI45_Df_raw['Dens_Suc']
    R290_PI45_Df['h1'] = R290_PI45_Df_raw['h1']
    R290_PI45_Df['s1'] = R290_PI45_Df_raw['s1']
    R290_PI45_Df['v1'] = R290_PI45_Df_raw['v1']
    R290_PI45_Df['cp1'] = R290_PI45_Df_raw['cp1']
    R290_PI45_Df['h2'] = R290_PI45_Df_raw['h2']
    R290_PI45_Df['h2is'] = R290_PI45_Df_raw['h2is']
    R290_PI45_Df['s2'] = R290_PI45_Df_raw['s2']
    R290_PI45_Df['cp2'] = R290_PI45_Df_raw['cp2']
    R290_PI45_Df['tc'] = R290_PI45_Df_raw['tc']

    # R32_Df['T_Evaps'] = R32_Df_raw['T_Evaps']
    # R32_Df['T_Conds'] = R32_Df_raw['T_Conds']


    return R290_PI45_Df

def clean_R290_PI5_DF():
    R290_PI5_Df = pd.DataFrame()
    R290_PI5_Df['P1_Process'] =R290_PI5_Df_raw['P1_Process']
    R290_PI5_Df['P1_Process'] = R290_PI5_Df_raw['P1_Process']
    R290_PI5_Df['P1_Set'] = R290_PI5_Df_raw['P1_Set']
    R290_PI5_Df['P2_Set'] = R290_PI5_Df_raw['P2_Set']
    R290_PI5_Df['P2_Process'] = R290_PI5_Df_raw['P2_Process']
    R290_PI5_Df['T1_Process'] = R290_PI5_Df_raw['T1_Process']
    R290_PI5_Df['T2_Process'] = R290_PI5_Df_raw['T2_Process']
    R290_PI5_Df['T_Amb_Process'] = R290_PI5_Df_raw['T_Amb_Process']
    R290_PI5_Df['Power'] = R290_PI5_Df_raw['Power']
    R290_PI5_Df['MF_Suc'] = R290_PI5_Df_raw['MF_Suc']
    R290_PI5_Df['Dens_Suc'] = R290_PI5_Df_raw['Dens_Suc']
    R290_PI5_Df['h1'] = R290_PI5_Df_raw['h1']
    R290_PI5_Df['s1'] = R290_PI5_Df_raw['s1']
    R290_PI5_Df['v1'] = R290_PI5_Df_raw['v1']
    R290_PI5_Df['cp1'] = R290_PI5_Df_raw['cp1']
    R290_PI5_Df['h2'] = R290_PI5_Df_raw['h2']
    R290_PI5_Df['h2is'] = R290_PI5_Df_raw['h2is']
    R290_PI5_Df['s2'] = R290_PI5_Df_raw['s2']
    R290_PI5_Df['cp2'] = R290_PI5_Df_raw['cp2']
    R290_PI5_Df['tc'] = R290_PI5_Df_raw['tc']

    # R32_Df['T_Evaps'] = R32_Df_raw['T_Evaps']
    # R32_Df['T_Conds'] = R32_Df_raw['T_Conds']


    return R290_PI5_Df


def clean_R290_PI55_DF():
    R290_PI55_Df = pd.DataFrame()
    R290_PI55_Df['P1_Process'] =R290_PI55_Df_raw['P1_Process']
    R290_PI55_Df['P1_Process'] = R290_PI55_Df_raw['P1_Process']
    R290_PI55_Df['P1_Set'] = R290_PI55_Df_raw['P1_Set']
    R290_PI55_Df['P2_Set'] = R290_PI55_Df_raw['P2_Set']
    R290_PI55_Df['P2_Process'] = R290_PI55_Df_raw['P2_Process']
    R290_PI55_Df['T1_Process'] = R290_PI55_Df_raw['T1_Process']
    R290_PI55_Df['T2_Process'] = R290_PI55_Df_raw['T2_Process']
    R290_PI55_Df['T_Amb_Process'] = R290_PI55_Df_raw['T_Amb_Process']
    R290_PI55_Df['Power'] = R290_PI55_Df_raw['Power']
    R290_PI55_Df['MF_Suc'] = R290_PI55_Df_raw['MF_Suc']
    R290_PI55_Df['Dens_Suc'] = R290_PI55_Df_raw['Dens_Suc']
    R290_PI55_Df['h1'] = R290_PI55_Df_raw['h1']
    R290_PI55_Df['s1'] = R290_PI55_Df_raw['s1']
    R290_PI55_Df['v1'] = R290_PI55_Df_raw['v1']
    R290_PI55_Df['cp1'] = R290_PI55_Df_raw['cp1']
    R290_PI55_Df['h2'] = R290_PI55_Df_raw['h2']
    R290_PI55_Df['h2is'] = R290_PI55_Df_raw['h2is']
    R290_PI55_Df['s2'] = R290_PI55_Df_raw['s2']
    R290_PI55_Df['cp2'] = R290_PI55_Df_raw['cp2']
    R290_PI55_Df['tc'] = R290_PI55_Df_raw['tc']

    # R32_Df['T_Evaps'] = R32_Df_raw['T_Evaps']
    # R32_Df['T_Conds'] = R32_Df_raw['T_Conds']


    return R290_PI55_Df

def clean_R290_PI6_DF():
    R290_PI6_Df = pd.DataFrame()
    R290_PI6_Df['P1_Process'] =R290_PI6_Df_raw['P1_Process']
    R290_PI6_Df['P1_Process'] = R290_PI6_Df_raw['P1_Process']
    R290_PI6_Df['P1_Set'] = R290_PI6_Df_raw['P1_Set']
    R290_PI6_Df['P2_Set'] = R290_PI6_Df_raw['P2_Set']
    R290_PI6_Df['P2_Process'] = R290_PI6_Df_raw['P2_Process']
    R290_PI6_Df['T1_Process'] = R290_PI6_Df_raw['T1_Process']
    R290_PI6_Df['T2_Process'] = R290_PI6_Df_raw['T2_Process']
    R290_PI6_Df['T_Amb_Process'] = R290_PI6_Df_raw['T_Amb_Process']
    R290_PI6_Df['Power'] = R290_PI6_Df_raw['Power']
    R290_PI6_Df['MF_Suc'] = R290_PI6_Df_raw['MF_Suc']
    R290_PI6_Df['Dens_Suc'] = R290_PI6_Df_raw['Dens_Suc']
    R290_PI6_Df['h1'] = R290_PI6_Df_raw['h1']
    R290_PI6_Df['s1'] = R290_PI6_Df_raw['s1']
    R290_PI6_Df['v1'] = R290_PI6_Df_raw['v1']
    R290_PI6_Df['cp1'] = R290_PI6_Df_raw['cp1']
    R290_PI6_Df['h2'] = R290_PI6_Df_raw['h2']
    R290_PI6_Df['h2is'] = R290_PI6_Df_raw['h2is']
    R290_PI6_Df['s2'] = R290_PI6_Df_raw['s2']
    R290_PI6_Df['cp2'] = R290_PI6_Df_raw['cp2']
    R290_PI6_Df['tc'] = R290_PI6_Df_raw['tc']

    # R32_Df['T_Evaps'] = R32_Df_raw['T_Evaps']
    # R32_Df['T_Conds'] = R32_Df_raw['T_Conds']


    return R290_PI6_Df

def clean_R290_PI65_DF():
    R290_PI65_Df = pd.DataFrame()
    R290_PI65_Df['P1_Process'] =R290_PI65_Df_raw['P1_Process']
    R290_PI65_Df['P1_Process'] = R290_PI65_Df_raw['P1_Process']
    R290_PI65_Df['P1_Set'] = R290_PI65_Df_raw['P1_Set']
    R290_PI65_Df['P2_Set'] = R290_PI65_Df_raw['P2_Set']
    R290_PI65_Df['P2_Process'] = R290_PI65_Df_raw['P2_Process']
    R290_PI65_Df['T1_Process'] = R290_PI65_Df_raw['T1_Process']
    R290_PI65_Df['T2_Process'] = R290_PI65_Df_raw['T2_Process']
    R290_PI65_Df['T_Amb_Process'] = R290_PI65_Df_raw['T_Amb_Process']
    R290_PI65_Df['Power'] = R290_PI65_Df_raw['Power']
    R290_PI65_Df['MF_Suc'] = R290_PI65_Df_raw['MF_Suc']
    R290_PI65_Df['Dens_Suc'] = R290_PI65_Df_raw['Dens_Suc']
    R290_PI65_Df['h1'] = R290_PI65_Df_raw['h1']
    R290_PI65_Df['s1'] = R290_PI65_Df_raw['s1']
    R290_PI65_Df['v1'] = R290_PI65_Df_raw['v1']
    R290_PI65_Df['cp1'] = R290_PI65_Df_raw['cp1']
    R290_PI65_Df['h2'] = R290_PI65_Df_raw['h2']
    R290_PI65_Df['h2is'] = R290_PI65_Df_raw['h2is']
    R290_PI65_Df['s2'] = R290_PI65_Df_raw['s2']
    R290_PI65_Df['cp2'] = R290_PI65_Df_raw['cp2']
    R290_PI65_Df['tc'] = R290_PI65_Df_raw['tc']

    # R32_Df['T_Evaps'] = R32_Df_raw['T_Evaps']
    # R32_Df['T_Conds'] = R32_Df_raw['T_Conds']


    return R290_PI65_Df

def clean_R410A_PI3_DF():
    R410A_PI3_Df = pd.DataFrame()
    R410A_PI3_Df['P1_Process'] =R410A_PI3_Df_raw['P1_Process']
    R410A_PI3_Df['P1_Process'] = R410A_PI3_Df_raw['P1_Process']
    R410A_PI3_Df['P1_Set'] = R410A_PI3_Df_raw['P1_Set']
    R410A_PI3_Df['P2_Set'] = R410A_PI3_Df_raw['P2_Set']
    R410A_PI3_Df['P2_Process'] = R410A_PI3_Df_raw['P2_Process']
    R410A_PI3_Df['T1_Process'] = R410A_PI3_Df_raw['T1_Process']
    R410A_PI3_Df['T2_Process'] = R410A_PI3_Df_raw['T2_Process']
    R410A_PI3_Df['T_Amb_Process'] = R410A_PI3_Df_raw['T_Amb_Process']
    R410A_PI3_Df['Power'] = R410A_PI3_Df_raw['Power']
    R410A_PI3_Df['MF_Suc'] = R410A_PI3_Df_raw['MF_Suc']
    R410A_PI3_Df['Dens_Suc'] = R410A_PI3_Df_raw['Dens_Suc']
    R410A_PI3_Df['h1'] = R410A_PI3_Df_raw['h1']
    R410A_PI3_Df['s1'] = R410A_PI3_Df_raw['s1']
    R410A_PI3_Df['v1'] = R410A_PI3_Df_raw['v1']
    R410A_PI3_Df['cp1'] = R410A_PI3_Df_raw['cp1']
    R410A_PI3_Df['h2'] = R410A_PI3_Df_raw['h2']
    R410A_PI3_Df['h2is'] = R410A_PI3_Df_raw['h2is']
    R410A_PI3_Df['s2'] = R410A_PI3_Df_raw['s2']
    R410A_PI3_Df['cp2'] = R410A_PI3_Df_raw['cp2']
    R410A_PI3_Df['tc'] = R410A_PI3_Df_raw['tc']

    # R32_Df['T_Evaps'] = R32_Df_raw['T_Evaps']
    # R32_Df['T_Conds'] = R32_Df_raw['T_Conds']


    return R410A_PI3_Df

def clean_R410A_PI35_DF():
    R410A_PI35_Df = pd.DataFrame()
    R410A_PI35_Df['P1_Process'] =R410A_PI35_Df_raw['P1_Process']
    R410A_PI35_Df['P1_Process'] = R410A_PI35_Df_raw['P1_Process']
    R410A_PI35_Df['P1_Set'] = R410A_PI35_Df_raw['P1_Set']
    R410A_PI35_Df['P2_Set'] = R410A_PI35_Df_raw['P2_Set']
    R410A_PI35_Df['P2_Process'] = R410A_PI35_Df_raw['P2_Process']
    R410A_PI35_Df['T1_Process'] = R410A_PI35_Df_raw['T1_Process']
    R410A_PI35_Df['T2_Process'] = R410A_PI35_Df_raw['T2_Process']
    R410A_PI35_Df['T_Amb_Process'] = R410A_PI35_Df_raw['T_Amb_Process']
    R410A_PI35_Df['Power'] = R410A_PI35_Df_raw['Power']
    R410A_PI35_Df['MF_Suc'] = R410A_PI35_Df_raw['MF_Suc']
    R410A_PI35_Df['Dens_Suc'] = R410A_PI35_Df_raw['Dens_Suc']
    R410A_PI35_Df['h1'] = R410A_PI35_Df_raw['h1']
    R410A_PI35_Df['s1'] = R410A_PI35_Df_raw['s1']
    R410A_PI35_Df['v1'] = R410A_PI35_Df_raw['v1']
    R410A_PI35_Df['cp1'] = R410A_PI35_Df_raw['cp1']
    R410A_PI35_Df['h2'] = R410A_PI35_Df_raw['h2']
    R410A_PI35_Df['h2is'] = R410A_PI35_Df_raw['h2is']
    R410A_PI35_Df['s2'] = R410A_PI35_Df_raw['s2']
    R410A_PI35_Df['cp2'] = R410A_PI35_Df_raw['cp2']
    R410A_PI35_Df['tc'] = R410A_PI35_Df_raw['tc']

    # R32_Df['T_Evaps'] = R32_Df_raw['T_Evaps']
    # R32_Df['T_Conds'] = R32_Df_raw['T_Conds']


    return R410A_PI35_Df


def clean_R410A_PI4_DF():
    R410A_PI4_Df = pd.DataFrame()

    R410A_PI4_Df['P1_Process'] = R410A_PI4_Df_raw['P1_Process']
    R410A_PI4_Df['P1_Set'] = R410A_PI4_Df_raw['P1_Set']
    R410A_PI4_Df['P2_Set'] = R410A_PI4_Df_raw['P2_Set']
    R410A_PI4_Df['P2_Process'] = R410A_PI4_Df_raw['P2_Process']
    R410A_PI4_Df['T1_Process'] = R410A_PI4_Df_raw['T1_Process']
    R410A_PI4_Df['T2_Process'] = R410A_PI4_Df_raw['T2_Process']
    R410A_PI4_Df['T_Amb_Process'] = R410A_PI4_Df_raw['T_Amb_Process']
    R410A_PI4_Df['Power'] = R410A_PI4_Df_raw['Power']
    R410A_PI4_Df['MF_Suc'] = R410A_PI4_Df_raw['MF_Suc']
    R410A_PI4_Df['Dens_Suc'] = R410A_PI4_Df_raw['Dens_Suc']
    R410A_PI4_Df['h1'] = R410A_PI4_Df_raw['h1']
    R410A_PI4_Df['s1'] = R410A_PI4_Df_raw['s1']
    R410A_PI4_Df['v1'] = R410A_PI4_Df_raw['v1']
    R410A_PI4_Df['cp1'] = R410A_PI4_Df_raw['cp1']
    R410A_PI4_Df['h2'] = R410A_PI4_Df_raw['h2']
    R410A_PI4_Df['h2is'] = R410A_PI4_Df_raw['h2is']
    R410A_PI4_Df['s2'] = R410A_PI4_Df_raw['s2']
    R410A_PI4_Df['cp2'] = R410A_PI4_Df_raw['cp2']
    R410A_PI4_Df['tc'] = R410A_PI4_Df_raw['tc']

    # R32_Df['T_Evaps'] = R32_Df_raw['T_Evaps']
    # R32_Df['T_Conds'] = R32_Df_raw['T_Conds']


    return R410A_PI4_Df
def clean_R410A_PI42_DF():
    R410A_PI42_Df = pd.DataFrame()

    R410A_PI42_Df['P1_Process'] = R410A_PI42_Df_raw['P1_Process']
    R410A_PI42_Df['P1_Set'] = R410A_PI42_Df_raw['P1_Set']
    R410A_PI42_Df['P2_Set'] = R410A_PI42_Df_raw['P2_Set']
    R410A_PI42_Df['P2_Process'] = R410A_PI42_Df_raw['P2_Process']
    R410A_PI42_Df['T1_Process'] = R410A_PI42_Df_raw['T1_Process']
    R410A_PI42_Df['T2_Process'] = R410A_PI42_Df_raw['T2_Process']
    R410A_PI42_Df['T_Amb_Process'] = R410A_PI42_Df_raw['T_Amb_Process']
    R410A_PI42_Df['Power'] = R410A_PI42_Df_raw['Power']
    R410A_PI42_Df['MF_Suc'] = R410A_PI42_Df_raw['MF_Suc']
    R410A_PI42_Df['Dens_Suc'] = R410A_PI42_Df_raw['Dens_Suc']
    R410A_PI42_Df['h1'] = R410A_PI42_Df_raw['h1']
    R410A_PI42_Df['s1'] = R410A_PI42_Df_raw['s1']
    R410A_PI42_Df['v1'] = R410A_PI42_Df_raw['v1']
    R410A_PI42_Df['cp1'] = R410A_PI42_Df_raw['cp1']
    R410A_PI42_Df['h2'] = R410A_PI42_Df_raw['h2']
    R410A_PI42_Df['h2is'] = R410A_PI42_Df_raw['h2is']
    R410A_PI42_Df['s2'] = R410A_PI42_Df_raw['s2']
    R410A_PI42_Df['cp2'] = R410A_PI42_Df_raw['cp2']
    R410A_PI42_Df['tc'] = R410A_PI42_Df_raw['tc']

    # R32_Df['T_Evaps'] = R32_Df_raw['T_Evaps']
    # R32_Df['T_Conds'] = R32_Df_raw['T_Conds']


    return R410A_PI42_Df
def clean_R410A_PI45_DF():
    R410A_PI45_Df = pd.DataFrame()
    R410A_PI45_Df['P1_Process'] =R410A_PI45_Df_raw['P1_Process']
    R410A_PI45_Df['P1_Process'] = R410A_PI45_Df_raw['P1_Process']
    R410A_PI45_Df['P1_Set'] = R410A_PI45_Df_raw['P1_Set']
    R410A_PI45_Df['P2_Set'] = R410A_PI45_Df_raw['P2_Set']
    R410A_PI45_Df['P2_Process'] = R410A_PI45_Df_raw['P2_Process']
    R410A_PI45_Df['T1_Process'] = R410A_PI45_Df_raw['T1_Process']
    R410A_PI45_Df['T2_Process'] = R410A_PI45_Df_raw['T2_Process']
    R410A_PI45_Df['T_Amb_Process'] = R410A_PI45_Df_raw['T_Amb_Process']
    R410A_PI45_Df['Power'] = R410A_PI45_Df_raw['Power']
    R410A_PI45_Df['MF_Suc'] = R410A_PI45_Df_raw['MF_Suc']
    R410A_PI45_Df['Dens_Suc'] = R410A_PI45_Df_raw['Dens_Suc']
    R410A_PI45_Df['h1'] = R410A_PI45_Df_raw['h1']
    R410A_PI45_Df['s1'] = R410A_PI45_Df_raw['s1']
    R410A_PI45_Df['v1'] = R410A_PI45_Df_raw['v1']
    R410A_PI45_Df['cp1'] = R410A_PI45_Df_raw['cp1']
    R410A_PI45_Df['h2'] = R410A_PI45_Df_raw['h2']
    R410A_PI45_Df['h2is'] = R410A_PI45_Df_raw['h2is']
    R410A_PI45_Df['s2'] = R410A_PI45_Df_raw['s2']
    R410A_PI45_Df['cp2'] = R410A_PI45_Df_raw['cp2']
    R410A_PI45_Df['tc'] = R410A_PI45_Df_raw['tc']

    # R32_Df['T_Evaps'] = R32_Df_raw['T_Evaps']
    # R32_Df['T_Conds'] = R32_Df_raw['T_Conds']


    return R410A_PI45_Df

def clean_R410A_PI5_DF():
    R410A_PI5_Df = pd.DataFrame()
    R410A_PI5_Df['P1_Process'] =R410A_PI5_Df_raw['P1_Process']
    R410A_PI5_Df['P1_Process'] = R410A_PI5_Df_raw['P1_Process']
    R410A_PI5_Df['P1_Set'] = R410A_PI5_Df_raw['P1_Set']
    R410A_PI5_Df['P2_Set'] = R410A_PI5_Df_raw['P2_Set']
    R410A_PI5_Df['P2_Process'] = R410A_PI5_Df_raw['P2_Process']
    R410A_PI5_Df['T1_Process'] = R410A_PI5_Df_raw['T1_Process']
    R410A_PI5_Df['T2_Process'] = R410A_PI5_Df_raw['T2_Process']
    R410A_PI5_Df['T_Amb_Process'] = R410A_PI5_Df_raw['T_Amb_Process']
    R410A_PI5_Df['Power'] = R410A_PI5_Df_raw['Power']
    R410A_PI5_Df['MF_Suc'] = R410A_PI5_Df_raw['MF_Suc']
    R410A_PI5_Df['Dens_Suc'] = R410A_PI5_Df_raw['Dens_Suc']
    R410A_PI5_Df['h1'] = R410A_PI5_Df_raw['h1']
    R410A_PI5_Df['s1'] = R410A_PI5_Df_raw['s1']
    R410A_PI5_Df['v1'] = R410A_PI5_Df_raw['v1']
    R410A_PI5_Df['cp1'] = R410A_PI5_Df_raw['cp1']
    R410A_PI5_Df['h2'] = R410A_PI5_Df_raw['h2']
    R410A_PI5_Df['h2is'] = R410A_PI5_Df_raw['h2is']
    R410A_PI5_Df['s2'] = R410A_PI5_Df_raw['s2']
    R410A_PI5_Df['cp2'] = R410A_PI5_Df_raw['cp2']
    R410A_PI5_Df['tc'] = R410A_PI5_Df_raw['tc']

    # R32_Df['T_Evaps'] = R32_Df_raw['T_Evaps']
    # R32_Df['T_Conds'] = R32_Df_raw['T_Conds']


    return R410A_PI5_Df

def clean_R410A_PI55_DF():
    R410A_PI55_Df = pd.DataFrame()
    R410A_PI55_Df['P1_Process'] =R410A_PI55_Df_raw['P1_Process']
    R410A_PI55_Df['P1_Process'] = R410A_PI55_Df_raw['P1_Process']
    R410A_PI55_Df['P1_Set'] = R410A_PI55_Df_raw['P1_Set']
    R410A_PI55_Df['P2_Set'] = R410A_PI55_Df_raw['P2_Set']
    R410A_PI55_Df['P2_Process'] = R410A_PI55_Df_raw['P2_Process']
    R410A_PI55_Df['T1_Process'] = R410A_PI55_Df_raw['T1_Process']
    R410A_PI55_Df['T2_Process'] = R410A_PI55_Df_raw['T2_Process']
    R410A_PI55_Df['T_Amb_Process'] = R410A_PI55_Df_raw['T_Amb_Process']
    R410A_PI55_Df['Power'] = R410A_PI55_Df_raw['Power']
    R410A_PI55_Df['MF_Suc'] = R410A_PI55_Df_raw['MF_Suc']
    R410A_PI55_Df['Dens_Suc'] = R410A_PI55_Df_raw['Dens_Suc']
    R410A_PI55_Df['h1'] = R410A_PI55_Df_raw['h1']
    R410A_PI55_Df['s1'] = R410A_PI55_Df_raw['s1']
    R410A_PI55_Df['v1'] = R410A_PI55_Df_raw['v1']
    R410A_PI55_Df['cp1'] = R410A_PI55_Df_raw['cp1']
    R410A_PI55_Df['h2'] = R410A_PI55_Df_raw['h2']
    R410A_PI55_Df['h2is'] = R410A_PI55_Df_raw['h2is']
    R410A_PI55_Df['s2'] = R410A_PI55_Df_raw['s2']
    R410A_PI55_Df['cp2'] = R410A_PI55_Df_raw['cp2']
    R410A_PI55_Df['tc'] = R410A_PI55_Df_raw['tc']

    # R32_Df['T_Evaps'] = R32_Df_raw['T_Evaps']
    # R32_Df['T_Conds'] = R32_Df_raw['T_Conds']


    return R410A_PI55_Df
def clean_R410A_PI6_DF():
    R410A_PI6_Df = pd.DataFrame()
    R410A_PI6_Df['P1_Process'] =R410A_PI6_Df_raw['P1_Process']
    R410A_PI6_Df['P1_Process'] = R410A_PI6_Df_raw['P1_Process']
    R410A_PI6_Df['P1_Set'] = R410A_PI6_Df_raw['P1_Set']
    R410A_PI6_Df['P2_Set'] = R410A_PI6_Df_raw['P2_Set']
    R410A_PI6_Df['P2_Process'] = R410A_PI6_Df_raw['P2_Process']
    R410A_PI6_Df['T1_Process'] = R410A_PI6_Df_raw['T1_Process']
    R410A_PI6_Df['T2_Process'] = R410A_PI6_Df_raw['T2_Process']
    R410A_PI6_Df['T_Amb_Process'] = R410A_PI6_Df_raw['T_Amb_Process']
    R410A_PI6_Df['Power'] = R410A_PI6_Df_raw['Power']
    R410A_PI6_Df['MF_Suc'] = R410A_PI6_Df_raw['MF_Suc']
    R410A_PI6_Df['Dens_Suc'] = R410A_PI6_Df_raw['Dens_Suc']
    R410A_PI6_Df['h1'] = R410A_PI6_Df_raw['h1']
    R410A_PI6_Df['s1'] = R410A_PI6_Df_raw['s1']
    R410A_PI6_Df['v1'] = R410A_PI6_Df_raw['v1']
    R410A_PI6_Df['cp1'] = R410A_PI6_Df_raw['cp1']
    R410A_PI6_Df['h2'] = R410A_PI6_Df_raw['h2']
    R410A_PI6_Df['h2is'] = R410A_PI6_Df_raw['h2is']
    R410A_PI6_Df['s2'] = R410A_PI6_Df_raw['s2']
    R410A_PI6_Df['cp2'] = R410A_PI6_Df_raw['cp2']
    R410A_PI6_Df['tc'] = R410A_PI6_Df_raw['tc']

    # R32_Df['T_Evaps'] = R32_Df_raw['T_Evaps']
    # R32_Df['T_Conds'] = R32_Df_raw['T_Conds']


    return R410A_PI6_Df
def clean_R410A_PI65_DF():
    R410A_PI65_Df = pd.DataFrame()
    R410A_PI65_Df['P1_Process'] =R410A_PI65_Df_raw['P1_Process']
    R410A_PI65_Df['P1_Process'] = R410A_PI65_Df_raw['P1_Process']
    R410A_PI65_Df['P1_Set'] = R410A_PI65_Df_raw['P1_Set']
    R410A_PI65_Df['P2_Set'] = R410A_PI65_Df_raw['P2_Set']
    R410A_PI65_Df['P2_Process'] = R410A_PI65_Df_raw['P2_Process']
    R410A_PI65_Df['T1_Process'] = R410A_PI65_Df_raw['T1_Process']
    R410A_PI65_Df['T2_Process'] = R410A_PI65_Df_raw['T2_Process']
    R410A_PI65_Df['T_Amb_Process'] = R410A_PI65_Df_raw['T_Amb_Process']
    R410A_PI65_Df['Power'] = R410A_PI65_Df_raw['Power']
    R410A_PI65_Df['MF_Suc'] = R410A_PI65_Df_raw['MF_Suc']
    R410A_PI65_Df['Dens_Suc'] = R410A_PI65_Df_raw['Dens_Suc']
    R410A_PI65_Df['h1'] = R410A_PI65_Df_raw['h1']
    R410A_PI65_Df['s1'] = R410A_PI65_Df_raw['s1']
    R410A_PI65_Df['v1'] = R410A_PI65_Df_raw['v1']
    R410A_PI65_Df['cp1'] = R410A_PI65_Df_raw['cp1']
    R410A_PI65_Df['h2'] = R410A_PI65_Df_raw['h2']
    R410A_PI65_Df['h2is'] = R410A_PI65_Df_raw['h2is']
    R410A_PI65_Df['s2'] = R410A_PI65_Df_raw['s2']
    R410A_PI65_Df['cp2'] = R410A_PI65_Df_raw['cp2']
    R410A_PI65_Df['tc'] = R410A_PI65_Df_raw['tc']

    # R32_Df['T_Evaps'] = R32_Df_raw['T_Evaps']
    # R32_Df['T_Conds'] = R32_Df_raw['T_Conds']


    return R410A_PI65_Df

def clean_R454C_PI35_DF():
    R454C_PI35_Df = pd.DataFrame()
    R454C_PI35_Df['P1_Process'] =R454C_PI35_Df_raw['P1_Process']
    R454C_PI35_Df['P1_Process'] = R454C_PI35_Df_raw['P1_Process']
    R454C_PI35_Df['P1_Set'] = R454C_PI35_Df_raw['P1_Set']
    R454C_PI35_Df['P2_Set'] = R454C_PI35_Df_raw['P2_Set']
    R454C_PI35_Df['P2_Process'] = R454C_PI35_Df_raw['P2_Process']
    R454C_PI35_Df['T1_Process'] = R454C_PI35_Df_raw['T1_Process']
    R454C_PI35_Df['T2_Process'] = R454C_PI35_Df_raw['T2_Process']
    R454C_PI35_Df['T_Amb_Process'] = R454C_PI35_Df_raw['T_Amb_Process']
    R454C_PI35_Df['Power'] = R454C_PI35_Df_raw['Power']
    R454C_PI35_Df['MF_Suc'] = R454C_PI35_Df_raw['MF_Suc']
    R454C_PI35_Df['Dens_Suc'] = R454C_PI35_Df_raw['Dens_Suc']
    R454C_PI35_Df['h1'] = R454C_PI35_Df_raw['h1']
    R454C_PI35_Df['s1'] = R454C_PI35_Df_raw['s1']
    R454C_PI35_Df['v1'] = R454C_PI35_Df_raw['v1']
    R454C_PI35_Df['cp1'] = R454C_PI35_Df_raw['cp1']
    R454C_PI35_Df['h2'] = R454C_PI35_Df_raw['h2']
    R454C_PI35_Df['h2is'] = R454C_PI35_Df_raw['h2is']
    R454C_PI35_Df['s2'] = R454C_PI35_Df_raw['s2']
    R454C_PI35_Df['cp2'] = R454C_PI35_Df_raw['cp2']
    R454C_PI35_Df['tc'] = R454C_PI35_Df_raw['tc']

    # R32_Df['T_Evaps'] = R32_Df_raw['T_Evaps']
    # R32_Df['T_Conds'] = R32_Df_raw['T_Conds']


    return R454C_PI35_Df


def clean_R454C_PI45_DF():
    R454C_PI45_Df = pd.DataFrame()
    R454C_PI45_Df['P1_Process'] =R454C_PI45_Df_raw['P1_Process']
    R454C_PI45_Df['P1_Process'] = R454C_PI45_Df_raw['P1_Process']
    R454C_PI45_Df['P1_Set'] = R454C_PI45_Df_raw['P1_Set']
    R454C_PI45_Df['P2_Set'] = R454C_PI45_Df_raw['P2_Set']
    R454C_PI45_Df['P2_Process'] = R454C_PI45_Df_raw['P2_Process']
    R454C_PI45_Df['T1_Process'] = R454C_PI45_Df_raw['T1_Process']
    R454C_PI45_Df['T2_Process'] = R454C_PI45_Df_raw['T2_Process']
    R454C_PI45_Df['T_Amb_Process'] = R454C_PI45_Df_raw['T_Amb_Process']
    R454C_PI45_Df['Power'] = R454C_PI45_Df_raw['Power']
    R454C_PI45_Df['MF_Suc'] = R454C_PI45_Df_raw['MF_Suc']
    R454C_PI45_Df['Dens_Suc'] = R454C_PI45_Df_raw['Dens_Suc']
    R454C_PI45_Df['h1'] = R454C_PI45_Df_raw['h1']
    R454C_PI45_Df['s1'] = R454C_PI45_Df_raw['s1']
    R454C_PI45_Df['v1'] = R454C_PI45_Df_raw['v1']
    R454C_PI45_Df['cp1'] = R454C_PI45_Df_raw['cp1']
    R454C_PI45_Df['h2'] = R454C_PI45_Df_raw['h2']
    R454C_PI45_Df['h2is'] = R454C_PI45_Df_raw['h2is']
    R454C_PI45_Df['s2'] = R454C_PI45_Df_raw['s2']
    R454C_PI45_Df['cp2'] = R454C_PI45_Df_raw['cp2']
    R454C_PI45_Df['tc'] = R454C_PI45_Df_raw['tc']

    # R32_Df['T_Evaps'] = R32_Df_raw['T_Evaps']
    # R32_Df['T_Conds'] = R32_Df_raw['T_Conds']


    return R454C_PI45_Df

def clean_R454C_PI5_DF():
    R454C_PI5_Df = pd.DataFrame()
    R454C_PI5_Df['P1_Process'] =R454C_PI5_Df_raw['P1_Process']
    R454C_PI5_Df['P1_Process'] = R454C_PI5_Df_raw['P1_Process']
    R454C_PI5_Df['P1_Set'] = R454C_PI5_Df_raw['P1_Set']
    R454C_PI5_Df['P2_Set'] = R454C_PI5_Df_raw['P2_Set']
    R454C_PI5_Df['P2_Process'] = R454C_PI5_Df_raw['P2_Process']
    R454C_PI5_Df['T1_Process'] = R454C_PI5_Df_raw['T1_Process']
    R454C_PI5_Df['T2_Process'] = R454C_PI5_Df_raw['T2_Process']
    R454C_PI5_Df['T_Amb_Process'] = R454C_PI5_Df_raw['T_Amb_Process']
    R454C_PI5_Df['Power'] = R454C_PI5_Df_raw['Power']
    R454C_PI5_Df['MF_Suc'] = R454C_PI5_Df_raw['MF_Suc']
    R454C_PI5_Df['Dens_Suc'] = R454C_PI5_Df_raw['Dens_Suc']
    R454C_PI5_Df['h1'] = R454C_PI5_Df_raw['h1']
    R454C_PI5_Df['s1'] = R454C_PI5_Df_raw['s1']
    R454C_PI5_Df['v1'] = R454C_PI5_Df_raw['v1']
    R454C_PI5_Df['cp1'] = R454C_PI5_Df_raw['cp1']
    R454C_PI5_Df['h2'] = R454C_PI5_Df_raw['h2']
    R454C_PI5_Df['h2is'] = R454C_PI5_Df_raw['h2is']
    R454C_PI5_Df['s2'] = R454C_PI5_Df_raw['s2']
    R454C_PI5_Df['cp2'] = R454C_PI5_Df_raw['cp2']
    R454C_PI5_Df['tc'] = R454C_PI5_Df_raw['tc']

    # R32_Df['T_Evaps'] = R32_Df_raw['T_Evaps']
    # R32_Df['T_Conds'] = R32_Df_raw['T_Conds']


    return R454C_PI5_Df

def clean_R454C_PI55_DF():
    R454C_PI55_Df = pd.DataFrame()
    R454C_PI55_Df['P1_Process'] =R454C_PI55_Df_raw['P1_Process']
    R454C_PI55_Df['P1_Process'] = R454C_PI55_Df_raw['P1_Process']
    R454C_PI55_Df['P1_Set'] = R454C_PI55_Df_raw['P1_Set']
    R454C_PI55_Df['P2_Set'] = R454C_PI55_Df_raw['P2_Set']
    R454C_PI55_Df['P2_Process'] = R454C_PI55_Df_raw['P2_Process']
    R454C_PI55_Df['T1_Process'] = R454C_PI55_Df_raw['T1_Process']
    R454C_PI55_Df['T2_Process'] = R454C_PI55_Df_raw['T2_Process']
    R454C_PI55_Df['T_Amb_Process'] = R454C_PI55_Df_raw['T_Amb_Process']
    R454C_PI55_Df['Power'] = R454C_PI55_Df_raw['Power']
    R454C_PI55_Df['MF_Suc'] = R454C_PI55_Df_raw['MF_Suc']
    R454C_PI55_Df['Dens_Suc'] = R454C_PI55_Df_raw['Dens_Suc']
    R454C_PI55_Df['h1'] = R454C_PI55_Df_raw['h1']
    R454C_PI55_Df['s1'] = R454C_PI55_Df_raw['s1']
    R454C_PI55_Df['v1'] = R454C_PI55_Df_raw['v1']
    R454C_PI55_Df['cp1'] = R454C_PI55_Df_raw['cp1']
    R454C_PI55_Df['h2'] = R454C_PI55_Df_raw['h2']
    R454C_PI55_Df['h2is'] = R454C_PI55_Df_raw['h2is']
    R454C_PI55_Df['s2'] = R454C_PI55_Df_raw['s2']
    R454C_PI55_Df['cp2'] = R454C_PI55_Df_raw['cp2']
    R454C_PI55_Df['tc'] = R454C_PI55_Df_raw['tc']

    # R32_Df['T_Evaps'] = R32_Df_raw['T_Evaps']
    # R32_Df['T_Conds'] = R32_Df_raw['T_Conds']


    return R454C_PI55_Df

def clean_R454C_PI6_DF():
    R454C_PI6_Df = pd.DataFrame()
    R454C_PI6_Df['P1_Process'] =R454C_PI6_Df_raw['P1_Process']
    R454C_PI6_Df['P1_Process'] = R454C_PI6_Df_raw['P1_Process']
    R454C_PI6_Df['P1_Set'] = R454C_PI6_Df_raw['P1_Set']
    R454C_PI6_Df['P2_Set'] = R454C_PI6_Df_raw['P2_Set']
    R454C_PI6_Df['P2_Process'] = R454C_PI6_Df_raw['P2_Process']
    R454C_PI6_Df['T1_Process'] = R454C_PI6_Df_raw['T1_Process']
    R454C_PI6_Df['T2_Process'] = R454C_PI6_Df_raw['T2_Process']
    R454C_PI6_Df['T_Amb_Process'] = R454C_PI6_Df_raw['T_Amb_Process']
    R454C_PI6_Df['Power'] = R454C_PI6_Df_raw['Power']
    R454C_PI6_Df['MF_Suc'] = R454C_PI6_Df_raw['MF_Suc']
    R454C_PI6_Df['Dens_Suc'] = R454C_PI6_Df_raw['Dens_Suc']
    R454C_PI6_Df['h1'] = R454C_PI6_Df_raw['h1']
    R454C_PI6_Df['s1'] = R454C_PI6_Df_raw['s1']
    R454C_PI6_Df['v1'] = R454C_PI6_Df_raw['v1']
    R454C_PI6_Df['cp1'] = R454C_PI6_Df_raw['cp1']
    R454C_PI6_Df['h2'] = R454C_PI6_Df_raw['h2']
    R454C_PI6_Df['h2is'] = R454C_PI6_Df_raw['h2is']
    R454C_PI6_Df['s2'] = R454C_PI6_Df_raw['s2']
    R454C_PI6_Df['cp2'] = R454C_PI6_Df_raw['cp2']
    R454C_PI6_Df['tc'] = R454C_PI6_Df_raw['tc']

    # R32_Df['T_Evaps'] = R32_Df_raw['T_Evaps']
    # R32_Df['T_Conds'] = R32_Df_raw['T_Conds']


    return R454C_PI6_Df

def clean_R454C_PI65_DF():
    R454C_PI65_Df = pd.DataFrame()
    R454C_PI65_Df['P1_Process'] =R454C_PI65_Df_raw['P1_Process']
    R454C_PI65_Df['P1_Process'] = R454C_PI65_Df_raw['P1_Process']
    R454C_PI65_Df['P1_Set'] = R454C_PI65_Df_raw['P1_Set']
    R454C_PI65_Df['P2_Set'] = R454C_PI65_Df_raw['P2_Set']
    R454C_PI65_Df['P2_Process'] = R454C_PI65_Df_raw['P2_Process']
    R454C_PI65_Df['T1_Process'] = R454C_PI65_Df_raw['T1_Process']
    R454C_PI65_Df['T2_Process'] = R454C_PI65_Df_raw['T2_Process']
    R454C_PI65_Df['T_Amb_Process'] = R454C_PI65_Df_raw['T_Amb_Process']
    R454C_PI65_Df['Power'] = R454C_PI65_Df_raw['Power']
    R454C_PI65_Df['MF_Suc'] = R454C_PI65_Df_raw['MF_Suc']
    R454C_PI65_Df['Dens_Suc'] = R454C_PI65_Df_raw['Dens_Suc']
    R454C_PI65_Df['h1'] = R454C_PI65_Df_raw['h1']
    R454C_PI65_Df['s1'] = R454C_PI65_Df_raw['s1']
    R454C_PI65_Df['v1'] = R454C_PI65_Df_raw['v1']
    R454C_PI65_Df['cp1'] = R454C_PI65_Df_raw['cp1']
    R454C_PI65_Df['h2'] = R454C_PI65_Df_raw['h2']
    R454C_PI65_Df['h2is'] = R454C_PI65_Df_raw['h2is']
    R454C_PI65_Df['s2'] = R454C_PI65_Df_raw['s2']
    R454C_PI65_Df['cp2'] = R454C_PI65_Df_raw['cp2']
    R454C_PI65_Df['tc'] = R454C_PI65_Df_raw['tc']

    # R32_Df['T_Evaps'] = R32_Df_raw['T_Evaps']
    # R32_Df['T_Conds'] = R32_Df_raw['T_Conds']


    return R454C_PI65_Df

