import sympy
import pandas as pd
def Poly_10C_Calculation_Temp(C0, C1, C2, C3, C4, C5, C6, C7, C8, C9, Te, Tc):
    #Berechnungen der 10C-Polynome später als Funktion verwenden.
    erg = (C0) + (C1 * Te) + (C2 * Tc) + (C3 * Te ** 2) + (C4 * Te * Tc) + (C5 * Tc ** 2) + (C6 * Te ** 3) + (C7 * Te ** 2 * Tc) + (C8 * Te * Tc ** 2) + (C9 * Tc ** 3)
    return erg

def Poly_10C_Calculation(xd,Te,Tc):
    #print('Die Funktion Poly_10C_Calculation_wurde eingelesen')
    #erg= ZHI18K1P_Df.iloc[0] + ZHI18K1P_Df.iloc[1] *Te + ZHI18K1P_Df.iloc[2]*Tc + ZHI18K1P_Df.iloc[3]*(Te**2) +ZHI18K1P_Df.iloc[4]*Te*Tc + ZHI18K1P_Df.iloc[5]*(Tc**2) + ZHI18K1P_Df.iloc[6]*(Te**3) + ZHI18K1P_Df.iloc[7]*(Te**2) *Tc + ZHI18K1P_Df.iloc[8]*Te*(Tc**2) + ZHI18K1P_Df.iloc[9]*(Tc**3)
    ''' erg gibt direkt alle 4 Parameter Ergebnisse aus'''

    res_10CPoly = xd.iloc[0] + xd.iloc[1] * Te + xd.iloc[2] * Tc + xd.iloc[3] * (Te ** 2) + xd.iloc[4] * Te * Tc + xd.iloc[5] * (Tc ** 2) + xd.iloc[6] * (Te ** 3)+ xd.iloc[7] * (Te ** 2) * Tc + xd.iloc[8] * Te * (Tc ** 2) + xd.iloc[9] * (Tc ** 3)
    return res_10CPoly


def func_eta_isen_rosk(m_flow, h_2_isentrop, h_1, a_fac, b_fac, rho_1 ,  eta_Motor , PI_Set):
  Pis = ( m_flow * (h_2_isentrop- h_1)) * 1000 #kg/s * KJ/s = kW
  c = 1- eta_Motor
  denominator = ( Pis + a_fac + b_fac*((m_flow**3) / (rho_1**2)) ) * ( 1/(1-c))
  Rosk = pd.DataFrame()
  Rosk['Pis'] = Pis

  Rosk['denominator'] = denominator
  Rosk['a'] = a_fac
  Rosk['b'] = b_fac*(m_flow**3 / (rho_1**2))*1/(1-c)
  Rosk['m/rho'] = m_flow**3 / (rho_1**2)
  Rosk['m_flow'] = m_flow
  Rosk['rho'] = rho_1
  Rosk['PI_Set'] = PI_Set

  eta_is_ros = Pis/denominator
  Rosk['eta_is_ros'] = eta_is_ros
  return eta_is_ros , Rosk


def func_eta_a(m_flow, h_2_isentrop, h_1, a_fac):
  Pis = ( m_flow * (h_2_isentrop- h_1)) *1000
  denominator = ( (m_flow * ( h_2_isentrop - h_1)) + a_fac )
  eta_is_a = Pis/denominator
  return eta_is_a

def func_eta_b(m_flow, h_2_isentrop, h_1, b_fac, rho_1 ,  eta_Motor):
  Pis = ( m_flow * (h_2_isentrop- h_1)) *1000 #kg/s * KJ/kg = kW
  print('Das ist Pis' , Pis)
  c = 1 - eta_Motor
  denominator = ( (m_flow * ( h_2_isentrop - h_1))  + b_fac*(m_flow**3 / (rho_1**2))*1/(1-c))
  eta_is_b = Pis/denominator
  return eta_is_b


