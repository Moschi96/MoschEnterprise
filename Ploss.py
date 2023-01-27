import pandas as pd
import numpy as np
import xlsxwriter
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeClassifier
from pathlib import Path
import matplotlib.pyplot as plt
# Get Data from excel File
dataFolder = Path(__file__).resolve().parent # Absoluter Pfad zum Ordner dieser Datei, findet ihn automatisch heraus
import sys; sys.path.append(str(dataFolder.parent)) # Füge Ordner zur Laufzeitumgebung damit die selbst erstellte Module gefunden werden
import seaborn as sb
print(dataFolder)
''' Diese Datei lädt die Quasistätionären Data in abhängigkeit von dem Verdichtungsverhältnis ein und berechnet damit die Ploss nach Roskosch. '''


'''Lädt die  Input Daten aus dem Script ein'''


from Data_handling.data_cleaning import clean_R32_PI25_DF
from Data_handling.data_cleaning import clean_R32_PI3_DF
from Data_handling.data_cleaning import clean_R32_PI35_DF
from Data_handling.data_cleaning import clean_R32_PI4_DF
from Data_handling.data_cleaning import clean_R32_PI45_DF
from Data_handling.data_cleaning import clean_R32_DF
'''Lädt die Berechnungen in das Script'''
from Calculation.Ploss_calculation import P_R32
from Calculation.Ploss_calculation import P_R32_Pi25
from Calculation.Ploss_calculation import P_R32_Pi3
from Calculation.Ploss_calculation import P_R32_Pi35
from Calculation.Ploss_calculation import P_R32_Pi4
from Calculation.Ploss_calculation import P_R32_Pi45

R32_DF = clean_R32_DF()
R32_PI25_Df = clean_R32_PI25_DF()
R32_PI3_Df =  clean_R32_PI3_DF()
R32_PI35_Df = clean_R32_PI35_DF()
R32_PI4_Df = clean_R32_PI4_DF()
R32_PI45_Df = clean_R32_PI45_DF()

P_R32=P_R32(R32_DF)
P_R32_PI25 = P_R32_Pi25(R32_PI25_Df)
P_R32_PI3 = P_R32_Pi3(R32_PI3_Df)
P_R32_PI35 = P_R32_Pi35(R32_PI35_Df)
P_R32_PI4 = P_R32_Pi4(R32_PI4_Df)
P_R32_PI45 = P_R32_Pi45(R32_PI45_Df)






LR_R32=pd.DataFrame(columns=['COE','LIN','Score'],
                    index = ['25','3','35','4','45'])


from sklearn.linear_model import LinearRegression

linP_R32_PI25 = LinearRegression()
linP_R32_PI25.fit(P_R32_PI25[['P1_Process']],P_R32_PI25[['P_loss']])



x=linP_R32_PI25.coef_[0]
y=linP_R32_PI25.intercept_
z=linP_R32_PI25.score(P_R32_PI25[['P1_Process']],P_R32_PI25[['P_loss']])


LR_R32.loc['25'] =[x,y,z ]

linP_R32_PI3 = LinearRegression()
linP_R32_PI3.fit(P_R32_PI3[['P1_Process']],P_R32_PI3[['P_loss']])


x =linP_R32_PI3.intercept_
y=linP_R32_PI3.coef_
z=linP_R32_PI3.score(P_R32_PI3[['P1_Process']],P_R32_PI3[['P_loss']])

LR_R32.loc['3'] =[x,y,z ]

linP_R32_PI35 = LinearRegression()
linP_R32_PI35.fit(P_R32_PI35[['P1_Process']],P_R32_PI35[['P_loss']])


y =linP_R32_PI35.intercept_
x =linP_R32_PI35.coef_
z=linP_R32_PI35.score(P_R32_PI35[['P1_Process']],P_R32_PI35[['P_loss']])



LR_R32.loc['35'] =[x,y,z ]
linP_R32_PI4 = LinearRegression()
linP_R32_PI4.fit(P_R32_PI4[['P1_Process']],P_R32_PI4[['P_loss']])


y =linP_R32_PI4.intercept_
x =linP_R32_PI4.coef_
z=linP_R32_PI4.score(P_R32_PI4[['P1_Process']],P_R32_PI4[['P_loss']])
LR_R32.loc['4'] =[x,y,z ]

