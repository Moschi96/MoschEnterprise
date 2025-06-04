import pandas as pd
import numpy as np
import sklearn.utils
import xlsxwriter
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeClassifier
from pathlib import Path
import matplotlib.pyplot as plt

from sklearn.tree import DecisionTreeClassifier # Import Decision Tree Classifier
from sklearn.model_selection import train_test_split # Import train_test_split function
from sklearn import metrics #Import scikit-learn metrics module for accuracy calculation

from sklearn.datasets import load_iris
from sklearn.datasets import load_breast_cancer
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split


from sklearn import tree


# Get Data from excel File
dataFolder = Path(__file__).resolve().parent # Absoluter Pfad zum Ordner dieser Datei, findet ihn automatisch heraus
import sys; sys.path.append(str(dataFolder.parent)) # Füge Ordner zur Laufzeitumgebung damit die selbst erstellte Module gefunden werden

print(dataFolder)
''' Diese Datei lädt die Quasistätionären Data in abhängigkeit von dem Verdichtungsverhältnis ein und berechnet damit die Ploss nach Roskosch. '''


'''Lädt die  Input Daten aus dem Script ein'''

from Data_handling.data_cleaning import clean_R32_DF
from Data_handling.data_cleaning import clean_R32_PI25_DF
from Data_handling.data_cleaning import clean_R32_PI3_DF
from Data_handling.data_cleaning import clean_R32_PI35_DF
from Data_handling.data_cleaning import clean_R32_PI4_DF
from Data_handling.data_cleaning import clean_R32_PI45_DF
from Data_handling.data_cleaning import clean_R32_PI5_DF

R32_Mean = clean_R32_DF()
'''Lädt die Berechnungen in das Script'''

from Calculation.Ploss_calculation import P_R32_Pi25
from Calculation.Ploss_calculation import P_R32_Pi3
from Calculation.Ploss_calculation import P_R32_Pi35
from Calculation.Ploss_calculation import P_R32_Pi4
from Calculation.Ploss_calculation import P_R32_Pi45
from Calculation.Ploss_calculation import P_R32_Pi5

R32_PI25_Df = clean_R32_PI25_DF()
R32_PI25_Df['PI']= 2.5
R32_PI3_Df =  clean_R32_PI3_DF()
R32_PI3_Df['PI'] = 3.0
R32_PI35_Df = clean_R32_PI35_DF()
R32_PI35_Df['PI'] = 3.5
R32_PI4_Df = clean_R32_PI4_DF()
R32_PI4_Df['PI'] = 4.0
R32_PI45_Df = clean_R32_PI45_DF()
R32_PI45_Df['PI'] = 4.5
R32_PI5_Df = clean_R32_PI5_DF()
R32_PI5_Df['PI'] = 5.0



P_R32_PI25 = P_R32_Pi25(R32_PI25_Df)
P_R32_PI25['PI'] = 2.5
P_R32_PI3 = P_R32_Pi3(R32_PI3_Df)
P_R32_PI3['PI'] = 3.0
P_R32_PI35 = P_R32_Pi35(R32_PI35_Df)
P_R32_PI35['PI'] = 3.5
P_R32_PI4 = P_R32_Pi4(R32_PI4_Df)
P_R32_PI4['PI'] = 4.0
P_R32_PI45 = P_R32_Pi45(R32_PI45_Df)
P_R32_PI45['PI'] = 4.5
P_R32_PI5 = P_R32_Pi45(R32_PI5_Df)
P_R32_PI5['PI'] = 5.0
#print(R32_PI45_Df)

R32_Df_list = [R32_PI25_Df, R32_PI3_Df, R32_PI35_Df , R32_PI4_Df, R32_PI45_Df, R32_PI5_Df]
R32_Df = pd.concat(R32_Df_list)



P_R32_list = [P_R32_PI25,P_R32_PI3, P_R32_PI35,P_R32_PI4, P_R32_PI45 , P_R32_PI5]
P_R32 = pd.concat(P_R32_list)
P_R32['KM'] = 1

R32_Df['P_loss'] = P_R32['P_loss']





