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


from Data_handling.data_cleaning import clean_R32_PI25_DF
from Data_handling.data_cleaning import clean_R32_PI3_DF
from Data_handling.data_cleaning import clean_R32_PI35_DF
from Data_handling.data_cleaning import clean_R32_PI4_DF
from Data_handling.data_cleaning import clean_R32_PI45_DF

'''Lädt die Berechnungen in das Script'''

from Calculation.Ploss_calculation import P_R32_Pi25
from Calculation.Ploss_calculation import P_R32_Pi3
from Calculation.Ploss_calculation import P_R32_Pi35
from Calculation.Ploss_calculation import P_R32_Pi4
from Calculation.Ploss_calculation import P_R32_Pi45


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
#print(R32_PI45_Df)

R32_Df_list = [R32_PI25_Df, R32_PI3_Df, R32_PI35_Df , R32_PI4_Df, R32_PI45_Df]
R32_Df = pd.concat(R32_Df_list)



P_R32_list = [P_R32_PI25,P_R32_PI3, P_R32_PI35,P_R32_PI4, P_R32_PI45 ]
P_R32 = pd.concat(P_R32_list)
P_R32['KM'] = 1

R32_Df['P_loss'] = P_R32['P_loss']





#print(P_R32 , 'Das ist P_R32')
from Data_handling.data_cleaning import clean_R290_PI25_DF
from Data_handling.data_cleaning import clean_R290_PI3_DF
from Data_handling.data_cleaning import clean_R290_PI35_DF
from Data_handling.data_cleaning import clean_R290_PI4_DF
from Data_handling.data_cleaning import clean_R290_PI45_DF
from Data_handling.data_cleaning import clean_R290_PI5_DF
from Data_handling.data_cleaning import clean_R290_PI55_DF
from Data_handling.data_cleaning import clean_R290_PI6_DF
from Data_handling.data_cleaning import clean_R290_PI65_DF



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


from Data_handling.data_cleaning import clean_R410A_PI3_DF
from Data_handling.data_cleaning import clean_R410A_PI35_DF
from Data_handling.data_cleaning import clean_R410A_PI4_DF
from Data_handling.data_cleaning import clean_R410A_PI42_DF
from Data_handling.data_cleaning import clean_R410A_PI45_DF
from Data_handling.data_cleaning import clean_R410A_PI5_DF
from Data_handling.data_cleaning import clean_R410A_PI55_DF
from Data_handling.data_cleaning import clean_R410A_PI6_DF
from Data_handling.data_cleaning import clean_R410A_PI65_DF



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
R410A_PI42_Df = clean_R410A_PI42_DF()

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

R410A_PI4_List = [R410A_PI4_Df, R410A_PI42_Df]
R410A_PI4_Df = pd.concat(R410A_PI4_List)
R410A_PI4_Df['PI'] = 4.0

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
P_R410A_list = [P_R410A_PI35, P_R410A_PI35,P_R410A_PI4,P_R410A_PI45,P_R410A_PI5,P_R410A_PI55, P_R410A_PI6,P_R410A_PI65]
P_R410A = pd.concat(P_R410A_list)
P_R410A['KM'] = 3
R410A_Df_list = [R410A_PI3_Df, R410A_PI35_Df, R410A_PI4_Df, R410A_PI42_Df, R410A_PI45_Df, R410A_PI5_Df, R410A_PI55_Df, R410A_PI6_Df, R410A_PI65_Df]
R410A_Df = pd.concat(R410A_Df_list)



#R410A_Df['P_loss'] = P_R410A['P_loss']



from Data_handling.data_cleaning import clean_R454C_PI35_DF
from Data_handling.data_cleaning import clean_R454C_PI45_DF
from Data_handling.data_cleaning import clean_R454C_PI5_DF
from Data_handling.data_cleaning import clean_R454C_PI55_DF
from Data_handling.data_cleaning import clean_R454C_PI6_DF
from Data_handling.data_cleaning import clean_R454C_PI65_DF

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
def calc_cis_mod(df , KM): #RKm_PIXX_DF
    for i in range(0, len(df)):
        h = pd.DataFrame()
        s1 = df.iloc[i]['s1'] * 1000
        h1 = df.iloc[i]['h1'] * 1000
        p2 = df.iloc[i]['P2_Process'] * 100000
        t2 = df.iloc[i]['T2_Process'] +273.15
        h2_is = CP.PropsSI('H', 'P', p2 , 'S', s1, str(KM))/1000
        T2_is = CP.PropsSI('d(H)/d(S)|P','P',p2,'S',s1, str(KM))
        sp = CP.PropsSI('S'   , 'P', p2 , 'H' , h1, str(KM)) / 1000



        sp_list.append(sp)



    return sp_list



R32_Df['sp'] = calc_cis_mod(R32_Df, KM = 'R32')

print(R32_Df)






#print(LR_ds_R32, LR_ds_R290, LR_ds_R410A, LR_ds_R454C)

from pyfluids import Fluid, FluidsList
import CoolProp
import CoolProp.CoolProp as CP


