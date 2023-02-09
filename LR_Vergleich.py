#Modul Importe
from pathlib import Path
import openpyxl
import pandas as pd
import numpy as np
import warnings
import os
import glob
import matplotlib.pyplot as plt


# Get Data from excel File
dataFolder = Path(__file__).resolve().parent # Absoluter Pfad zum Ordner dieser Datei, findet ihn automatisch heraus
import sys; sys.path.append(str(dataFolder.parent)) # Füge Ordner zur Laufzeitumgebung damit die selbst erstellte Module gefunden werden

from Plot.Plot_LR import plot_Tan_KM_3
from Plot.Plot_LR import plot_Tan_KM_35
from Plot.Plot_LR import plot_Tan_KM_4
from Plot.Plot_LR import plot_Tan_KM_45
from Plot.Plot_LR import plot_Tan_KM_5
from Plot.Plot_LR import plot_Tan_KM_55
from Plot.Plot_LR import plot_Tan_KM_6
#from Plot.Plot_LR import plot_Tan_KM_65

print(os.listdir(dataFolder))


LR_R32_Data_raw = dataFolder/  'Calculation' /'Calculation_Data' / 'Nachbearbeitet'/'LR_R32_Data.xlsx'
LR_R32_Data_raw = pd.read_excel(LR_R32_Data_raw)

LR_R32_Data = LR_R32_Data_raw.iloc[0:3]

print(LR_R32_Data , 'LR_R32')

LR_R290_Data_raw = dataFolder/  'Calculation' /'Calculation_Data' / 'Nachbearbeitet'/'LR_R290_Data.xlsx'
LR_R290_Data_raw = pd.read_excel(LR_R290_Data_raw)


LR_R290_Data = LR_R290_Data_raw.iloc[1:8]

print(LR_R290_Data, 'LR_R290')





LR_R410A_Data_raw = dataFolder/  'Calculation' /'Calculation_Data' / 'Nachbearbeitet'/'LR_R410A_Data.xlsx'
LR_R410A_Data_raw = pd.read_excel(LR_R410A_Data_raw)

LR_R410A_Data = LR_R410A_Data_raw

print(LR_R410A_Data , 'LR_R410A')

LR_R454C_Data_raw = dataFolder/  'Calculation' /'Calculation_Data' / 'Nachbearbeitet'/'LR_R454C_Data.xlsx'
LR_R454C_Data_raw = pd.read_excel(LR_R454C_Data_raw)

LR_R454C_Data = LR_R454C_Data_raw

print(LR_R454C_Data , 'LR_R454C')


''' Tangentenberechnung'''

x_Achse = np.arange(0,20 )
#print(x_Achse)



LR_Data = pd.DataFrame()


#LR_R32_Data = LR_R32_Data.loc[0]




#print(LR_R32_Data)




def calc_Tangente_KM(LR_KM, x_Achse, i ):




    LR_KM = LR_KM.loc[i]
    #print(i)
    #print(LR_KM)
    tange= LR_KM['LIN'] + LR_KM['COE']*x_Achse
    #print(tange)
    return tange




Tan_R32 = pd.DataFrame()

Tan_R32['PI25']= calc_Tangente_KM(LR_KM=LR_R32_Data , x_Achse= x_Achse , i=0 )
Tan_R32['PI3']= calc_Tangente_KM(LR_KM=LR_R32_Data , x_Achse= x_Achse , i=1 )
Tan_R32['PI35']= calc_Tangente_KM(LR_KM=LR_R32_Data , x_Achse= x_Achse , i=2 )




fig, ax = plt.subplots(1, 1, figsize=(13, 8), layout='constrained', sharey=True)
    # Festlegen der Achsenbeschriftung
font1 = {'family': 'serif', 'color': 'black', 'size': 15}
font2 = {'family': 'serif', 'color': 'black', 'size': 10}
plt.title('Linear Regression von R32' , fontdict=font1)
plt.xlabel('P1', fontdict=font2)
plt.ylabel('Verlustleistung [W]', fontdict=font2)
plt.grid(color='black', linestyle='--', linewidth=0.5)
plt.plot(x_Achse, Tan_R32['PI25'],color = 'green' , label = 'PI 2.5')
plt.plot(x_Achse, Tan_R32['PI3'], color='lime' , label = 'PI 3')
plt.plot(x_Achse, Tan_R32['PI35'],color = 'aquamarine' , label = 'PI 3.5')

plt.legend()




Tan_R290 = pd.DataFrame()