linP_R32_PI45 = LinearRegression()
linP_R32_PI45.fit(P_R32_PI45[['P1_Process']],P_R32_PI45[['P_loss']])


y = linP_R32_PI45.intercept_
x =linP_R32_PI45.coef_
z=linP_R32_PI45.score(P_R32_PI45[['P1_Process']],P_R32_PI45[['P_loss']])
LR_R32.loc['45'] =[x,y,z ]





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


from Calculation.Ploss_calculation import P_R290
from Calculation.Ploss_calculation import P_R290_Pi25
from Calculation.Ploss_calculation import P_R290_Pi3
from Calculation.Ploss_calculation import P_R290_Pi35
from Calculation.Ploss_calculation import P_R290_Pi4
from Calculation.Ploss_calculation import P_R290_Pi45
from Calculation.Ploss_calculation import P_R290_Pi5
from Calculation.Ploss_calculation import P_R290_Pi55
from Calculation.Ploss_calculation import P_R290_Pi6
from Calculation.Ploss_calculation import P_R290_Pi65

R290_Df = clean_R290_DF()
R290_PI25_Df = clean_R290_PI25_DF()
R290_PI3_Df = clean_R290_PI3_DF()
R290_PI35_Df = clean_R290_PI35_DF()
R290_PI4_Df = clean_R290_PI4_DF()
R290_PI45_Df = clean_R290_PI45_DF()
R290_PI5_Df = clean_R290_PI5_DF()
R290_PI55_Df = clean_R290_PI55_DF()
R290_PI6_Df = clean_R290_PI6_DF()
R290_PI65_Df = clean_R290_PI65_DF()

P_R290= P_R290(R290_Df)
P_R290_PI25 = P_R290_Pi25(R290_PI25_Df)
P_R290_PI3 = P_R290_Pi3(R290_PI3_Df)
P_R290_PI35 = P_R290_Pi35(R290_PI35_Df)
P_R290_PI4 = P_R290_Pi4(R290_PI4_Df)
P_R290_PI45 = P_R290_Pi45(R290_PI45_Df)
P_R290_PI5 = P_R290_Pi5(R290_PI5_Df)
P_R290_PI55 = P_R290_Pi55(R290_PI55_Df)
P_R290_PI6 = P_R290_Pi6(R290_PI6_Df)
P_R290_PI65 = P_R290_Pi65(R290_PI65_Df)

LR_R290=pd.DataFrame(columns=['COE','LIN','Score'],
                    index = ['25','3','35','4','45','5','55','6','65'])

linP_R290_PI25 = LinearRegression()
linP_R290_PI25.fit(P_R290_PI25[['P1_Process']],P_R290_PI25[['P_loss']])



x=linP_R290_PI25.coef_
y=linP_R290_PI25.intercept_
z=linP_R290_PI25.score(P_R290_PI25[['P1_Process']],P_R290_PI25[['P_loss']])


LR_R290.loc['25'] =[x,y,z ]

linP_R290_PI3 = LinearRegression()
linP_R290_PI3.fit(P_R290_PI3[['P1_Process']], P_R290_PI3[['P_loss']])


y =linP_R290_PI3.intercept_
x=linP_R290_PI3.coef_
z=linP_R290_PI3.score(P_R290_PI3[['P1_Process']], P_R290_PI3[['P_loss']])

LR_R290.loc['3'] =[x,y,z ]

linP_R290_PI35 = LinearRegression()
linP_R290_PI35.fit(P_R290_PI35[['P1_Process']], P_R290_PI35[['P_loss']])

y =linP_R290_PI35.intercept_
x =linP_R290_PI35.coef_
z=linP_R290_PI35.score(P_R290_PI35[['P1_Process']], P_R290_PI35[['P_loss']])

LR_R290.loc['35'] =[ x,y,z ]


linP_R290_PI4 = LinearRegression()
linP_R290_PI4.fit(P_R290_PI4[['P1_Process']], P_R290_PI4[['P_loss']])

y =linP_R290_PI4.intercept_
x =linP_R290_PI4.coef_
z=linP_R290_PI4.score(P_R290_PI4[['P1_Process']], P_R290_PI4[['P_loss']])
LR_R290.loc['4'] =[x,y,z ]