#print(P_R32 , 'Das ist P_R32')
from Data_handling.data_cleaning import clean_R290_DF
from Data_handling.data_cleaning import clean_R290_PI25_DF
from Data_handling.data_cleaning import clean_R290_PI3_DF
from Data_handling.data_cleaning import clean_R290_PI35_DF
from Data_handling.data_cleaning import clean_R290_PI4_DF
from Data_handling.data_cleaning import clean_R290_PI45_DF
from Data_handling.data_cleaning import clean_R290_PI5_DF
from Data_handling.data_cleaning import clean_R290_PI55_DF
from Data_handling.data_cleaning import clean_R290_PI6_DF
from Data_handling.data_cleaning import clean_R290_PI65_DF

R290_Mean = clean_R290_DF()

from Calculation.Ploss_calculation import P_R290_Pi25
from Calculation.Ploss_calculation import P_R290_Pi3
from Calculation.Ploss_calculation import P_R290_Pi35
from Calculation.Ploss_calculation import P_R290_Pi4
from Calculation.Ploss_calculation import P_R290_Pi45
from Calculation.Ploss_calculation import P_R290_Pi5
from Calculation.Ploss_calculation import P_R290_Pi55
from Calculation.Ploss_calculation import P_R290_Pi6
from Calculation.Ploss_calculation import P_R290_Pi65

R290_PI25_Df = clean_R290_PI25_DF()
R290_PI25_Df['PI'] = 2.5
R290_PI3_Df = clean_R290_PI3_DF()
R290_PI3_Df['PI'] = 3.0
R290_PI35_Df = clean_R290_PI35_DF()
R290_PI35_Df['PI'] = 3.5
R290_PI4_Df = clean_R290_PI4_DF()
R290_PI4_Df['PI'] = 4.0
R290_PI45_Df = clean_R290_PI45_DF()
R290_PI45_Df['PI'] = 4.5
R290_PI5_Df = clean_R290_PI5_DF()
R290_PI5_Df['PI'] = 5.0
R290_PI55_Df = clean_R290_PI55_DF()
R290_PI55_Df['PI'] = 5.5
R290_PI6_Df = clean_R290_PI6_DF()
R290_PI6_Df['PI'] = 6.0
R290_PI65_Df = clean_R290_PI65_DF()
R290_PI65_Df['PI'] = 6.5

P_R290_PI25 = P_R290_Pi25(R290_PI25_Df)
P_R290_PI25['PI'] = 2.5
P_R290_PI3 = P_R290_Pi3(R290_PI3_Df)
P_R290_PI3['PI'] = 3.0
P_R290_PI35 = P_R290_Pi35(R290_PI35_Df)
P_R290_PI35['PI'] = 3.5
P_R290_PI4 = P_R290_Pi4(R290_PI4_Df)
P_R290_PI4['PI'] = 4.0
P_R290_PI45 = P_R290_Pi45(R290_PI45_Df)
P_R290_PI45['PI'] = 4.5
P_R290_PI5 = P_R290_Pi5(R290_PI5_Df)
P_R290_PI5['PI'] = 5.0
P_R290_PI55 = P_R290_Pi55(R290_PI55_Df)
P_R290_PI55['PI'] = 5.5
P_R290_PI6 = P_R290_Pi6(R290_PI6_Df)
P_R290_PI6['PI'] = 6.0
P_R290_PI65 = P_R290_Pi65(R290_PI65_Df)
P_R290_PI65['PI'] = 6.5

P_R290_list = [P_R290_PI25, P_R290_PI3 , P_R290_PI35, P_R290_PI4 , P_R290_PI45, P_R290_PI5 , P_R290_PI55, P_R290_PI6, P_R290_PI65]
R290_Df_list = [R290_PI25_Df,R290_PI3_Df, R290_PI35_Df, R290_PI4_Df, R290_PI45_Df, R290_PI5_Df, R290_PI55_Df, R290_PI6_Df, R290_PI65_Df]
P_R290 = pd.concat(P_R290_list)
P_R290['KM'] = 2