Tan_R290['PI3']= calc_Tangente_KM(LR_KM=LR_R290_Data , x_Achse= x_Achse , i=1 )
Tan_R290['PI35']= calc_Tangente_KM(LR_KM=LR_R290_Data , x_Achse= x_Achse , i=2 )
Tan_R290['PI4']= calc_Tangente_KM(LR_KM=LR_R290_Data , x_Achse= x_Achse , i=3 )
Tan_R290['PI45']= calc_Tangente_KM(LR_KM=LR_R290_Data , x_Achse= x_Achse , i=4 )
Tan_R290['PI5']= calc_Tangente_KM(LR_KM=LR_R290_Data , x_Achse= x_Achse , i=5 )
Tan_R290['PI55']= calc_Tangente_KM(LR_KM=LR_R290_Data , x_Achse= x_Achse , i=6 )
Tan_R290['PI6']= calc_Tangente_KM(LR_KM=LR_R290_Data , x_Achse= x_Achse , i=7 )











fig, ax = plt.subplots(1, 1, figsize=(13, 8), layout='constrained', sharey=True)
    # Festlegen der Achsenbeschriftung
font1 = {'family': 'serif', 'color': 'black', 'size': 15}
font2 = {'family': 'serif', 'color': 'black', 'size': 10}
plt.title('Linear Regression von R290' , fontdict=font1)
plt.xlabel('P1', fontdict=font2)
plt.ylabel('Verlustleistung [W]', fontdict=font2)
plt.grid(color='black', linestyle='--', linewidth=0.5)

plt.plot(x_Achse, Tan_R290['PI3'], color='lime' , label = 'PI 3')
plt.plot(x_Achse, Tan_R290['PI35'],color = 'aquamarine' , label = 'PI 3.5')
plt.plot(x_Achse, Tan_R290['PI4'],color = 'aqua' , label = 'PI 4')
plt.plot(x_Achse, Tan_R290['PI45'],color = 'teal' , label = 'PI 4.5')
plt.plot(x_Achse, Tan_R290['PI5'],color = 'dodgerblue' , label = 'PI 5')
plt.plot(x_Achse, Tan_R290['PI55'],color = 'navy' , label = 'PI 5.5')
plt.plot(x_Achse, Tan_R290['PI6'],color = 'blueviolet' , label = 'PI 6')


plt.legend()



Tan_R410A = pd.DataFrame()


Tan_R410A['PI3']= calc_Tangente_KM(LR_KM=LR_R410A_Data , x_Achse= x_Achse , i=0 )
Tan_R410A['PI35']= calc_Tangente_KM(LR_KM=LR_R410A_Data , x_Achse= x_Achse , i=1 )
Tan_R410A['PI4']= calc_Tangente_KM(LR_KM=LR_R410A_Data , x_Achse= x_Achse , i=2 )
Tan_R410A['PI45']= calc_Tangente_KM(LR_KM=LR_R410A_Data , x_Achse= x_Achse , i=3 )
Tan_R410A['PI5']= calc_Tangente_KM(LR_KM=LR_R410A_Data , x_Achse= x_Achse , i=4 )
Tan_R410A['PI55']= calc_Tangente_KM(LR_KM=LR_R410A_Data , x_Achse= x_Achse , i=5 )
Tan_R410A['PI6']= calc_Tangente_KM(LR_KM=LR_R410A_Data , x_Achse= x_Achse , i=6 )
Tan_R410A['PI65']= calc_Tangente_KM(LR_KM=LR_R410A_Data , x_Achse= x_Achse , i=7 )







fig, ax = plt.subplots(1, 1, figsize=(13, 8), layout='constrained', sharey=True)
    # Festlegen der Achsenbeschriftung
font1 = {'family': 'serif', 'color': 'black', 'size': 15}
font2 = {'family': 'serif', 'color': 'black', 'size': 10}
plt.title('Linear Regression von R410A' , fontdict=font1)
plt.xlabel('P1', fontdict=font2)
plt.ylabel('Verlustleistung [W]', fontdict=font2)
plt.grid(color='black', linestyle='--', linewidth=0.5)