linP_R290_PI45 = LinearRegression()
linP_R290_PI45.fit(P_R290_PI45[['P1_Process']], P_R290_PI45[['P_loss']])


y = linP_R290_PI45.intercept_
x =linP_R290_PI45.coef_
z=linP_R290_PI45.score(P_R290_PI45[['P1_Process']], P_R290_PI45[['P_loss']])
LR_R290.loc['45'] =[x,y,z ]

linP_R290_PI5 = LinearRegression()
linP_R290_PI5.fit(P_R290_PI5[['P1_Process']], P_R290_PI5[['P_loss']])


y =linP_R290_PI5.intercept_
x =linP_R290_PI5.coef_
z=linP_R290_PI5.score(P_R290_PI5[['P1_Process']], P_R290_PI5[['P_loss']])
LR_R290.loc['5'] =[x,y,z ]







linP_R290_PI55 = LinearRegression()
linP_R290_PI55.fit(P_R290_PI55[['P1_Process']], P_R290_PI55[['P_loss']])


y = linP_R290_PI55.intercept_
x =linP_R290_PI55.coef_
z=linP_R290_PI55.score(P_R290_PI55[['P1_Process']], P_R290_PI55[['P_loss']])
LR_R290.loc['55'] =[ x,y,z ]

linP_R290_PI6 = LinearRegression()
linP_R290_PI6.fit(P_R290_PI6[['P1_Process']], P_R290_PI6[['P_loss']])


y = linP_R290_PI6.intercept_
x =linP_R290_PI6.coef_
z=linP_R290_PI6.score(P_R290_PI6[['P1_Process']], P_R290_PI6[['P_loss']])
LR_R290.loc['6'] =[x,y,z ]

linP_R290_PI65 = LinearRegression() # [x,y]
linP_R290_PI65.fit(P_R290_PI65[['P1_Process']], P_R290_PI65[['P_loss']])


y = linP_R290_PI65.intercept_
x =linP_R290_PI65.coef_
z=linP_R290_PI65.score(P_R290_PI65[['P1_Process']], P_R290_PI65[['P_loss']])
LR_R290.loc['65'] =[x,y,z ]


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


from Calculation.Ploss_calculation import P_R410A
from Calculation.Ploss_calculation import P_R410A_Pi3
from Calculation.Ploss_calculation import P_R410A_Pi35
from Calculation.Ploss_calculation import P_R410A_Pi4
from Calculation.Ploss_calculation import P_R410A_Pi45
from Calculation.Ploss_calculation import P_R410A_Pi5
from Calculation.Ploss_calculation import P_R410A_Pi55
from Calculation.Ploss_calculation import P_R410A_Pi6
from Calculation.Ploss_calculation import P_R410A_Pi65



R410A_Df = clean_R410A_DF()
R410A_PI3_Df = clean_R410A_PI3_DF()
R410A_PI35_Df = clean_R410A_PI35_DF()
R410A_PI4_Df = clean_R410A_PI4_DF()
R410A_PI42_Df = clean_R410A_PI42_DF()
R410A_PI45_Df = clean_R410A_PI45_DF()
R410A_PI5_Df = clean_R410A_PI5_DF()
R410A_PI55_Df = clean_R410A_PI55_DF()
R410A_PI6_Df = clean_R410A_PI6_DF()
R410A_PI65_Df = clean_R410A_PI65_DF()



R410A_PI4_Df = R410A_PI4_Df.append(R410A_PI42_Df)

print(R410A_PI4_Df)
P_R410A = P_R410A(R410A_Df)
P_R410A_PI3 = P_R410A_Pi3(R410A_PI3_Df)
P_R410A_PI35 = P_R410A_Pi35(R410A_PI35_Df)
P_R410A_PI4 = P_R410A_Pi4(R410A_PI4_Df)
P_R410A_PI45 = P_R410A_Pi45(R410A_PI45_Df)
P_R410A_PI5 = P_R410A_Pi5(R410A_PI5_Df)
P_R410A_PI55 = P_R410A_Pi55(R410A_PI55_Df)
P_R410A_PI6 = P_R410A_Pi6(R410A_PI6_Df)
P_R410A_PI65 = P_R410A_Pi65(R410A_PI65_Df)