R290_Df = pd.concat(R290_Df_list)
R290_Df['P_loss'] = P_R290['P_loss']

from Data_handling.data_cleaning import clean_R410A_DF
from Data_handling.data_cleaning import clean_R410A_PI3_DF
from Data_handling.data_cleaning import clean_R410A_PI35_DF
from Data_handling.data_cleaning import clean_R410A_PI4_DF
from Data_handling.data_cleaning import clean_R410A_PI42_DF
from Data_handling.data_cleaning import clean_R410A_PI45_DF
from Data_handling.data_cleaning import clean_R410A_PI5_DF
from Data_handling.data_cleaning import clean_R410A_PI55_DF
from Data_handling.data_cleaning import clean_R410A_PI6_DF
from Data_handling.data_cleaning import clean_R410A_PI65_DF

R410A_Mean = clean_R410A_DF()

from Calculation.Ploss_calculation import P_R410A_Pi3
from Calculation.Ploss_calculation import P_R410A_Pi35
from Calculation.Ploss_calculation import P_R410A_Pi4
from Calculation.Ploss_calculation import P_R410A_Pi45
from Calculation.Ploss_calculation import P_R410A_Pi5
from Calculation.Ploss_calculation import P_R410A_Pi55
from Calculation.Ploss_calculation import P_R410A_Pi6
from Calculation.Ploss_calculation import P_R410A_Pi65




R410A_PI3_Df = clean_R410A_PI3_DF()
R410A_PI3_Df['PI'] = 3.0
R410A_PI35_Df = clean_R410A_PI35_DF()
R410A_PI35_Df['PI'] = 3.5
R410A_PI4_Df = clean_R410A_PI4_DF()
R410A_PI4_Df['PI'] = 4.0
#R410A_PI42_Df = clean_R410A_PI42_DF()

R410A_PI45_Df = clean_R410A_PI45_DF()
R410A_PI45_Df['PI'] = 4.5
R410A_PI5_Df = clean_R410A_PI5_DF()
R410A_PI5_Df['PI'] = 5.0
R410A_PI55_Df = clean_R410A_PI55_DF()
R410A_PI55_Df['PI'] = 5.5
R410A_PI6_Df = clean_R410A_PI6_DF()
R410A_PI6_Df['PI'] = 6.0
R410A_PI65_Df = clean_R410A_PI65_DF()
R410A_PI65_Df['PI'] = 6.5

'''
R410A_PI4_List = [R410A_PI4_Df, R410A_PI42_Df]
R410A_PI4_Df = pd.concat(R410A_PI4_List)
R410A_PI4_Df['PI'] = 4.0 '''

P_R410A_PI3 = P_R410A_Pi3(R410A_PI3_Df)
P_R410A_PI3['PI'] = 3.0
P_R410A_PI35 = P_R410A_Pi35(R410A_PI35_Df)
P_R410A_PI35['PI'] = 3.5
P_R410A_PI4 = P_R410A_Pi4(R410A_PI4_Df)
P_R410A_PI4['PI'] = 4.0
P_R410A_PI45 = P_R410A_Pi45(R410A_PI45_Df)
P_R410A_PI45['PI'] = 4.5
P_R410A_PI5 = P_R410A_Pi5(R410A_PI5_Df)
P_R410A_PI5['PI'] = 5.0
P_R410A_PI55 = P_R410A_Pi55(R410A_PI55_Df)
P_R410A_PI55['PI'] = 5.5
P_R410A_PI6 = P_R410A_Pi6(R410A_PI6_Df)
P_R410A_PI6['PI'] = 6.0
P_R410A_PI65 = P_R410A_Pi65(R410A_PI65_Df)
P_R410A_PI65['PI'] = 6.5
P_R410A_list = [P_R410A_PI3, P_R410A_PI35,P_R410A_PI4,P_R410A_PI45,P_R410A_PI5,P_R410A_PI55, P_R410A_PI6,P_R410A_PI65]
P_R410A = pd.concat(P_R410A_list)
P_R410A['KM'] = 3
R410A_Df_list = [R410A_PI3_Df, R410A_PI35_Df, R410A_PI4_Df, R410A_PI45_Df, R410A_PI5_Df, R410A_PI55_Df, R410A_PI6_Df, R410A_PI65_Df]
R410A_Df = pd.concat(R410A_Df_list)



