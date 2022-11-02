import matplotlib.pyplot as plt
import pandas as pd



def Eta_is_Plot(eta_is , eta_ros, PI_set,Res_Pi):
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
    plt.show()