plt.plot(x_Achse, Tan_R410A['PI3'], color='lime' , label = 'PI 3')
plt.plot(x_Achse, Tan_R410A['PI35'],color = 'aquamarine' , label = 'PI 3.5')
plt.plot(x_Achse, Tan_R410A['PI4'],color = 'aqua' , label = 'PI 4')
plt.plot(x_Achse, Tan_R410A['PI45'],color = 'teal' , label = 'PI 4.5')
plt.plot(x_Achse, Tan_R410A['PI5'],color = 'dodgerblue' , label = 'PI 5')
plt.plot(x_Achse, Tan_R410A['PI55'],color = 'navy' , label = 'PI 5.5')
plt.plot(x_Achse, Tan_R410A['PI6'],color = 'blueviolet' , label = 'PI 6')
plt.plot(x_Achse, Tan_R410A['PI65'],color = 'magenta' , label = 'PI 6')

plt.legend()




Tan_R454C = pd.DataFrame()



Tan_R454C['PI35']= calc_Tangente_KM(LR_KM=LR_R454C_Data , x_Achse= x_Achse , i=0 )

Tan_R454C['PI45']= calc_Tangente_KM(LR_KM=LR_R454C_Data , x_Achse= x_Achse , i=1 )
Tan_R454C['PI5']= calc_Tangente_KM(LR_KM=LR_R454C_Data , x_Achse= x_Achse , i=2)
Tan_R454C['PI55']= calc_Tangente_KM(LR_KM=LR_R454C_Data , x_Achse= x_Achse , i=3 )
Tan_R454C['PI6']= calc_Tangente_KM(LR_KM=LR_R454C_Data , x_Achse= x_Achse , i=4 )
Tan_R454C['PI65']= calc_Tangente_KM(LR_KM=LR_R454C_Data , x_Achse= x_Achse , i=5 )


fig, ax = plt.subplots(1, 1, figsize=(13, 8), layout='constrained', sharey=True)
    # Festlegen der Achsenbeschriftung
font1 = {'family': 'serif', 'color': 'black', 'size': 15}
font2 = {'family': 'serif', 'color': 'black', 'size': 10}
plt.title('Linear Regression von R454C' , fontdict=font1)
plt.xlabel('P1', fontdict=font2)
plt.ylabel('Verlustleistung [W]', fontdict=font2)
plt.grid(color='black', linestyle='--', linewidth=0.5)


plt.plot(x_Achse, Tan_R454C['PI35'],color = 'aquamarine' , label = 'PI 3.5')

plt.plot(x_Achse, Tan_R454C['PI45'],color = 'teal' , label = 'PI 4.5')
plt.plot(x_Achse, Tan_R454C['PI5'],color = 'dodgerblue' , label = 'PI 5')
plt.plot(x_Achse, Tan_R454C['PI55'],color = 'navy' , label = 'PI 5.5')
plt.plot(x_Achse, Tan_R454C['PI6'],color = 'blueviolet' , label = 'PI 6')
plt.plot(x_Achse, Tan_R454C['PI65'],color = 'magenta' , label = 'PI 6.5')

plt.legend()




plot_Tan_KM_3(Tan_R32= Tan_R32['PI3'] , Tan_R290=Tan_R290['PI3'] , Tan_R410A=Tan_R410A['PI3'],  x_Achse= x_Achse)
plot_Tan_KM_35(Tan_R32= Tan_R32['PI35'] , Tan_R290=Tan_R290['PI35'] , Tan_R410A=Tan_R410A['PI35'],Tan_R454C=Tan_R454C['PI35'],  x_Achse= x_Achse)
plot_Tan_KM_4( Tan_R290=Tan_R290['PI4'] , Tan_R410A=Tan_R410A['PI4'],  x_Achse= x_Achse)
plot_Tan_KM_45( Tan_R290=Tan_R290['PI45'] , Tan_R410A=Tan_R410A['PI45'],Tan_R454C=Tan_R454C['PI45'],  x_Achse= x_Achse)
plot_Tan_KM_5( Tan_R290=Tan_R290['PI5'] , Tan_R410A=Tan_R410A['PI5'],Tan_R454C=Tan_R454C['PI5'],  x_Achse= x_Achse)
plot_Tan_KM_55( Tan_R290=Tan_R290['PI55'] , Tan_R410A=Tan_R410A['PI55'],Tan_R454C=Tan_R454C['PI55'],  x_Achse= x_Achse)
plot_Tan_KM_6( Tan_R290=Tan_R290['PI6'] , Tan_R410A=Tan_R410A['PI6'],Tan_R454C=Tan_R454C['PI6'],  x_Achse= x_Achse)
#plot_Tan_KM_65( Tan_R410A=Tan_R410A['PI65'],Tan_R454C=Tan_R454C['PI65'],  x_Achse= x_Achse)