LR_R410A=pd.DataFrame(columns=[ 'COE', 'LIN', 'Score'],
                      index = ['3','35','4','45','5','55','6','65'])



linP_R410A_PI3 = LinearRegression()
linP_R410A_PI3.fit(P_R410A_PI3[['P1_Process']], P_R410A_PI3[['P_loss']])


x =linP_R410A_PI3.intercept_
y=linP_R410A_PI3.coef_
z=linP_R410A_PI3.score(P_R410A_PI3[['P1_Process']], P_R410A_PI3[['P_loss']])

LR_R410A.loc['3'] =[ x, y, z]

linP_R410A_PI35 = LinearRegression()
linP_R410A_PI35.fit(P_R410A_PI35[['P1_Process']], P_R410A_PI35[['P_loss']])


y =linP_R410A_PI35.intercept_
x =linP_R410A_PI35.coef_
z=linP_R410A_PI35.score(P_R410A_PI35[['P1_Process']], P_R410A_PI35[['P_loss']])



LR_R410A.loc['35'] =[ x, y, z]



linP_R410A_PI4 = LinearRegression()
linP_R410A_PI4.fit(P_R410A_PI4[['P1_Process']], P_R410A_PI4[['P_loss']])


y =linP_R410A_PI4.intercept_
x =linP_R410A_PI4.coef_
z=linP_R410A_PI4.score(P_R410A_PI4[['P1_Process']], P_R410A_PI4[['P_loss']])
LR_R410A.loc['4'] =[ x, y, z]







linP_R410A_PI45 = LinearRegression()
linP_R410A_PI45.fit(P_R410A_PI45[['P1_Process']], P_R410A_PI45[['P_loss']])


y = linP_R410A_PI45.intercept_
x =linP_R410A_PI45.coef_
z=linP_R410A_PI45.score(P_R410A_PI45[['P1_Process']], P_R410A_PI45[['P_loss']])
LR_R410A.loc['45'] =[ x, y, z]


linP_R410A_PI5 = LinearRegression()
linP_R410A_PI5.fit(P_R410A_PI5[['P1_Process']], P_R410A_PI5[['P_loss']])


y =linP_R410A_PI5.intercept_
x =linP_R410A_PI5.coef_
z=linP_R410A_PI5.score(P_R410A_PI5[['P1_Process']], P_R410A_PI5[['P_loss']])
LR_R410A.loc['5'] =[ x, y, z]







linP_R410A_PI55 = LinearRegression()
linP_R410A_PI55.fit(P_R410A_PI55[['P1_Process']], P_R410A_PI55[['P_loss']])


y = linP_R410A_PI55.intercept_
x =linP_R410A_PI55.coef_
z=linP_R410A_PI55.score(P_R410A_PI55[['P1_Process']], P_R410A_PI55[['P_loss']])
LR_R410A.loc['55'] =[ x, y, z]

linP_R410A_PI6 = LinearRegression()
linP_R410A_PI6.fit(P_R410A_PI6[['P1_Process']], P_R410A_PI6[['P_loss']])


y = linP_R410A_PI6.intercept_
x =linP_R410A_PI6.coef_
z=linP_R410A_PI6.score(P_R410A_PI6[['P1_Process']], P_R410A_PI6[['P_loss']])
LR_R410A.loc['6'] =[ x, y, z]




linP_R410A_PI65 = LinearRegression()
linP_R410A_PI65.fit(P_R410A_PI65[['P1_Process']], P_R410A_PI65[['P_loss']])


y = linP_R410A_PI65.intercept_
x =linP_R410A_PI65.coef_
z=linP_R410A_PI65.score(P_R410A_PI65[['P1_Process']], P_R410A_PI65[['P_loss']])
LR_R410A.loc['65'] =[ x, y, z]



from Data_handling.data_cleaning import clean_R454C_DF
from Data_handling.data_cleaning import clean_R454C_PI35_DF
from Data_handling.data_cleaning import clean_R454C_PI45_DF
from Data_handling.data_cleaning import clean_R454C_PI5_DF
from Data_handling.data_cleaning import clean_R454C_PI55_DF
from Data_handling.data_cleaning import clean_R454C_PI6_DF
from Data_handling.data_cleaning import clean_R454C_PI65_DF

