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
R32_PI3_Df =  clean_R32_PI3_DF()
R32_PI35_Df = clean_R32_PI35_DF()
R32_PI4_Df = clean_R32_PI4_DF()
R32_PI45_Df = clean_R32_PI45_DF()

P_R32_PI25 = P_R32_Pi25(R32_PI25_Df)
P_R32_PI3 = P_R32_Pi3(R32_PI3_Df)
P_R32_PI35 = P_R32_Pi35(R32_PI35_Df)
P_R32_PI4 = P_R32_Pi4(R32_PI4_Df)
P_R32_PI45 = P_R32_Pi45(R32_PI45_Df)
#print(R32_PI45_Df)

#print(P_R32_PI45, ' Das ist P_R32')



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
R290_PI3_Df = clean_R290_PI3_DF()
R290_PI35_Df = clean_R290_PI35_DF()
R290_PI4_Df = clean_R290_PI4_DF()
R290_PI45_Df = clean_R290_PI45_DF()
R290_PI5_Df = clean_R290_PI5_DF()
R290_PI55_Df = clean_R290_PI55_DF()
R290_PI6_Df = clean_R290_PI6_DF()
R290_PI65_Df = clean_R290_PI65_DF()


P_R290_PI25 = P_R290_Pi25(R290_PI25_Df)
P_R290_PI3 = P_R290_Pi3(R290_PI3_Df)
P_R290_PI35 = P_R290_Pi35(R290_PI35_Df)
P_R290_PI4 = P_R290_Pi4(R290_PI4_Df)
P_R290_PI45 = P_R290_Pi45(R290_PI45_Df)
P_R290_PI5 = P_R290_Pi5(R290_PI5_Df)
P_R290_PI55 = P_R290_Pi55(R290_PI55_Df)
P_R290_PI6 = P_R290_Pi6(R290_PI6_Df)
P_R290_PI65 = P_R290_Pi65(R290_PI65_Df)


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
R410A_PI35_Df = clean_R410A_PI35_DF()
R410A_PI4_Df = clean_R410A_PI4_DF()
R410A_PI42_Df = clean_R410A_PI42_DF()
R410A_PI45_Df = clean_R410A_PI45_DF()
R410A_PI5_Df = clean_R410A_PI5_DF()
R410A_PI55_Df = clean_R410A_PI55_DF()
R410A_PI6_Df = clean_R410A_PI6_DF()
R410A_PI65_Df = clean_R410A_PI65_DF()

R410A_PI4_Df = R410A_PI4_Df.append(R410A_PI42_Df, ignore_index= True)

P_R410A_PI3 = P_R410A_Pi3(R410A_PI3_Df)
P_R410A_PI35 = P_R410A_Pi35(R410A_PI35_Df)
P_R410A_PI4 = P_R410A_Pi4(R410A_PI4_Df)
P_R410A_PI45 = P_R410A_Pi45(R410A_PI45_Df)
P_R410A_PI5 = P_R410A_Pi5(R410A_PI5_Df)
P_R410A_PI55 = P_R410A_Pi55(R410A_PI55_Df)
P_R410A_PI6 = P_R410A_Pi6(R410A_PI6_Df)
P_R410A_PI65 = P_R410A_Pi65(R410A_PI65_Df)


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
R454C_PI45_Df = clean_R454C_PI45_DF()
R454C_PI5_Df = clean_R454C_PI5_DF()
R454C_PI55_Df = clean_R454C_PI55_DF()
R454C_PI6_Df = clean_R454C_PI6_DF()
R454C_PI65_Df = clean_R454C_PI65_DF()



P_R454C_PI35 = P_R454C_Pi35(R454C_PI35_Df)
P_R454C_PI45 = P_R454C_Pi45(R454C_PI45_Df)
P_R454C_PI5 = P_R454C_Pi5(R454C_PI5_Df)
P_R454C_PI55 = P_R454C_Pi55(R454C_PI55_Df)
P_R454C_PI6 = P_R454C_Pi6(R454C_PI6_Df)
P_R454C_PI65 = P_R454C_Pi65(R454C_PI65_Df)