#R410A_Df['P_loss'] = P_R410A['P_loss']


from Data_handling.data_cleaning import clean_R454C_DF
from Data_handling.data_cleaning import clean_R454C_PI35_DF
from Data_handling.data_cleaning import clean_R454C_PI45_DF
from Data_handling.data_cleaning import clean_R454C_PI5_DF
from Data_handling.data_cleaning import clean_R454C_PI55_DF
from Data_handling.data_cleaning import clean_R454C_PI6_DF
from Data_handling.data_cleaning import clean_R454C_PI65_DF


R454C_Mean = clean_R454C_DF()
from Calculation.Ploss_calculation import P_R454C_Pi35

from Calculation.Ploss_calculation import P_R454C_Pi45
from Calculation.Ploss_calculation import P_R454C_Pi5
from Calculation.Ploss_calculation import P_R454C_Pi55
from Calculation.Ploss_calculation import P_R454C_Pi6
from Calculation.Ploss_calculation import P_R454C_Pi65

R454C_PI35_Df = clean_R454C_PI35_DF()
R454C_PI35_Df['PI'] = 3.5
R454C_PI45_Df = clean_R454C_PI45_DF()
R454C_PI45_Df['PI'] = 4.5
R454C_PI5_Df = clean_R454C_PI5_DF()
R454C_PI5_Df['PI'] = 5.0
R454C_PI55_Df = clean_R454C_PI55_DF()
R454C_PI55_Df['PI'] = 5.5
R454C_PI6_Df = clean_R454C_PI6_DF()
R454C_PI6_Df['PI'] = 6.0
R454C_PI65_Df = clean_R454C_PI65_DF()
R454C_PI65_Df['PI'] = 6.5

R454C_list = [R454C_PI35_Df, R454C_PI45_Df, R454C_PI5_Df, R454C_PI55_Df, R454C_PI6_Df, R454C_PI65_Df]
R454C_Df= pd.concat(R454C_list)

P_R454C_PI35 = P_R454C_Pi35(R454C_PI35_Df)
P_R454C_PI35['PI'] = 3.5
P_R454C_PI45 = P_R454C_Pi45(R454C_PI45_Df)
P_R454C_PI45['PI'] = 4.5
P_R454C_PI5 = P_R454C_Pi5(R454C_PI5_Df)
P_R454C_PI5['PI'] = 5.0
P_R454C_PI55 = P_R454C_Pi55(R454C_PI55_Df)
P_R454C_PI55['PI'] = 5.5
P_R454C_PI6 = P_R454C_Pi6(R454C_PI6_Df)
P_R454C_PI6['PI'] = 6.0
P_R454C_PI65 = P_R454C_Pi65(R454C_PI65_Df)
P_R454C_PI65['PI'] = 6.5

P_R454C_list = [P_R454C_PI35,P_R454C_PI45, P_R454C_PI5, P_R454C_PI55,P_R454C_PI6, P_R454C_PI65]

P_R454C = pd.concat(P_R454C_list)
P_R454C['KM'] = 4


PI3= [P_R32_PI3, P_R290_PI3, P_R410A_PI3]
PI35 = [P_R32_PI35, P_R290_PI35, P_R410A_PI35, P_R454C_PI35]
PI4 = [P_R290_PI4, ]
PI45 = [P_R290_PI45, P_R410A_PI45, P_R454C_PI45]
PI5 = [P_R290_PI5, P_R410A_PI5, P_R454C_PI5]
PI55 = [P_R290_PI55, P_R410A_PI55, P_R454C_PI55]
PI6 = [P_R290_PI6, P_R410A_PI6, P_R454C_PI6]
PI65 = [P_R410A_PI65, P_R454C_PI65]





KM_List = [P_R32, P_R290 , P_R410A , P_R454C]
full = pd.concat(KM_List)