temp_T2_is = []
temp_h2_is = []
def calc_dh_mod(df , KM): #RKm_PIXX_DF
    for i in range(0, len(df)):
        h = pd.DataFrame()
        s1 = df.iloc[i]['s1'] * 1000
        p2 = df.iloc[i]['P2_Process'] * 100000
        t2 = df.iloc[i]['T2_Process'] +273.15
        h2_is = CP.PropsSI('H', 'P', p2 , 'S', s1, str(KM))/1000
        T2_is = CP.PropsSI('d(H)/d(S)|P','P',p2,'S',s1, str(KM))
        #cp = CP.PropsSI('d(Hmass)/d(T)|P', 'P', p2, 'T', t2, str(KM))



        temp_T2_is.append(T2_is)
        temp_h2_is.append(h2_is)


    return df , temp_h2_is , temp_T2_is


def Anal_Ploss(df):

    df['ds'] = df['s2'] - df['s1']
    dh_mod = df['T2_is_mod'] * df['ds']
    df['h_loss_mod'] = dh_mod
    df['dh'] = df['h2'] - df['h2is']
    df['P_loss_theo'] = df['MF_Suc'] * df['ds'] * df['T2_is_mod']
    df['Ver_Param'] = df['P_loss'] - df['P_loss_theo']
    return df

Calc_Mod_R32_Df , xd , tis = calc_dh_mod(R32_Df, KM='R32')

Calc_Mod_R32_Df['h2_is_mod'] = xd
Calc_Mod_R32_Df['T2_is_mod'] = tis



print(Calc_Mod_R32_Df)

#Calc_Mod_R290_Df = calc_dh_mod(R290_Df, KM = 'R290')
#Calc_Mod_R410A_Df = calc_dh_mod(R410A_Df, KM = 'R410A')
#print(Calc_Mod_R32_Df, 'Das ist der Calc_Mod_R32d')

#Calc_Mod_R32_PI35_Df = calc_dh_mod(R32_PI35_Df , KM= 'R32')
#Calc_Mod_R290_PI35_Df = calc_dh_mod(R290_PI35_Df, KM= 'R290')
#Calc_Mod_R410A_PI35_Df = calc_dh_mod(R410A_PI35_Df , KM = 'R410A')


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

Calc_Mod_R32_Df = Calc_Cis(Calc_Mod_R32_Df)
print(Calc_Mod_R32_Df)
def Plot_Ploss_Vergleich(df ):
    fig, ax = plt.subplots(1,1,figsize=(13, 8), layout='constrained',sharey=True )
    #Festlegen der Achsenbeschriftung
    font1 = {'family':'serif','color':'black','size':15}
    font2 = {'family':'serif','color':'black','size':10}
    plt.title('P_Loss Vergleich' , fontdict= font1)
    plt.xlabel('delta_s', fontdict= font2)
    plt.ylabel('Power Loss [W]', fontdict=font2)
    plt.grid(color = 'black', linestyle= '--', linewidth = 0.5)

    plt.scatter( df['ds'] , df['P_loss'] , color = 'red' ,label = 'Ploss')
    plt.scatter(df['ds'] , df['P_loss_theo'] , color = 'blue' ,label = 'P_loss_theo')


    plt.legend()
    plt.show()
#Plot_Ploss_Vergleich(Calc_Mod_R32_Df )


def Plot_Ploss_PI(df, KM  ):
    fig, ax = plt.subplots(1,1,figsize=(13, 8), layout='constrained',sharey=True )
    #Festlegen der Achsenbeschriftung
    font1 = {'family':'serif','color':'black','size':15}
    font2 = {'family':'serif','color':'black','size':10}
    plt.title('PI' , fontdict= font1)
    plt.xlabel('PI', fontdict= font2)
    plt.ylabel('Power Loss [W]', fontdict=font2)
    plt.grid(color = 'black', linestyle= '--', linewidth = 0.5)

    plt.scatter( df['PI'] , df['P_loss'] , color = 'red' ,label = 'Ploss')
    plt.scatter(df['PI'] , df['P_loss_theo'] , color = 'blue' ,label = 'P_loss_theo')


    plt.legend()
    plt.show()



# Plot_Ploss_PI(Calc_Mod_R32_Df, KM= 'R32')




#print(Calc_Mod_R32_Df, 'Das ist Calc Mod')




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
pp = PropertyPlot('HEOS::R32', 'HS', unit_system='EUR')
pp.calc_isolines(CoolProp.iQ, num=11)
cycle = SimpleCompressionCycle('HEOS::R32', 'PH', unit_system='EUR')
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
plot = PropertyPlot('HEOS::R32', 'HS', unit_system='EUR', tp_limits='ORC')
plot.calc_isolines(CoolProp.iQ, num=11)
plot.calc_isolines(CoolProp.iP, iso_range=[1,50], num=2, rounding=True)
plot.draw()
plot.isolines.clear()
plot.props[CoolProp.iP]['color'] = 'green'
plot.props[CoolProp.iP]['lw'] = '0.5'
plot.calc_isolines(CoolProp.iP, iso_range=[1,50], num=5, rounding=False)
plot.show()
'''