PI3= [P_R32_PI3, P_R290_PI3, P_R410A_PI3]
PI35 = [P_R32_PI35, P_R290_PI35, P_R410A_PI35, P_R454C_PI35]
PI4 = [P_R290_PI4, ]
PI45 = [P_R290_PI45, P_R410A_PI45, P_R454C_PI45]
PI5 = [P_R290_PI5, P_R410A_PI5, P_R454C_PI5]
PI55 = [P_R290_PI55, P_R410A_PI55, P_R454C_PI55]
PI6 = [P_R290_PI6, P_R410A_PI6, P_R454C_PI6]
PI65 = [P_R410A_PI65, P_R454C_PI65]

print(P_R32_PI35, 'Ist wichtig')

full_R32 = pd.DataFrame()



temp_R32= pd.DataFrame()
full_PI35 = pd.DataFrame()
temp_R32['P_loss'] = P_R32_PI35['P_loss']
temp_R32['P1_Process'] = P_R32_PI35['P1_Process']
temp_R32['delta_s'] = P_R32_PI35['delta_s']
temp_R32['KM']= 1
temp_R32['PI'] = 3.5
full_PI35 = full_PI35.append(temp_R32, ignore_index= True)
full_R32 = full_R32.append(temp_R32, ignore_index= True)
print(len(temp_R32))



temp_R32['P_loss'] = P_R32_PI3['P_loss']
temp_R32['P1_Process'] = P_R32_PI3['P1_Process']
temp_R32['delta_s'] = P_R32_PI3['delta_s']
temp_R32['PI'] = 3
temp_R32['KM']= 1
print(len(temp_R32))
full_R32 = full_R32.append(temp_R32, ignore_index= True)

temp_R32['P_loss'] = P_R32_PI4['P_loss']
temp_R32['P1_Process'] = P_R32_PI4['P1_Process']
temp_R32['delta_s'] = P_R32_PI4['delta_s']
temp_R32['KM']= 1
temp_R32['PI'] = 4
print(len(temp_R32))
full_R32 = full_R32.append(temp_R32, ignore_index= True)

temp_R32['P_loss'] = P_R32_PI45['P_loss']
temp_R32['P1_Process'] = P_R32_PI45['P1_Process']
temp_R32['delta_s'] = P_R32_PI45['delta_s']
temp_R32['PI'] = 4.5
temp_R32['KM']= 1
print(len(temp_R32))


full_R32 = full_R32.append(temp_R32, ignore_index= True)

temp_R32['P_loss'] = P_R32_PI25['P_loss']
temp_R32['P1_Process'] = P_R32_PI25['P1_Process']
temp_R32['delta_s'] = P_R32_PI25['delta_s']
temp_R32['KM']= 1
temp_R32['PI'] = 2.5

full_R32 = full_R32.append(temp_R32, ignore_index= True)

print(len(full_R32), ' Das ist full R32')
full_R32.to_excel('Full_R32.xlsx')



full_R290 = pd.DataFrame()






temp_R290= pd.DataFrame()

temp_R290['P_loss'] = P_R290_PI3['P_loss']
temp_R290['P1_Process'] = P_R290_PI3['P1_Process']
temp_R290['delta_s'] = P_R290_PI3['delta_s']
temp_R290['KM']= 2
temp_R290['PI'] = 3
full_R290 = full_R290.append(temp_R290, ignore_index= True)





temp_R290['P_loss'] = P_R290_PI35['P_loss']
temp_R290['P1_Process'] = P_R290_PI35['P1_Process']
temp_R290['delta_s'] = P_R290_PI35['delta_s']
temp_R290['KM']= 2
temp_R290['PI'] = 3.5
full_PI35 = full_PI35.append(temp_R290, ignore_index= True)
full_R290 = full_R290.append(temp_R290, ignore_index= True)

temp_R290['P_loss'] = P_R290_PI4['P_loss']
temp_R290['P1_Process'] = P_R290_PI4['P1_Process']
temp_R290['delta_s'] = P_R290_PI4['delta_s']
temp_R290['KM']= 2
temp_R290['PI'] = 4
full_R290 = full_R290.append(temp_R290, ignore_index= True)


