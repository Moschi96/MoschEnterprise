import matplotlib.pyplot as plt
import pandas as pd



def plot_LR(P_KM_PI, LR_KM_PI):
    print(P_KM_PI)
    fig, ax = plt.subplots(1,1,figsize=(13, 8), layout='constrained',sharey=True )
    #Festlegen der Achsenbeschriftung
    font1 = {'family':'serif','color':'black','size':15}
    font2 = {'family':'serif','color':'black','size':10}
    plt.title('Linear Regression ' , fontdict= font1)
    plt.xlabel('PI = p2/p1', fontdict= font2)
    plt.ylabel('Isentroper Wirkungsgrad', fontdict=font2)
    plt.grid(color = 'black', linestyle= '--', linewidth = 0.5)

    plt.scatter(P_KM_PI[['P1_Process']],P_KM_PI[['P_loss']], )
    plt.plot(P_KM_PI[['P1_Process']], LR_KM_PI.predict(P_KM_PI[['P1_Process']]), color = 'red')
    plt.legend()
    plt.show()

import matplotlib.pyplot as plt
import pandas as pd



def Eta_is_Ros_Vergleich_Plot(eta_is , eta_ros, PI_set,Res_Pi):
    fig, ax = plt.subplots(1,1,figsize=(13, 8), layout='constrained',sharey=True )
    #Festlegen der Achsenbeschriftung
    font1 = {'family':'serif','color':'black','size':15}
    font2 = {'family':'serif','color':'black','size':10}
    plt.title('Isentroper Wikrungsgrade über das DruckVerhältnis' , fontdict= font1)
    plt.xlabel('PI = p2/p1', fontdict= font2)
    plt.ylabel('Isentroper Wirkungsgrad', fontdict=font2)
    plt.grid(color = 'black', linestyle= '--', linewidth = 0.5)

    plt.scatter(PI_set,eta_is, label = 'eta_is')
    plt.scatter(PI_set,eta_ros, label = 'eta_ros')
    plt.plot(Res_Pi['PI_Set'],Res_Pi['eta_is'], label= 'eta_is_mean')
    plt.legend()



def Power_Loss_R410A_Plot_PI(P_R410A_pi3,P_R410A_pi35,P_R410A_pi4,P_R410A_pi45,P_R410A_pi5, P_R410A_pi55, P_R410A_pi6, P_R410A_pi65 ):
    fig, ax = plt.subplots(1,1,figsize=(20, 10), layout='constrained',sharey=True )
    #Festlegen der Achsenbeschriftung
    font1 = {'family':'serif','color':'black','size':20}
    font2 = {'family':'serif','color':'black','size':15}
    plt.title('Leistungsverluste R410A bei PI über dem Eingangsdruck' , fontdict= font1)
    plt.xlabel('P1', fontdict= font2)
    plt.ylabel('Power Loss [W]', fontdict=font2)
    plt.grid(color = 'black', linestyle= '--', linewidth = 0.5)


    plt.plot(P_R410A_pi3['P1_Set'],P_R410A_pi3['P_loss'] , label= 'PI3')
    plt.plot(P_R410A_pi35['P1_Set'], P_R410A_pi35['P_loss'], label= 'PI35' )
    plt.plot(P_R410A_pi4['P1_Set'], P_R410A_pi4['P_loss'], label='PI4')
    plt.plot(P_R410A_pi45['P1_Set'], P_R410A_pi45['P_loss'], label='PI45')
    plt.plot(P_R410A_pi5['P1_Set'], P_R410A_pi5['P_loss'], label='PI5')
    plt.plot(P_R410A_pi55['P1_Set'], P_R410A_pi55['P_loss'], label='PI55')
    plt.plot(P_R410A_pi6['P1_Set'], P_R410A_pi6['P_loss'], label='PI6')
    plt.plot(P_R410A_pi65['P1_Set'], P_R410A_pi65['P_loss'], label='PI65')
    plt.legend()
    plt.savefig('P_loss_R410A.svg' , format= 'svg')