P_R32['PI_Process'] = P_R32['P2_Process'] / P_R32['P1_Process']
P_R290['PI_Process'] = P_R290['P2_Process'] / P_R290['P1_Process']
P_R410A['PI_Process'] = P_R410A['P2_Process'] / P_R410A['P1_Process']
P_R454C['PI_Process'] = P_R454C['P2_Process'] / P_R454C['P1_Process']

#### ALLE DataFrames sind vollständig eingeladen. Jetzt gehts rund.

from pyfluids import Fluid, FluidsList
import CoolProp
import CoolProp.CoolProp as CP





def Calc_LR_ds(Df):
    LR = LinearRegression()
    Res_Df = pd.DataFrame()
    LR.fit(Df[['PI_Process']], Df[['delta_s']])
    x = LR.coef_[0]
    y = LR.intercept_
    z = LR.score(Df[['PI_Process']], Df[['delta_s']])
    Res_Df['COE'] = x
    Res_Df['LIN'] = y
    Res_Df['Score'] = z
    return Res_Df





#LR_ds_R32 = Calc_LR_ds(P_R32)
#LR_ds_R290 = Calc_LR_ds(P_R290)
#LR_ds_R410A = Calc_LR_ds(P_R410A)
#LR_ds_R454C = Calc_LR_ds(P_R454C)

'''
Corr_R32 = P_R454C.corr()
Res_R32 = Corr_R32['eta_is_rosk'].sort_values(ascending= False)
print(Res_R32)
'''
temp_T2_is = []
temp_h2_is = []
sp_list =[]
T2_is_list = []


def calc_cis_mod(df , KM): #RKm_PIXX_DF

    for i in range(0, len(df)):
        h = pd.DataFrame()
        s1 = df.iloc[i]['s1'] * 1000
        h1 = df.iloc[i]['h1'] * 1000
        p2 = df.iloc[i]['P2_Process'] * 100000
        p1 = df.iloc[i]['P1_Process'] * 100000
        t2 = df.iloc[i]['T2_Process'] +273.15
        h2_is = CP.PropsSI('H', 'P', p2 , 'S', s1, str(KM))/1000
        T2_is = CP.PropsSI('d(H)/d(S)|P','P',p2,'S',s1, str(KM))
        sp = CP.PropsSI('S'   , 'P', p2 , 'H' , h1, str(KM)) / 1000
        rho = CP.PropsSI('D', 'P', p1, 'H', h1 , str(KM))

        rho_list.append(rho)
        sp_list.append(sp)
        T2_is_list.append(T2_is)


    return T2_is_list,rho_list


rho_list = []
T2_is_list = []
T2_is_list32 , rholist32 = calc_cis_mod(R32_Df, 'R32')
R32_Df['T2_is'] = T2_is_list32
R32_Df['rho_1'] = rholist32



T2_is_list = []
rho_list = []
T2_is_list290 , rholist290 = calc_cis_mod(R290_Df, 'R290')
R290_Df['T2_is'] = T2_is_list290
R290_Df['rho_1'] = rholist290




T2_is_list = []
rho_list = []
T2_is_list410A , rholist410 = calc_cis_mod(R410A_Df, 'R410A')
R410A_Df['T2_is'] = T2_is_list410A
R410A_Df['rho_1'] = rholist410

print(R410A_Df, 'Das ist R410A_Df')

''' Das ist für R454C. Das funktioniert aber mit CoolProp nicht. Auf Refprop umarbeiten
T2_is_list = []
rho_list = []
T2_is_list454C , rholist454C = calc_cis_mod(R454C_Df, 'R454C')
R410A_Df['T2_is'] = T2_is_list454C
R410A_Df['rho_1'] = rholist454C


'''
#print(LR_ds_R32, LR_ds_R290, LR_ds_R410A, LR_ds_R454C)








R32_Df['delta_s'] = R32_Df['s2'] - R32_Df['s1']
R290_Df['delta_s'] = R290_Df['s2'] - R290_Df['s1']
R410A_Df['delta_s'] = R410A_Df['s2'] - R410A_Df['s1']
#R454C_Df['delta_s'] = R454C_Df['s2'] - R454C_Df['s1']
from Calculation.BA_Calculation import calc_h2_mod