from Calculation.Ploss_calculation import P_R454C
from Calculation.Ploss_calculation import P_R454C_Pi35

from Calculation.Ploss_calculation import P_R454C_Pi45
from Calculation.Ploss_calculation import P_R454C_Pi5
from Calculation.Ploss_calculation import P_R454C_Pi55
from Calculation.Ploss_calculation import P_R454C_Pi6
from Calculation.Ploss_calculation import P_R454C_Pi65

R454C_Df = clean_R454C_DF()
R454C_PI35_Df = clean_R454C_PI35_DF()
R454C_PI45_Df = clean_R454C_PI45_DF()
R454C_PI5_Df = clean_R454C_PI5_DF()
R454C_PI55_Df = clean_R454C_PI55_DF()
R454C_PI6_Df = clean_R454C_PI6_DF()
R454C_PI65_Df = clean_R454C_PI65_DF()


P_R454C = P_R454C(R454C_Df)
P_R454C_PI35 = P_R454C_Pi35(R454C_PI35_Df)
P_R454C_PI45 = P_R454C_Pi45(R454C_PI45_Df)
P_R454C_PI5 = P_R454C_Pi5(R454C_PI5_Df)
P_R454C_PI55 = P_R454C_Pi55(R454C_PI55_Df)
P_R454C_PI6 = P_R454C_Pi6(R454C_PI6_Df)
P_R454C_PI65 = P_R454C_Pi65(R454C_PI65_Df)

LR_R454C=pd.DataFrame(columns=[ 'COE', 'LIN', 'Score'],
                      index = ['35','45','5','55','6','65'])



linP_R454C_PI35 = LinearRegression()
linP_R454C_PI35.fit(P_R454C_PI35[['P1_Process']], P_R454C_PI35[['P_loss']])


y =linP_R454C_PI35.intercept_
x =linP_R454C_PI35.coef_
z=linP_R454C_PI35.score(P_R454C_PI35[['P1_Process']], P_R454C_PI35[['P_loss']])



LR_R454C.loc['35'] =[ x, y, z]

linP_R454C_PI45 = LinearRegression()
linP_R454C_PI45.fit(P_R454C_PI45[['P1_Process']], P_R454C_PI45[['P_loss']])


y =linP_R454C_PI45.intercept_
x =linP_R454C_PI45.coef_
z=linP_R454C_PI45.score(P_R454C_PI45[['P1_Process']], P_R454C_PI45[['P_loss']])



LR_R454C.loc['45'] =[ x, y, z]

linP_R454C_PI5 = LinearRegression()
linP_R454C_PI5.fit(P_R454C_PI5[['P1_Process']], P_R454C_PI5[['P_loss']])


y =linP_R454C_PI5.intercept_
x =linP_R454C_PI5.coef_
z=linP_R454C_PI5.score(P_R454C_PI5[['P1_Process']], P_R454C_PI5[['P_loss']])



LR_R454C.loc['5'] =[x, y, z]

linP_R454C_PI55 = LinearRegression()
linP_R454C_PI55.fit(P_R454C_PI55[['P1_Process']], P_R454C_PI55[['P_loss']])


y =linP_R454C_PI55.intercept_
x =linP_R454C_PI55.coef_
z=linP_R454C_PI55.score(P_R454C_PI55[['P1_Process']], P_R454C_PI55[['P_loss']])



LR_R454C.loc['55'] =[ x, y, z]

linP_R454C_PI6 = LinearRegression()
linP_R454C_PI6.fit(P_R454C_PI6[['P1_Process']], P_R454C_PI6[['P_loss']])


y =linP_R454C_PI6.intercept_
x =linP_R454C_PI6.coef_
z=linP_R454C_PI6.score(P_R454C_PI6[['P1_Process']], P_R454C_PI6[['P_loss']])



LR_R454C.loc['6'] =[ x, y, z]

linP_R454C_PI65 = LinearRegression()
linP_R454C_PI65.fit(P_R454C_PI65[['P1_Process']], P_R454C_PI65[['P_loss']])

