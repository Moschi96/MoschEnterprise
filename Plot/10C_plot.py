import matplotlib.pyplot as plt
import pandas as pd
from CPolynominals import R410A_Df_MF
from CPolynominals import R410A_Df_POW
from CPolynominals import pup_pi3,pup_pi35,pup_pi4,pup_pi45,pup_pi5,pup_pi55,pup_pi6,pup_pi65,pub

def moredimensional():
    #print(R410A_Df_MF)
    '''
    xs1 = R410A_Df_MF['P1_Set']
    ys1 = R410A_Df_MF['PI_Set']
    zs1 = R410A_Df_MF['MF_Verhältnis']

    xs2 = R410A_Df_POW['P1_Set']
    ys2 = R410A_Df_POW['PI_Set']
    zs2 = R410A_Df_POW['Power_Verhältnis']

    'Drehzahl 50 Hertz Verdichter' \
    '' \
    'Min Max Fehler' \
    'Polynome
    ax = fig.add_subplot(111, projection='3d')

    #p1 p2 mf
    ax.scatter(xs1,ys1,zs1) # plot the point (2,3,4) on the figure
    plt.show()
    '''

def VerhältnissePowerPlot():
    fig, ax = plt.subplots(1,1,figsize=(13, 8), layout='constrained',sharey=True )
    #Festlegen der Achsenbeschriftung
    font1 = {'family':'serif','color':'black','size':15}
    font2 = {'family':'serif','color':'black','size':10}
    plt.title('Fehleranteil der Power über den Druckverlauf' , fontdict= font1)
    plt.xlabel('P1 in bar', fontdict= font2)
    plt.ylabel('Fehlerabweichung [%]', fontdict=font2)
    plt.grid(color = 'black', linestyle= '--', linewidth = 0.5)


    '''
    plt.scatter(pup_pi3['P1_Set'],pup_pi3['MF_Verhältnis'], label='PI=3')
    plt.scatter(pup_pi35['P1_Set'],pup_pi35['MF_Verhältnis'], label='PI=3.5')
    plt.scatter(pup_pi4['P1_Set'],pup_pi4['MF_Verhältnis'], label='PI=4')
    plt.scatter(pup_pi45['P1_Set'],pup_pi45['MF_Verhältnis'],label='PI=4.5')
    plt.scatter(pup_pi5['P1_Set'],pup_pi5['MF_Verhältnis'],label='PI=5')
    plt.scatter(pup_pi55['P1_Set'],pup_pi55['MF_Verhältnis'],label='PI=5.5')
    plt.scatter(pup_pi6['P1_Set'],pup_pi6['MF_Verhältnis'],label='PI=6')
    plt.scatter(pup_pi65['P1_Set'],pup_pi65['MF_Verhältnis'],label='PI=6.5')
    plt.text(8, 3.9, r'max.Verhältnis:4.97% bei P1=4bar/ PI=6', fontdict=font1)
    plt.text(8, 3.75, r'min.Verhältnis:0.52% bei P1=8bar/ PI=3.5', fontdict=font1)
    '''

    plt.scatter(pup_pi3['P1_Set'],pup_pi3['Power_Verhältnis'], label='PI=3')
    plt.scatter(pup_pi35['P1_Set'],pup_pi35['Power_Verhältnis'], label='PI=3.5')
    plt.scatter(pup_pi4['P1_Set'],pup_pi4['Power_Verhältnis'], label='PI=4')
    plt.scatter(pup_pi45['P1_Set'],pup_pi45['Power_Verhältnis'],label='PI=4.5')
    plt.scatter(pup_pi5['P1_Set'],pup_pi5['Power_Verhältnis'],label='PI=5')
    plt.scatter(pup_pi55['P1_Set'],pup_pi55['Power_Verhältnis'],label='PI=5.5')
    plt.scatter(pup_pi6['P1_Set'],pup_pi6['Power_Verhältnis'],label='PI=6')
    plt.scatter(pup_pi65['P1_Set'],pup_pi65['Power_Verhältnis'],label='PI=6.5')
    plt.text(12, 2, r'max.Verhältnis:14.66% bei P1=8bar/ PI=5.5', fontdict=font1)
    plt.text(12, 1.6, r'min.Verhältnis:0.55% bei P1=9bar/ PI=3', fontdict=font1)


    plt.legend()
    plt.savefig('Power_Verhältniss.png')
    plt.show()

def VerhältnisseMassPlot():
    fig, ax = plt.subplots(1,1,figsize=(13, 8), layout='constrained',sharey=True )
    #Festlegen der Achsenbeschriftung
    font1 = {'family':'serif','color':'black','size':15}
    font2 = {'family':'serif','color':'black','size':10}
    plt.title('Fehleranteil der Power über den Druckverlauf' , fontdict= font1)
    plt.xlabel('P1 in bar', fontdict= font2)
    plt.ylabel('Fehlerabweichung [%]', fontdict=font2)
    plt.grid(color = 'black', linestyle= '--', linewidth = 0.5)


    plt.scatter(pup_pi3['P1_Set'],pup_pi3['MF_Verhältnis'], label='PI=3')
    plt.scatter(pup_pi35['P1_Set'],pup_pi35['MF_Verhältnis'], label='PI=3.5')
    plt.scatter(pup_pi4['P1_Set'],pup_pi4['MF_Verhältnis'], label='PI=4')
    plt.scatter(pup_pi45['P1_Set'],pup_pi45['MF_Verhältnis'],label='PI=4.5')
    plt.scatter(pup_pi5['P1_Set'],pup_pi5['MF_Verhältnis'],label='PI=5')
    plt.scatter(pup_pi55['P1_Set'],pup_pi55['MF_Verhältnis'],label='PI=5.5')
    plt.scatter(pup_pi6['P1_Set'],pup_pi6['MF_Verhältnis'],label='PI=6')
    plt.scatter(pup_pi65['P1_Set'],pup_pi65['MF_Verhältnis'],label='PI=6.5')
    plt.text(8, 3.9, r'max.Verhältnis:4.97% bei P1=4bar/ PI=6', fontdict=font1)
    plt.text(8, 3.75, r'min.Verhältnis:0.52% bei P1=8bar/ PI=3.5', fontdict=font1)


    plt.legend()
    plt.savefig('Mass_Verhältniss.png')
    plt.show()

x = VerhältnissePowerPlot()
print(x)

#with pd.ExcelWriter('C10_Publicity.xlsx',engine= 'xlsxwriter') as writer:
#   pub.to_excel(writer, sheet_name='ResultsData')