R32_Df= calc_h2_mod(R32_Df)

R290_Df = calc_h2_mod(R290_Df)

R410A_Df = calc_h2_mod(R410A_Df)





Results_R32 = R32_Df.groupby('PI').mean()
Results_R290 = R290_Df.groupby('PI').mean()

Results_R410A = R410A_Df.groupby('PI').mean()



Results_R32 =  Results_R32.round(2)
Results_R32 =  Results_R32.abs()

Results_R290 =  Results_R290.round(2)
Results_R290 =  Results_R290.abs()
#Results_R454C = R454C_Df.groupby('PI')

Results_R410A =  Results_R410A.round(2)
Results_R410A =  Results_R410A.abs()

print(Results_R32,'Das ist R32')
print(Results_R290, 'Das ist R290')
print(Results_R410A, 'Das ist R410A')


Results_R32.to_excel('Results_R32.xlsx')
Results_R290.to_excel('Results_R290.xlsx')
Results_R410A.to_excel('Results_R410A.xlsx')
def Anal_Ploss(df):

    df['ds'] = df['s2'] - df['s1']
    dh_mod = df['T2_is_mod'] * df['ds']
    df['h_loss_mod'] = dh_mod
    df['dh'] = df['h2'] - df['h2is']
    df['P_loss_theo'] = df['MF_Suc'] * df['ds'] * df['T2_is_mod']
    df['Ver_Param'] = df['P_loss'] - df['P_loss_theo']
    return df







def Calc_Cis(df):

    Z = df['T2_is_mod']* (df['s1'] + df['sp'])
    N = df['h2_is_mod'] - df['h1']
    cis1 = Z/N


    df['Cis1'] = cis1
    X = df['s1'] * (1 + cis1)
    Y = 1 - cis1
    res = X/Y

    df['s2_theo'] = res

    return df









from Plot.Plot_eta import plot_eta_vergleich

# Plot_Ploss_PI(Calc_Mod_R32_Df, KM= 'R32')
R32_PI25_Df=R32_PI25_Df.groupby('P1_Set').mean()
R32_PI3_Df=R32_PI3_Df.groupby('P1_Set').mean()
R32_PI35_Df=R32_PI35_Df.groupby('P1_Set').mean()
R32_PI4_Df=R32_PI4_Df.groupby('P1_Set').mean()
R32_PI45_Df=R32_PI45_Df.groupby('P1_Set').mean()
R32_PI5_Df=R32_PI5_Df.groupby('P1_Set').mean()


R290_PI25_Df = R290_PI25_Df.groupby(['P1_Set']).mean()
R290_PI3_Df = R290_PI3_Df.groupby(['P1_Set']).mean()
R290_PI35_Df = R290_PI35_Df.groupby(['P1_Set']).mean()
R290_PI4_Df = R290_PI4_Df.groupby(['P1_Set']).mean()
R290_PI45_Df = R290_PI45_Df.groupby(['P1_Set']).mean()
R290_PI5_Df = R290_PI5_Df.groupby(['P1_Set']).mean()
R290_PI55_Df = R290_PI55_Df.groupby(['P1_Set']).mean()
R290_PI6_Df = R290_PI6_Df.groupby(['P1_Set']).mean()
R290_PI65_Df = R290_PI35_Df.groupby(['P1_Set']).mean()


R410A_PI3_Df = R410A_PI3_Df.groupby('P1_Set').mean()
R410A_PI35_Df =R410A_PI35_Df.groupby('P1_Set').mean()
R410A_PI4_Df = R410A_PI4_Df .groupby('P1_Set').mean()
R410A_PI45_Df = R410A_PI45_Df.groupby('P1_Set').mean()
R410A_PI5_Df = R410A_PI5_Df .groupby('P1_Set').mean()
R410A_PI55_Df =R410A_PI55_Df.groupby('P1_Set').mean()
R410A_PI6_Df =R410A_PI6_Df.groupby('P1_Set').mean()
R410A_PI65_Df =R410A_PI65_Df.groupby('P1_Set').mean()