''' Erstellt für jedes Druckverhältnis die Funktion'''
'''
Tan_PI3 = pd.DataFrame()
Tan_PI3['R32'] = Tan_R32['PI3']
Tan_PI3['R290'] = Tan_R290['PI3']
Tan_PI3['R410A'] = Tan_R410A['PI3']
Tan_PI3['R454C'] = 0

Tan_PI35 = pd.DataFrame()
Tan_PI35['R32'] = Tan_R32['PI35']
Tan_PI35['R290'] = Tan_R290['PI35']
Tan_PI35['R410A'] = Tan_R410A['PI35']
Tan_PI35['R454C'] = Tan_R454C['PI35']

Tan_PI4 = pd.DataFrame()
Tan_PI4['R32'] = 0
Tan_PI4['R290'] = Tan_R290['PI4']
Tan_PI4['R410A'] = Tan_R410A['PI4']
Tan_PI4['R454C'] = 0

Tan_PI45 = pd.DataFrame()
Tan_PI45['R32'] = 0

Tan_PI45['R290'] = Tan_R290['PI45']
Tan_PI45['R410A'] = Tan_R410A['PI45']
Tan_PI45['R454C'] = Tan_R454C['PI45']

Tan_PI5 = pd.DataFrame()
Tan_PI5['R32'] = 0
Tan_PI5['R290'] = Tan_R290['PI5']
Tan_PI5['R410A'] = Tan_R410A['PI5']
Tan_PI5['R454C'] = Tan_R454C['PI5']

Tan_PI55 = pd.DataFrame()
Tan_PI55['R32'] = 0
Tan_PI55['R290'] = Tan_R290['PI55']
Tan_PI55['R410A'] = Tan_R410A['PI55']
Tan_PI55['R454C'] = Tan_R454C['PI55']

Tan_PI6 = pd.DataFrame()
Tan_PI6['R32'] = 0
Tan_PI6['R290'] = Tan_R290['PI6']
Tan_PI6['R410A'] = Tan_R410A['PI6']
Tan_PI6['R454C'] = Tan_R454C['PI6']

Tan_PI65 = pd.DataFrame()
Tan_PI65['R32'] = 0
Tan_PI65['R290'] = 0
Tan_PI65['R410A'] = Tan_R410A['PI65']
Tan_PI65['R454C'] = Tan_R454C['PI65']
'''

LR_PI3 = pd.DataFrame()

LR_PI3['R32'] = LR_R32_Data.loc[1]
LR_PI3['R290'] = LR_R290_Data.loc[1]
LR_PI3['R410A']= LR_R410A_Data.loc[0]
LR_PI3['R454C'] = 0


LR_PI35 = pd.DataFrame()

LR_PI35['R32'] = LR_R32_Data.loc[2]
LR_PI35['R290'] = LR_R290_Data.loc[2]
LR_PI35['R410A']= LR_R410A_Data.loc[1]
LR_PI35['R454C'] = LR_R454C_Data.loc[0]

LR_PI4 = pd.DataFrame()

LR_PI4['R32'] = 0
LR_PI4['R290'] = LR_R290_Data.loc[3]
LR_PI4['R410A']= LR_R410A_Data.loc[2]
LR_PI4['R454C'] = 0

LR_PI45 = pd.DataFrame()

LR_PI45['R32'] = 0
LR_PI45['R290'] = LR_R290_Data.loc[4]
LR_PI45['R410A']= LR_R410A_Data.loc[3]
LR_PI45['R454C'] = LR_R454C_Data.loc[1]

LR_PI5 = pd.DataFrame()

LR_PI5['R32'] = 0

LR_PI5['R290'] = LR_R290_Data.loc[5]
LR_PI5['R410A']= LR_R410A_Data.loc[4]
LR_PI5['R454C'] = LR_R454C_Data.loc[2]

LR_PI55 = pd.DataFrame()

LR_PI55['R32'] = 0
LR_PI55['R290'] = LR_R290_Data.loc[6]
LR_PI55['R410A']= LR_R410A_Data.loc[5]
LR_PI55['R454C'] = LR_R454C_Data.loc[3]

LR_PI6 = pd.DataFrame()

LR_PI6['R32'] = int(0)
LR_PI6['R290'] = LR_R290_Data.loc[7]
LR_PI6['R410A']= LR_R410A_Data.loc[6]
LR_PI6['R454C'] = LR_R454C_Data.loc[5]



from Plot.Plot_LR import plot_COE_KM



