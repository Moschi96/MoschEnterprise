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



P_R32_list = [P_R32_PI25,P_R32_PI3, P_R32_PI35,P_R32_PI4, P_R32_PI45 ]
P_R32 = pd.concat(P_R32_list)
P_R32['KM'] = 1
P_R32['PI_Process'] = P_R32['P2_Process']/P_R32['P1_Process']


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
R290_PI3_Df = clean_R290_PI3_DF()
R290_PI35_Df = clean_R290_PI35_DF()
R290_PI4_Df = clean_R290_PI4_DF()
R290_PI45_Df = clean_R290_PI45_DF()
R290_PI5_Df = clean_R290_PI5_DF()
R290_PI55_Df = clean_R290_PI55_DF()
R290_PI6_Df = clean_R290_PI6_DF()
R290_PI65_Df = clean_R290_PI65_DF()


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

P_R290 = pd.concat(P_R290_list)
P_R290['KM'] = 2
P_R290['PI_Process'] = P_R290['P2_Process'] / P_R290['P1_Process']


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
P_R410A['PI_Process'] = P_R410A['P2_Process'] / P_R410A['P1_Process']



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
P_R454C['PI_Process'] = P_R454C['P2_Process'] / P_R454C['P1_Process']

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


print(full)
full = sklearn.utils.shuffle(full)
full.to_excel('Full.xlsx')
Xtemp = pd.DataFrame() #Xen soll X_Test und X_Train zusammenstellen.
Ytemp = pd.DataFrame()
Xtemp['P_loss'] = full['P_loss']
Xtemp['P1_Process'] = full['P1_Process']
Ytemp['KM'] = full['KM']




X = Xtemp
Y = Ytemp


X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)





def Plot_eta(temp_R32, temp_R290, temp_R410A, temp_R454C):
    fig, ax = plt.subplots(1,1,figsize=(13, 8), layout='constrained',sharey=True )
    #Festlegen der Achsenbeschriftung
    font1 = {'family':'serif','color':'black','size':15}
    font2 = {'family':'serif','color':'black','size':10}
    plt.title('Wirkunsgrad abhängig vom Druckverhältnis ' , fontdict= font1)
    plt.xlabel('PI_Process ]', fontdict= font2)
    plt.ylabel('Isentroper Wirkungsgrad', fontdict=font2)
    plt.grid(color = 'black', linestyle= '--', linewidth = 0.5)

    plt.scatter( temp_R32['PI'],temp_R32['eta_is_rosk'], label='R32', color = 'magenta')
    plt.scatter( temp_R290['PI'],temp_R290['eta_is_rosk'], label='R290', color='blue')
    plt.scatter( temp_R410A['PI'],temp_R410A['eta_is_rosk'], label='R410A', color='green')
    plt.scatter( temp_R454C['PI'],temp_R454C['eta_is_rosk'], label='R454C', color='red')
    plt.legend()
    plt.show()

Plot_eta(P_R32, P_R290, P_R410A, P_R454C)

from sklearn.linear_model import LinearRegression
def Calc_LinearModell(Df):
    LR = LinearRegression()
    Res_Df = pd.DataFrame()
    LR.fit(Df[['PI_Process']], Df[['eta_is_rosk']])
    x = LR.coef_[0]
    y = LR.intercept_
    z = LR.score(Df[['PI_Process']], Df[['eta_is_rosk']])
    Res_Df['COE'] = x
    Res_Df['LIN'] = y
    Res_Df['Score'] = z
    return Res_Df

LR_R32_eta = Calc_LinearModell(P_R32)
LR_R290_eta = Calc_LinearModell(P_R290)
LR_R410A_eta = Calc_LinearModell(P_R410A)
LR_R454C_eta = Calc_LinearModell(P_R454C)
print(LR_R32_eta ,LR_R290_eta, LR_R410A_eta, LR_R454C_eta, ' Das ist jetzt der wichtige Bumms')

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
Plot_ds_R32(P_R32, P_R290, P_R410A, P_R454C)
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