temp_R290['P_loss'] = P_R290_PI45['P_loss']
temp_R290['P1_Process'] = P_R290_PI45['P1_Process']
temp_R290['delta_s'] = P_R290_PI45['delta_s']
temp_R290['KM']= 2
temp_R290['PI'] = 4.5
full_R290 = full_R290.append(temp_R290, ignore_index= True)

temp_R290['P_loss'] = P_R290_PI5['P_loss']
temp_R290['P1_Process'] = P_R290_PI5['P1_Process']
temp_R290['delta_s'] = P_R290_PI5['delta_s']
temp_R290['KM']= 2
temp_R290['PI'] = 5
full_R290 = full_R290.append(temp_R290, ignore_index= True)

temp_R290['P_loss'] = P_R290_PI55['P_loss']
temp_R290['P1_Process'] = P_R290_PI55['P1_Process']
temp_R290['delta_s'] = P_R290_PI55['delta_s']
temp_R290['KM']= 2
temp_R290['PI'] = 5.5
full_R290 = full_R290.append(temp_R290, ignore_index= True)

temp_R290['P_loss'] = P_R290_PI6['P_loss']
temp_R290['P1_Process'] = P_R290_PI6['P1_Process']
temp_R290['delta_s'] = P_R290_PI6['delta_s']
temp_R290['KM']= 2
temp_R290['PI'] = 6
full_R290 = full_R290.append(temp_R290, ignore_index= True)

temp_R290['P_loss'] = P_R290_PI65['P_loss']
temp_R290['P1_Process'] = P_R290_PI65['P1_Process']
temp_R290['delta_s'] = P_R290_PI65['delta_s']
temp_R290['PI'] = 6.5
temp_R290['KM']= 2
full_R290 = full_R290.append(temp_R290, ignore_index= True)






temp_R410A= pd.DataFrame()
full_R410A = pd.DataFrame()
temp_R410A['P_loss'] = P_R410A_PI3['P_loss']
temp_R410A['P1_Process'] = P_R410A_PI3['P1_Process']
temp_R410A['delta_s'] = P_R410A_PI3['delta_s']
temp_R410A['KM']= 3
temp_R410A['PI'] = 3
full_R410A = full_R410A.append(temp_R410A, ignore_index= True)


temp_R410A['P_loss'] = P_R410A_PI35['P_loss']
temp_R410A['P1_Process'] = P_R410A_PI35['P1_Process']
temp_R410A['delta_s'] = P_R410A_PI35['delta_s']
temp_R410A['KM']= 3
temp_R410A['PI'] = 3.5
full_PI35 = full_PI35.append(temp_R410A, ignore_index= True)
full_R410A = full_R410A.append(temp_R410A, ignore_index= True)

temp_R410A['P_loss'] = P_R410A_PI4['P_loss']
temp_R410A['P1_Process'] = P_R410A_PI4['P1_Process']
temp_R410A['delta_s'] = P_R410A_PI4['delta_s']
temp_R410A['KM']= 3
temp_R410A['PI'] = 4
full_R410A = full_R410A.append(temp_R410A, ignore_index= True)

temp_R410A['P_loss'] = P_R410A_PI45['P_loss']
temp_R410A['P1_Process'] = P_R410A_PI45['P1_Process']
temp_R410A['delta_s'] = P_R410A_PI45['delta_s']
temp_R410A['KM']= 3
temp_R410A['PI'] = 4.5
full_R410A = full_R410A.append(temp_R410A, ignore_index= True)

temp_R410A['P_loss'] = P_R410A_PI5['P_loss']
temp_R410A['P1_Process'] = P_R410A_PI5['P1_Process']
temp_R410A['delta_s'] = P_R410A_PI5['delta_s']
temp_R410A['KM']= 3
temp_R410A['PI'] = 5
full_R410A = full_R410A.append(temp_R410A, ignore_index= True)