x_290 = LR_R290_Data.iloc[:,[0]]
plot_COE_KM(LR_R290_Data['LIN'], x_Achse= x_290, KM= 'R290')

x_32 = LR_R32_Data.iloc[:,[0]]

plot_COE_KM(LR_R32_Data['LIN'], x_Achse= x_32, KM= 'R32')

x_410A = LR_R410A_Data.iloc[:,[0]]
plot_COE_KM(LR_R410A_Data['LIN'], x_Achse= x_410A, KM= 'R410A')

x_454C = LR_R454C_Data.iloc[:,[0]]
plot_COE_KM(LR_R454C_Data['LIN'], x_Achse= x_454C, KM= 'R454C')

from sklearn.preprocessing import PolynomialFeatures

print(LR_R410A_Data,'Das ist LR410A')


mona = pd.DataFrame()



temp_R32 = pd.DataFrame()
temp_R32 = LR_R32_Data[['COE', 'LIN', 'PI']]
temp_R32['KM'] = 1
mona = mona.append(temp_R32, ignore_index=True)

temp_R290 = pd.DataFrame()
temp_R290 = LR_R290_Data[['COE', 'LIN', 'PI']]
temp_R290['KM'] = 2
mona = mona.append(temp_R290, ignore_index=True)
temp_R410A = pd.DataFrame()
temp_R410A = LR_R410A_Data[['COE', 'LIN', 'PI']]
temp_R410A['KM'] = 3
mona = mona.append(temp_R410A, ignore_index=True)
temp_R454C = pd.DataFrame()
temp_R454C = LR_R454C_Data[['COE', 'LIN', 'PI']]
temp_R454C['KM'] = 4
mona = mona.append(temp_R454C, ignore_index=True)



print(mona)


from sklearn.metrics import mean_squared_error
from sklearn.neural_network import MLPRegressor

Xtemp = pd.DataFrame() #Xen soll X_Test und X_Train zusammenstellen.
Ytemp = pd.DataFrame()

Xtemp['COE'] = mona['COE']
Xtemp['LIN'] = mona['LIN']
Ytemp['KM'] = mona['KM']
Ytemp['PI'] = mona['PI']





#X_Train, X_Test,Y_Train,Y_Test = X_PI35[:9000], X_PI35[9000:], Y_PI35[:9000], Y_PI35[9000:]


# Modell erstellen und trainieren
model = MLPRegressor(hidden_layer_sizes=(50,50), max_iter=1000)
model.fit(Xtemp, Ytemp)

# Vorhersagen machen und den Root Mean Squared Error berechnen
y_pred = model.predict(Xtemp)
rmse = np.sqrt(mean_squared_error(Ytemp, y_pred))
print("RMSE: ", rmse)


import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Beispieldaten generieren
import numpy as np
np.random.seed(1)

# 3D-Scatter-Plot erstellen
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(LR_R32_Data['COE'], LR_R32_Data['LIN'], temp_R32['PI'] , color = 'green',label = 'R32')
ax.scatter(LR_R290_Data['COE'], LR_R290_Data['LIN'], temp_R290['PI'] , color = 'blue',label = 'R290')
ax.scatter(LR_R410A_Data['COE'], LR_R410A_Data['LIN'], temp_R410A['PI'] , color = 'red',label = 'R410A')
ax.scatter(LR_R454C_Data['COE'], LR_R454C_Data['LIN'], temp_R454C['PI'] , color = 'magenta',label = 'R454C')
ax.set_xlabel('COE')
ax.set_ylabel('LIN')
ax.set_zlabel('PI')
plt.legend()
plt.show()


fig, ax = plt.subplots(1,1,figsize=(13, 8), layout='constrained',sharey=True )
#Festlegen der Achsenbeschriftung
font1 = {'family':'serif','color':'black','size':15}
font2 = {'family':'serif','color':'black','size':10}
plt.title('Steigung über PI ' , fontdict= font1)
plt.xlabel('PI', fontdict= font2)
plt.ylabel('COE', fontdict=font2)
plt.grid(color = 'black', linestyle= '--', linewidth = 0.5)
plt.plot( temp_R32['PI'],LR_R32_Data['COE'], label='R32', color = 'magenta')
plt.plot(temp_R290['PI'],LR_R290_Data['COE'], label='R290', color='blue')
plt.plot(temp_R410A['PI'],LR_R410A_Data['COE'],  label='R410A', color='green')
plt.plot( temp_R454C['PI'],LR_R454C_Data['COE'], label='R454C', color='red')
plt.legend()
plt.show()