y =linP_R454C_PI65.intercept_
x =linP_R454C_PI65.coef_
z=linP_R454C_PI65.score(P_R454C_PI65[['P1_Process']], P_R454C_PI65[['P_loss']])



LR_R454C.loc['65'] =[ x, y, z]




 #Just to save the Protocoll in Excel What am I doing for Random shit :D Merry Christmas
LR_Dic = dataFolder / 'Calculation' / 'Calculation_Data' / 'Linear_Regression_Data' / ''

'''

LR_R32.to_excel(str(LR_Dic) + 'LR_R32.xlsx')
LR_R290.to_excel(str(LR_Dic) + 'LR_R290.xlsx')
LR_R410A.to_excel(str(LR_Dic) +  'LR_R410A.xlsx')
LR_R454C.to_excel(str(LR_Dic)+ 'LR_R454C.xlsx')
'''

from Plot.Plot_Regression import plot_LR_KM_PI
from Plot.Plot_Regression import plot_LR_R32

plot_LR_R32_PI_25 = plot_LR_R32(P_KM_PI=P_R32_PI25, LR_KM_PI= linP_R32_PI25, name= str('R32_PI25'))
plot_LR_R32_PI_3 = plot_LR_R32(P_KM_PI=P_R32_PI3, LR_KM_PI= linP_R32_PI3, name= str('R32_PI3'))
plot_LR_R32_PI_35 = plot_LR_R32(P_KM_PI=P_R32_PI35, LR_KM_PI= linP_R32_PI35, name= str('R32_PI35'))
plot_LR_R32_PI_4 = plot_LR_R32(P_KM_PI=P_R32_PI4, LR_KM_PI= linP_R32_PI4, name= str('R32_PI4'))
plot_LR_R32_PI_45 = plot_LR_R32(P_KM_PI=P_R32_PI45, LR_KM_PI= linP_R32_PI45, name= str('R32_PI45'))


plot_LR_R290_PI_25 = plot_LR_KM_PI(P_KM_PI=P_R290_PI25, LR_KM_PI= linP_R290_PI25, name= str('R290_PI25'))
plot_LR_R290_PI_3 = plot_LR_KM_PI(P_KM_PI=P_R290_PI3, LR_KM_PI= linP_R290_PI3, name= str('R290_PI3'))
plot_LR_R290_PI_35 = plot_LR_KM_PI(P_KM_PI=P_R290_PI35, LR_KM_PI= linP_R290_PI35, name= str('R290_PI35'))
plot_LR_R290_PI_4 = plot_LR_KM_PI(P_KM_PI=P_R290_PI4, LR_KM_PI= linP_R290_PI4, name= str('R290_PI4'))

plot_LR_R290_PI_45 = plot_LR_KM_PI(P_KM_PI=P_R290_PI45, LR_KM_PI= linP_R290_PI45, name= str('R290_PI45'))

plot_LR_R290_PI_5 = plot_LR_KM_PI(P_KM_PI=P_R290_PI5, LR_KM_PI= linP_R290_PI5, name= str('R290_PI5'))
plot_LR_R290_PI_55 = plot_LR_KM_PI(P_KM_PI=P_R290_PI55, LR_KM_PI= linP_R290_PI55, name= str('R290_PI55'))
plot_LR_R290_PI_6 = plot_LR_KM_PI(P_KM_PI=P_R290_PI6, LR_KM_PI= linP_R290_PI6, name= str('R290_PI6'))
plot_LR_R290_PI_65 = plot_LR_KM_PI(P_KM_PI=P_R290_PI65, LR_KM_PI= linP_R290_PI65, name= str('R290_PI65'))

plot_LR_R410A_PI_3 = plot_LR_KM_PI(P_KM_PI=P_R410A_PI3, LR_KM_PI= linP_R410A_PI3, name= str('R410A_PI3'))

plot_LR_R410A_PI_35 = plot_LR_KM_PI(P_KM_PI=P_R410A_PI35, LR_KM_PI= linP_R410A_PI35, name= str('R410A_PI35'))

plot_LR_R410A_PI_4 = plot_LR_KM_PI(P_KM_PI=P_R410A_PI4, LR_KM_PI= linP_R410A_PI4, name= str('R410A_PI4'))