def func_split_PI(Res):
    '''Nimmt den DataFrame wo die isentropen Wirkungsgrade sind und bestimmt für jedes Druckverhältnis den Durschschni
    lichen Wirkungsgrad und die gesamt Abweichungdifferenz in %'''
    dRes_pi = pd.DataFrame()
    df_mask = Res['PI_Set'] == 3
    Res_pi3 = Res[df_mask]
    Res_pi3 = Res_pi3.drop(['PI_Set'], axis=1)
    dRes_pi['PI_3'] = (Res_pi3.max() - Res_pi3.min())*100
    df_mask = Res['PI_Set'] == 3.5
    Res_pi35 = Res[df_mask]
    dRes_pi['PI_35'] = (Res_pi35.max() - Res_pi35.min()) * 100
    df_mask = Res['PI_Set'] == 4
    Res_pi4 = Res[df_mask]
    dRes_pi['PI_4'] = (Res_pi4.max() - Res_pi4.min()) * 100
    df_mask = Res['PI_Set'] == 4.5
    Res_pi45 = Res[df_mask]
    dRes_pi['PI_45'] = (Res_pi45.max() - Res_pi45.min()) * 100
    df_mask = Res['PI_Set'] == 5
    Res_pi5 = Res[df_mask]
    dRes_pi['PI_5'] = (Res_pi5.max() - Res_pi5.min()) * 100
    df_mask = Res['PI_Set'] == 5.5
    Res_pi55 = Res[df_mask]
    dRes_pi['PI_55'] = (Res_pi55.max() - Res_pi55.min()) * 100
    df_mask = Res['PI_Set'] == 6
    Res_pi6 = Res[df_mask]
    dRes_pi['PI_6'] = (Res_pi6.max() - Res_pi6.min()) * 100
    df_mask = Res['PI_Set'] == 6.5
    Res_pi65 = Res[df_mask]
    dRes_pi['PI_65'] = (Res_pi65.max() - Res_pi65.min()) * 100
    Mean_Res_Pi = pd.DataFrame()
    Mean_Res_Pi['PI_3'] = round(Res_pi3.mean(), 4)
    Mean_Res_Pi['PI_35'] = round(Res_pi35.mean(), 4)
    Mean_Res_Pi['PI_4'] = round(Res_pi4.mean(), 4)
    Mean_Res_Pi['PI_45'] = round(Res_pi45.mean(), 4)
    Mean_Res_Pi['PI_5'] = round(Res_pi5.mean(), 4)
    Mean_Res_Pi['PI_55'] = round(Res_pi55.mean(), 4)
    Mean_Res_Pi['PI_6'] = round(Res_pi6.mean(), 4)
    Mean_Res_Pi['PI_65'] = round(Res_pi65.mean(), 4)
    dRes_pi = dRes_pi.rename(index={'eta_is': 'Abweichung_eta_is%', 'eta_is_Rosko': 'Abweichung_eta_is_Rosko%'})
    PI = pd.DataFrame({'PI_3': 3 , 'PI_35': 3.5, 'PI_4': 4,'PI_45': 4.5,'PI_5': 5,'PI_55': 5.5, 'PI_6': 6,'PI_65': 6.5}, index = ['PI_Set'])
    Res_pi = pd.concat([Mean_Res_Pi, dRes_pi[:]])
    Res_pi = pd.concat([PI , Res_pi[:]])

    return Res_pi




def KM_Mean_Dif(Res):
    '''Nimmt den DataFrame wo die isentropen Wirkungsgrade sind und bestimmt für jedes Druckverhältnis den Durschschni
    lichen Wirkungsgrad und die gesamt Abweichungdifferenz in %'''
    dRes_pi = pd.DataFrame()
    df_mask = Res['PI_Set'] == 3
    Res_pi3 = Res[df_mask]
    Res_pi3 = Res_pi3.drop(['PI_Set'], axis=1)
    dRes_pi['PI_3'] = (Res_pi3.max() - Res_pi3.min())
    df_mask = Res['PI_Set'] == 3.5
    Res_pi35 = Res[df_mask]
    dRes_pi['PI_35'] = (Res_pi35.max() - Res_pi35.min())
    df_mask = Res['PI_Set'] == 4
    Res_pi4 = Res[df_mask]
    dRes_pi['PI_4'] = (Res_pi4.max() - Res_pi4.min())
    df_mask = Res['PI_Set'] == 4.5
    Res_pi45 = Res[df_mask]
    dRes_pi['PI_45'] = (Res_pi45.max() - Res_pi45.min())
    df_mask = Res['PI_Set'] == 5
    Res_pi5 = Res[df_mask]
    dRes_pi['PI_5'] = (Res_pi5.max() - Res_pi5.min())
    df_mask = Res['PI_Set'] == 5.5
    Res_pi55 = Res[df_mask]
    dRes_pi['PI_55'] = (Res_pi55.max() - Res_pi55.min())
    df_mask = Res['PI_Set'] == 6
    Res_pi6 = Res[df_mask]
    dRes_pi['PI_6'] = (Res_pi6.max() - Res_pi6.min())
    df_mask = Res['PI_Set'] == 6.5
    Res_pi65 = Res[df_mask]
    dRes_pi['PI_65'] = (Res_pi65.max() - Res_pi65.min())
    Mean_Res_Pi = pd.DataFrame()
    Mean_Res_Pi['PI_3'] = round(Res_pi3.mean(), 4)
    Mean_Res_Pi['PI_35'] = round(Res_pi35.mean(), 4)
    Mean_Res_Pi['PI_4'] = round(Res_pi4.mean(), 4)
    Mean_Res_Pi['PI_45'] = round(Res_pi45.mean(), 4)
    Mean_Res_Pi['PI_5'] = round(Res_pi5.mean(), 4)
    Mean_Res_Pi['PI_55'] = round(Res_pi55.mean(), 4)
    Mean_Res_Pi['PI_6'] = round(Res_pi6.mean(), 4)
    Mean_Res_Pi['PI_65'] = round(Res_pi65.mean(), 4)
    dRes_pi = dRes_pi.rename(index={'eta_is': 'Dif_eta_is',})

    PI = pd.DataFrame({'PI_3': 3 , 'PI_35': 3.5, 'PI_4': 4,'PI_45': 4.5,'PI_5': 5,'PI_55': 5.5, 'PI_6': 6,'PI_65': 6.5}, index = ['PI_Set'])
    #calc_pi = pd.concat([Mean_Res_Pi,dRes_pi[:]])
    #calc_pi = pd.concat([PI, calc_pi[:]])



    return Mean_Res_Pi,dRes_pi