temp_R410A['P_loss'] = P_R410A_PI55['P_loss']
temp_R410A['P1_Process'] = P_R410A_PI55['P1_Process']
temp_R410A['KM']= 3
temp_R410A['PI'] = 5.5
full_R410A = full_R410A.append(temp_R410A, ignore_index= True)

temp_R410A['P_loss'] = P_R410A_PI6['P_loss']
temp_R410A['P1_Process'] = P_R410A_PI6['P1_Process']
temp_R410A['delta_s'] = P_R410A_PI6['delta_s']
temp_R410A['KM']= 3
temp_R410A['PI'] = 6
full_R410A = full_R410A.append(temp_R410A, ignore_index= True)

temp_R410A['P_loss'] = P_R410A_PI65['P_loss']
temp_R410A['P1_Process'] = P_R410A_PI65['P1_Process']
temp_R410A['delta_s'] = P_R410A_PI65['delta_s']
temp_R410A['KM']= 3
temp_R410A['PI'] = 6.5
full_R410A = full_R410A.append(temp_R410A, ignore_index= True)


temp_R454C= pd.DataFrame()
full_R454C = pd.DataFrame()



temp_R454C['P_loss'] = P_R454C_PI35['P_loss']
temp_R454C['P1_Process'] = P_R454C_PI35['P1_Process']
temp_R454C['delta_s'] = P_R454C_PI35['delta_s']
temp_R454C['KM']= 4
temp_R454C['PI']= 3.5
full_PI35 = full_PI35.append(temp_R454C, ignore_index= True)
full_R454C = full_R454C.append(temp_R454C, ignore_index= True)



temp_R454C['P_loss'] = P_R454C_PI45['P_loss']
temp_R454C['P1_Process'] = P_R454C_PI45['P1_Process']
temp_R454C['delta_s'] = P_R454C_PI45['delta_s']
temp_R454C['KM']= 4
temp_R454C['PI']= 4.5
full_R454C = full_R454C.append(temp_R454C, ignore_index= True)

temp_R454C['P_loss'] = P_R454C_PI5['P_loss']
temp_R454C['P1_Process'] = P_R454C_PI5['P1_Process']
temp_R454C['delta_s'] = P_R454C_PI5['delta_s']
temp_R454C['KM']= 4
temp_R454C['PI']= 5
full_R454C = full_R454C.append(temp_R454C, ignore_index= True)

temp_R454C['P_loss'] = P_R454C_PI55['P_loss']
temp_R454C['P1_Process'] = P_R454C_PI55['P1_Process']
temp_R454C['delta_s'] = P_R454C_PI55['delta_s']
temp_R454C['KM']= 4
temp_R454C['PI']= 5.5
full_R454C = full_R454C.append(temp_R454C, ignore_index= True)

temp_R454C['P_loss'] = P_R454C_PI6['P_loss']
temp_R454C['P1_Process'] = P_R454C_PI6['P1_Process']
temp_R454C['delta_s'] = P_R454C_PI6['delta_s']
temp_R454C['KM']= 4
temp_R454C['PI']= 6
full_R454C = full_R454C.append(temp_R454C, ignore_index= True)

temp_R454C['P_loss'] = P_R454C_PI65['P_loss']
temp_R454C['P1_Process'] = P_R454C_PI65['P1_Process']
temp_R454C['delta_s'] = P_R454C_PI65['delta_s']
temp_R454C['KM']= 4
temp_R454C['PI']= 6.5
full_R454C = full_R454C.append(temp_R454C, ignore_index= True)

full = pd.DataFrame()

full = full.append(full_R32 , ignore_index= True)
print(len(full),'Das ist Full nach R32')
full = full.append(full_R290 , ignore_index= True)
print(len(full),'Das ist Full nach R290')
full = full.append(full_R410A , ignore_index= True)
print(len(full),'Das ist Full nach R410A')
full = full.append(full_R454C , ignore_index= True)
print(len(full),'Das ist Full nach R454C')
full=full.dropna().reset_index(drop=True)

full = sklearn.utils.shuffle(full)
full.to_excel('Full.xlsx')
Xtemp = pd.DataFrame() #Xen soll X_Test und X_Train zusammenstellen.
Ytemp = pd.DataFrame()
Xtemp['P_loss'] = full['P_loss']
Xtemp['P1_Process'] = full['P1_Process']
Ytemp['KM'] = full['KM']