def Power_Loss_R32_Plot_PI(P_R32_pi25, P_R32_pi3, P_R32_pi35, P_R32_pi4, P_R32_pi45, P_R32_pi5):
    fig, ax = plt.subplots(1,1,figsize=(13, 8), layout='constrained',sharey=True )
    #Festlegen der Achsenbeschriftung
    font1 = {'family':'serif','color':'black','size':15}
    font2 = {'family':'serif','color':'black','size':10}
    plt.title('Leistungsverluste R32 bei PI über dem Eingangsdruck' , fontdict= font1)
    plt.xlabel('P1', fontdict= font2)
    plt.ylabel('Power Loss [W]', fontdict=font2)
    plt.grid(color = 'black', linestyle= '--', linewidth = 0.5)

    plt.plot(P_R32_pi25['P1_Set'], P_R32_pi25['P_loss'], label='PI25')

    plt.plot(P_R32_pi3['P1_Set'],P_R32_pi3['P_loss'] , label= 'PI3')
    plt.plot(P_R32_pi35['P1_Set'], P_R32_pi35['P_loss'], label= 'PI35' )
    plt.plot(P_R32_pi4['P1_Set'], P_R32_pi4['P_loss'], label='PI4')
    plt.plot(P_R32_pi45['P1_Set'], P_R32_pi45['P_loss'], label='PI45')
    plt.plot(P_R32_pi5['P1_Set'], P_R32_pi5['P_loss'], label='PI5')

    plt.legend()



def Power_Loss_R290_Plot_PI(P_R290_pi25,P_R290_pi3, P_R290_pi35, P_R290_pi4, P_R290_pi45, P_R290_pi5, P_R290_pi55, P_R290_pi6, P_R290_pi65 ):
    fig, ax = plt.subplots(1,1,figsize=(13, 8), layout='constrained',sharey=True )
    #Festlegen der Achsenbeschriftung
    font1 = {'family':'serif','color':'black','size':15}
    font2 = {'family':'serif','color':'black','size':10}
    plt.title('Leistungsverluste R290 bei PI über dem Eingangsdruck' , fontdict= font1)
    plt.xlabel('P1', fontdict= font2)
    plt.ylabel('Power Loss [W]', fontdict=font2)
    plt.grid(color = 'black', linestyle= '--', linewidth = 0.5)

    plt.plot(P_R290_pi25['P1_Set'], P_R290_pi25['P_loss'], label='PI25')
    plt.plot(P_R290_pi3['P1_Set'],P_R290_pi3['P_loss'] , label= 'PI3')
    plt.plot(P_R290_pi35['P1_Set'], P_R290_pi35['P_loss'], label= 'PI35' )
    plt.plot(P_R290_pi4['P1_Set'], P_R290_pi4['P_loss'], label='PI4')
    plt.plot(P_R290_pi45['P1_Set'], P_R290_pi45['P_loss'], label='PI45')
    plt.plot(P_R290_pi5['P1_Set'], P_R290_pi5['P_loss'], label='PI5')
    plt.plot(P_R290_pi55['P1_Set'], P_R290_pi55['P_loss'], label='PI55')
    plt.plot(P_R290_pi6['P1_Set'], P_R290_pi6['P_loss'], label='PI6')
    plt.plot(P_R290_pi65['P1_Set'], P_R290_pi65['P_loss'], label='PI65')
    plt.legend()

def Power_Loss_R454C_Plot_PI(P_R454C_pi45, P_R454C_pi5, P_R454C_pi55,P_R454C_pi6,P_R454C_pi65  ):
    fig, ax = plt.subplots(1,1,figsize=(13, 8), layout='constrained',sharey=True )
    #Festlegen der Achsenbeschriftung
    font1 = {'family':'serif','color':'black','size':15}
    font2 = {'family':'serif','color':'black','size':10}
    plt.title('Leistungsverluste R454C bei PI über dem Eingangsdruck' , fontdict= font1)
    plt.xlabel('P1', fontdict= font2)
    plt.ylabel('Power Loss [W]', fontdict=font2)
    plt.grid(color = 'black', linestyle= '--', linewidth = 0.5)


    plt.plot(P_R454C_pi45['P1_Set'], P_R454C_pi45['P_loss'], label='PI45')
    plt.plot(P_R454C_pi5['P1_Set'], P_R454C_pi5['P_loss'], label='PI5')
    plt.plot(P_R454C_pi55['P1_Set'], P_R454C_pi55['P_loss'], label='PI55')
    plt.plot(P_R454C_pi6['P1_Set'], P_R454C_pi6['P_loss'], label='PI6')
    plt.plot(P_R454C_pi65['P1_Set'], P_R454C_pi65['P_loss'], label='PI65')
    plt.legend()