plot_LR_R410A_PI_45 = plot_LR_KM_PI(P_KM_PI=P_R410A_PI45, LR_KM_PI= linP_R410A_PI45, name= str('R410A_PI45'))
plot_LR_R410A_PI_5 = plot_LR_KM_PI(P_KM_PI=P_R410A_PI5, LR_KM_PI= linP_R410A_PI5, name= str('R410A_PI5'))
plot_LR_R410A_PI_55 = plot_LR_KM_PI(P_KM_PI=P_R410A_PI55, LR_KM_PI= linP_R410A_PI55, name= str('R410A_PI55'))
plot_LR_R410A_PI_6 = plot_LR_KM_PI(P_KM_PI=P_R410A_PI6, LR_KM_PI= linP_R410A_PI6, name= str('R410A_PI6'))
plot_LR_R410A_PI_65 = plot_LR_KM_PI(P_KM_PI=P_R410A_PI65, LR_KM_PI= linP_R410A_PI65, name= str('R410A_PI65'))

plot_LR_R454C_PI_35 = plot_LR_KM_PI(P_KM_PI=P_R454C_PI35, LR_KM_PI= linP_R454C_PI35, name= str('R454C_PI35'))
plot_LR_R454C_PI_45 = plot_LR_KM_PI(P_KM_PI=P_R454C_PI45, LR_KM_PI= linP_R454C_PI45, name= str('R454C_PI45'))
plot_LR_R454C_PI_5 = plot_LR_KM_PI(P_KM_PI=P_R454C_PI5, LR_KM_PI= linP_R454C_PI5, name= str('R454C_PI5'))
plot_LR_R454C_PI_55 = plot_LR_KM_PI(P_KM_PI=P_R454C_PI55, LR_KM_PI= linP_R454C_PI55, name= str('R454C_PI55'))
plot_LR_R454C_PI_6 = plot_LR_KM_PI(P_KM_PI=P_R454C_PI6, LR_KM_PI= linP_R454C_PI6, name= str('R454C_PI6'))
plot_LR_R454C_PI_65 = plot_LR_KM_PI(P_KM_PI=P_R454C_PI65, LR_KM_PI= linP_R454C_PI65, name= str('R454C_PI65'))



from Plot.Plot_Regression import plot_LR_R32_PI
from Plot.Plot_Regression import plot_LR_R290_PI
from Plot.Plot_Regression import plot_LR_R410A_PI
from Plot.Plot_Regression import plot_LR_R454C_PI
from Plot.Plot_Loss_KM import Plot_eta

plot_LR_R32_PI(P_R32_PI25,linP_R32_PI25,P_R32_PI3,linP_R32_PI3,P_R32_PI35,linP_R32_PI35,P_R32_PI4,linP_R32_PI4
               ,P_R32_PI45,linP_R32_PI45)

plot_LR_R290_PI(P_R290_PI25,linP_R290_PI25, P_R290_PI3,linP_R290_PI3,linP_R290_PI35,P_R290_PI35,P_R290_PI4,
                linP_R290_PI4,P_R290_PI45,linP_R290_PI45,P_R290_PI5,linP_R290_PI5,P_R290_PI55,linP_R290_PI55,
                P_R290_PI6,linP_R290_PI6,linP_R290_PI65,P_R290_PI65)
plot_LR_R410A_PI(P_R410A_PI3,linP_R410A_PI3,P_R410A_PI35,linP_R410A_PI35,P_R410A_PI4,linP_R410A_PI4,P_R410A_PI45,
                 linP_R410A_PI45,P_R410A_PI5,linP_R410A_PI5,linP_R410A_PI55,P_R410A_PI55,P_R410A_PI6,linP_R410A_PI6,
                 P_R410A_PI65,linP_R410A_PI65)
plot_LR_R454C_PI(P_R454C_PI35,linP_R454C_PI35,P_R454C_PI45,linP_R454C_PI45,P_R454C_PI5,linP_R454C_PI5,P_R454C_PI55,
                 linP_R454C_PI55,P_R454C_PI6,linP_R454C_PI6,P_R454C_PI65,linP_R454C_PI65)





Plot_eta(P_R32, P_R290,P_R410A, P_R454C)