X = Xtemp
Y = Ytemp
#X_Train_PI35, X_Test_PI35 ,Y_Train_PI35,Y_Test_PI35 = X_PI35[:9000], X_PI35[9000:], Y_PI35[:9000], Y_PI35[9000:]

#X_Train, X_Test,Y_Train,Y_Test = X[:40000], X[40000:], Y[:40000], Y[40000:]

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)

print(len(X), 'Das sit die lange von x')
def Plot_Ploss_PI35(temp_R32, temp_R290, temp_R410A, temp_R454C):
    fig, ax = plt.subplots(1,1,figsize=(13, 8), layout='constrained',sharey=True )
    #Festlegen der Achsenbeschriftung
    font1 = {'family':'serif','color':'black','size':15}
    font2 = {'family':'serif','color':'black','size':10}
    plt.title('Verlustleistung über den Eingangsdruck bei PI: 3.5 ' , fontdict= font1)
    plt.xlabel('P1_Process [bar]', fontdict= font2)
    plt.ylabel('Verlustleistung [kW]', fontdict=font2)
    plt.grid(color = 'black', linestyle= '--', linewidth = 0.5)

    plt.scatter(temp_R32['P_loss'], temp_R32['P1_Process'], label='R32', color = 'magenta')
    plt.scatter(temp_R290['P_loss'], temp_R290['P1_Process'], label='R290', color='blue')
    plt.scatter(temp_R410A['P_loss'], temp_R410A['P1_Process'], label='R410A', color='green')
    plt.scatter(temp_R454C['P_loss'], temp_R454C['P1_Process'], label='R454C', color='red')
    plt.legend()
    plt.show()
print(full_R32)
def Plot_ds_R32(full_R32, full_R290, full_R410A, full_R454C):
    fig, ax = plt.subplots(1,1,figsize=(13, 8), layout='constrained',sharey=True )
    #Festlegen der Achsenbeschriftung
    font1 = {'family':'serif','color':'black','size':15}
    font2 = {'family':'serif','color':'black','size':10}
    plt.title('Entropiedifferenz abhängig vom Druckverhältnisse ' , fontdict= font1)
    plt.xlabel('ds (s2-s1)', fontdict= font2)
    plt.ylabel('PI', fontdict=font2)
    plt.grid(color = 'black', linestyle= '--', linewidth = 0.5)

    plt.scatter(full_R32['delta_s'], full_R32['PI'], label='R32', color = 'magenta')
    plt.scatter(full_R290['delta_s'], full_R290['PI'], label='R290', color='blue')
    plt.scatter(full_R410A['delta_s'], full_R410A['PI'], label='R410A', color='green')
    plt.scatter(full_R454C['delta_s'], full_R454C['PI'], label='R454C', color='orange')
    plt.legend()
    plt.show()
Plot_ds_R32(full_R32,full_R290, full_R410A,full_R454C)
#Plot_Ploss_PI35(temp_R32, temp_R290, temp_R410A, temp_R454C)

feature_cols = ['P_loss', 'P1_Process']
class_names = ['1','2','3','4']
'''
# Create Decision Tree classifer object
clf = DecisionTreeClassifier(max_depth= 20, random_state=0)

# Train Decision Tree Classifer
clf = clf.fit(X_Train,Y_Train)

#Predict the response for test dataset
y_pred = clf.predict(X_Test)
print("Accuracy:",metrics.accuracy_score(Y_Test, y_pred))
tree.plot_tree(clf)
fig = plt.figure(figsize=(500,500))
_ = tree.plot_tree(clf,
                   feature_names=feature_cols,
                   class_names=class_names,
                   filled=True)
fig.savefig("decistion_tree.png")
'''



'''

import statsmodels.api as sm



# create a multiple regression model
model = sm.OLS(y_train, X_train).fit()

# print the model summary
print(model.summary())

y_pred = model.predict(X_test)
print(y_pred)'''

print('Process finesh')