def Power_Loss_Plot_PI5(P_R410A_pi5, P_R32_pi5, P_R290_pi5,P_R454C_pi5  ):
    fig, ax = plt.subplots(1,1,figsize=(13, 8), layout='constrained',sharey=True )
    #Festlegen der Achsenbeschriftung
    font1 = {'family':'serif','color':'black','size':15}
    font2 = {'family':'serif','color':'black','size':10}
    plt.title('Leistungsverluste  bei PI = 5 ' , fontdict= font1)
    plt.xlabel('P1', fontdict= font2)
    plt.ylabel('Power Loss [W]', fontdict=font2)
    plt.grid(color = 'black', linestyle= '--', linewidth = 0.5)

    plt.plot(P_R410A_pi5['P1_Set'], P_R410A_pi5['P_loss'], label='R410A')
    plt.plot(P_R454C_pi5['P1_Set'], P_R454C_pi5['P_loss'], label='R454C')
    plt.plot(P_R32_pi5['P1_Set'], P_R32_pi5['P_loss'], label='R32')
    plt.plot(P_R290_pi5['P1_Set'], P_R290_pi5['P_loss'], label='R290')

    plt.legend()

def Power_Loss_Plot_PI45(P_R410A_pi45, P_R32_pi45, P_R290_pi45,P_R454C_pi45  ):
    fig, ax = plt.subplots(1,1,figsize=(13, 8), layout='constrained',sharey=True )
    #Festlegen der Achsenbeschriftung
    font1 = {'family':'serif','color':'black','size':15}
    font2 = {'family':'serif','color':'black','size':10}
    plt.title('Leistungsverluste  bei PI = 45 ' , fontdict= font1)
    plt.xlabel('P1', fontdict= font2)
    plt.ylabel('Power Loss [W]', fontdict=font2)
    plt.grid(color = 'black', linestyle= '--', linewidth = 0.5)

    plt.plot(P_R410A_pi45['P1_Set'], P_R410A_pi45['P_loss'], label='R410A')
    plt.plot(P_R454C_pi45['P1_Set'], P_R454C_pi45['P_loss'], label='R454C')
    plt.plot(P_R32_pi45['P1_Set'], P_R32_pi45['P_loss'], label='R32')
    plt.plot(P_R290_pi45['P1_Set'], P_R290_pi45['P_loss'], label='R290')

    plt.legend()

def Power_Loss_Plot_PI4(P_R410A_pi4, P_R32_pi4, P_R290_pi4 ):
    fig, ax = plt.subplots(1,1,figsize=(13, 8), layout='constrained',sharey=True )
    #Festlegen der Achsenbeschriftung
    font1 = {'family':'serif','color':'black','size':15}
    font2 = {'family':'serif','color':'black','size':10}
    plt.title('Leistungsverluste  bei PI = 4 ' , fontdict= font1)
    plt.xlabel('P1', fontdict= font2)
    plt.ylabel('Power Loss [W]', fontdict=font2)
    plt.grid(color = 'black', linestyle= '--', linewidth = 0.5)

    plt.plot(P_R410A_pi4['P1_Set'], P_R410A_pi4['P_loss'], label='R410A')

    plt.plot(P_R32_pi4['P1_Set'], P_R32_pi4['P_loss'], label='R32')
    plt.plot(P_R290_pi4['P1_Set'], P_R290_pi4['P_loss'], label='R290')

    plt.legend()