R454C_PI45_Df = R454C_PI45_Df.groupby('P1_Set').mean()
R454C_PI5_Df = R454C_PI5_Df.groupby('P1_Set').mean()
R454C_PI55_Df = R454C_PI55_Df.groupby('P1_Set').mean()
R454C_PI6_Df = R454C_PI6_Df.groupby('P1_Set').mean()
R454C_PI65_Df = R454C_PI65_Df.groupby('P1_Set').mean()


from Plot.Plot_Alles import plot_MF_R32
from Plot.Plot_Alles import plot_MF_R410A
#plot_MF_R32(D25 = R32_PI25_Df,D3= R32_PI3_Df, D35= R32_PI35_Df, KM='R32')
#print(Calc_Mod_R32_Df, 'Das ist Calc Mod')#
#plot_MF_R410A(D3=R410A_PI3_Df, D35=R410A_PI35_Df,D4= R410A_PI4_Df, D45=R410A_PI45_Df, D5= R410A_PI5_Df, D55=R410A_PI55_Df, D6=R410A_PI6_Df, D65=R410A_PI65_Df)





from Calculation.BA_Calculation import calc_delta
from Calculation.BA_Calculation import calc_eta_is

'''
eta_is = calc_eta_is(R32_Df)
P_R32['eta_is'] = eta_is


eta_is = calc_eta_is(R290_Df)
P_R290['eta_is'] = eta_is
eta_is = calc_eta_is(R410A_Df)
P_R410A['eta_is'] = eta_is
eta_is = calc_eta_is(R454C_Df)
P_R454C['eta_is'] = eta_is

P_R32 = calc_delta(P_R32)
P_R290 = calc_delta(P_R290)
P_R410A = calc_delta(P_R410A)
P_R454C = calc_delta(P_R454C)

print(P_R32)

Eta_R32 = pd.DataFrame()
Eta_R290 = pd.DataFrame()
Eta_R410A = pd.DataFrame()
Eta_R454C = pd.DataFrame()

Eta_R32 = P_R32.groupby(['PI']).mean()
Eta_R290 = P_R290.groupby(['PI']).mean()
Eta_R410A = P_R410A.groupby(['PI']).mean()
Eta_R454C = P_R454C.groupby(['PI']).mean()




###Volumetrischer Wirkungsgrad lambda
lam_R32 = R32_Mean.groupby(['PI_Set']).mean()
lam_R290 = R290_Mean.groupby(['PI_Set']).mean()
lam_R410A = R410A_Mean.groupby(['PI_Set']).mean()
lam_R454C = R454C_Mean.groupby(['PI_Set']).mean()


cve_R32 = R32_Df.groupby(['PI']).mean()
cve_R290 = R290_Df.groupby(['PI']).mean()
cve_R410A = R410A_Df.groupby(['PI']).mean()


Eta_R32['lambda'] = lam_R32['lambda']
Eta_R290['lambda'] = lam_R290['lambda']
Eta_R410A['lambda'] = lam_R410A['lambda']
Eta_R454C['lambda'] = lam_R454C['lambda']

print(Eta_R32,'Das ist ETA_R32')
print(lam_R32, 'Das ist lam_R32')
print(cve_R32, 'Das sit cve_R32')

Eta_R32.to_excel('Eta_R32.xlsx')
Eta_R290.to_excel('Eta_R290.xlsx')
Eta_R410A.to_excel('Eta_R410A.xlsx')
Eta_R454C.to_excel('Eta_R454C.xlsx')





rho_R32_R290 = cve_R32/cve_R290
rho_R32_R410A = cve_R32 / cve_R410A


Eta_R290R32= Eta_R290/Eta_R32
Eta_R410AR32= Eta_R410A/Eta_R32

from Plot.Plot_Alles import plot_lambda

plot_lambda(D1=Eta_R32, D2= Eta_R290, D3=Eta_R410A,D4= Eta_R454C)

from Plot.Plot_eta import plot_eta_proR32

plot_eta_proR32(rho_R32_R290, rho_R32_R410A)
'''
'''
plot_eta_vergleich(Eta_R32,lam_R32, KM='R32')
plot_eta_vergleich(Eta_R290,lam_R290, KM='R290')
plot_eta_vergleich(Eta_R410A, lam_R410A, KM='R410A')
plot_eta_vergleich(Eta_R454C, lam_R454C, KM='R454C')'''

from Plot.Plot_eta import plot_eta_komplett
#plot_eta_komplett(Eta_R32, Eta_R290, Eta_R410A, Eta_R454C)



def Plot_Ver_Para(df, ds  ):
    fig, ax = plt.subplots(1,1,figsize=(13, 8), layout='constrained',sharey=True )
    #Festlegen der Achsenbeschriftung
    font1 = {'family':'serif','color':'black','size':15}
    font2 = {'family':'serif','color':'black','size':10}
    plt.title('PI' , fontdict= font1)
    plt.xlabel('PI', fontdict= font2)
    plt.ylabel('Power Loss [W]', fontdict=font2)
    plt.grid(color = 'black', linestyle= '--', linewidth = 0.5)

    plt.scatter( df['PI'] , df['Ver_Param'] , color = 'red' ,label = 'R32')
    plt.scatter(ds['PI'], ds['Ver_Param'], color='blue', label='R290')



    plt.legend()
    plt.show()


#Plot_Ver_Para(Calc_Mod_R32_Df, Calc_Mod_R290_Df)

def Plot_Ver_Parads(df, ds  ):
    fig, ax = plt.subplots(1,1,figsize=(13, 8), layout='constrained',sharey=True )
    #Festlegen der Achsenbeschriftung
    font1 = {'family':'serif','color':'black','size':15}
    font2 = {'family':'serif','color':'black','size':10}
    plt.title('PI' , fontdict= font1)
    plt.xlabel('PI', fontdict= font2)
    plt.ylabel('Power Loss [W]', fontdict=font2)
    plt.grid(color = 'black', linestyle= '--', linewidth = 0.5)

    plt.scatter( df['ds'] , df['Ver_Param'] , color = 'red' ,label = 'R32')
    plt.scatter(ds['ds'], ds['Ver_Param'], color='blue', label='R290')



    plt.legend()
    plt.show()
#Plot_Ver_Parads(Calc_Mod_R32_Df, Calc_Mod_R290_Df)
'''
import CoolProp
from CoolProp.Plots import PropertyPlot
from CoolProp.Plots import SimpleCompressionCycle
pp = PropertyPlot('HEOS::R410A', 'HS', unit_system='EUR')
pp.calc_isolines(CoolProp.iQ, num=11)
cycle = SimpleCompressionCycle('HEOS::R410A', 'PH', unit_system='EUR')
T0 = 280
pp.state.update(CoolProp.QT_INPUTS,0.0,T0-10)
p0 = pp.state.keyed_output(CoolProp.iP)
T2 = 310
pp.state.update(CoolProp.QT_INPUTS,1.0,T2+15)
p2 = pp.state.keyed_output(CoolProp.iP)
pp.calc_isolines(CoolProp.iT, [T0-273.15,T2-273.15], num=2)
cycle.simple_solve(T0, p0, T2, p2, 0.7, SI=True)
cycle.steps = 50
sc = cycle.get_state_changes()
pp.draw_process(sc)
import matplotlib.pyplot as plt
plt.close(cycle.figure)
pp.show()


from CoolProp.Plots import PropertyPlot
plot = PropertyPlot('HEOS::R410A', 'HS', unit_system='EUR', tp_limits='ORC')
plot.calc_isolines(CoolProp.iQ, num=11)
plot.calc_isolines(CoolProp.iP, iso_range=[1,50], num=2, rounding=True)
plot.draw()
plot.isolines.clear()
plot.props[CoolProp.iP]['color'] = 'green'
plot.props[CoolProp.iP]['lw'] = '0.5'
plot.calc_isolines(CoolProp.iP, iso_range=[1,50], num=5, rounding=False)
plot.show()
'''
