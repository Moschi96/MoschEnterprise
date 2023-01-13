import pandas as pd


def func_eta_is( h_1, h_2_isentrop,h_2):
  eta_is =  (h_2_isentrop- h_1)/(h_2 - h_1)
  return eta_is


def func_P_theo(P_elec, eta_is):
    P_loss= P_elec*(1-eta_is)
    P_is = eta_is * P_elec
    return P_loss, P_is

def func_P_Rosk(mass_flow,h2_isentrop, h1, P_elec):
    P_is_ros = (mass_flow * (h2_isentrop - h1))
    P_loss = P_elec - P_is_ros
    return P_loss , P_is_ros



def P_R410A(R410A_Df):
    '''Berechnung des Isentropen Wirkungsgrad'''
    eta_is_R410A = func_eta_is(R410A_Df['h1'], R410A_Df['h2is'], R410A_Df['h2'])
    P_R410A = pd.DataFrame()
    #P_R410A['P_loss'], P_R410A['P_is'] = func_P_theo(R410A_Df['Power'], eta_is_R410A) für theoretisch
    P_R410A['P_loss'], P_R410A['P_is'] = func_P_Rosk(R410A_Df['MF_Suc'],R410A_Df['h2is'],R410A_Df['h1'],R410A_Df['Power'])
    P_R410A['PI_Set'] = R410A_Df['PI_Set']
    P_R410A['P1_Set'] = R410A_Df['P1_Set']
    P_R410A['P2_Set'] = R410A_Df['P2_Set']
    #P_R410A['eta_is'] = eta_is_R410A
    #print(R410A_Df)

    dummy_df = P_R410A['PI_Set'] == 3
    P_R410A_pi3 = P_R410A[dummy_df]
    # Res_pi3 = Res_pi3.drop(['PI_Set'], axis=1)

    dummy_df = P_R410A['PI_Set'] == 3.5
    P_R410A_pi35 = P_R410A[dummy_df]

    dummy_df = P_R410A['PI_Set'] == 4
    P_R410A_pi4 = P_R410A[dummy_df]

    dummy_df = P_R410A['PI_Set'] == 4.5
    P_R410A_pi45 = P_R410A[dummy_df]

    dummy_df = P_R410A['PI_Set'] == 5
    P_R410A_pi5 = P_R410A[dummy_df]

    dummy_df = P_R410A['PI_Set'] == 5.5
    P_R410A_pi55 = P_R410A[dummy_df]

    dummy_df = P_R410A['PI_Set'] == 6
    P_R410A_pi6 = P_R410A[dummy_df]

    dummy_df = P_R410A['PI_Set'] == 6.5
    P_R410A_pi65 = P_R410A[dummy_df]
    return P_R410A,P_R410A_pi3, P_R410A_pi35, P_R410A_pi4, P_R410A_pi45, P_R410A_pi5, P_R410A_pi55, P_R410A_pi6, P_R410A_pi65


def P_R32(R32_Df):
    '''Berechnung des Isentropen Wirkungsgrad'''
    eta_is_R32 = func_eta_is(R32_Df['h1'], R32_Df['h2is'], R32_Df['h2'])
    P_R32 = pd.DataFrame()
    #P_R32['P_loss'], P_R32['P_is'] = func_P_theo(R32_Df['Power'], eta_is_R32)
    P_R32['P_loss'], P_R32['P_is'] = func_P_Rosk(R32_Df['MF_Suc'], R32_Df['h2is'], R32_Df['h1'],
                                                     R32_Df['Power'])
    P_R32['PI_Set'] = R32_Df['PI_Set']
    P_R32['P1_Set'] = R32_Df['P1_Set']
    P_R32['P2_Set'] = R32_Df['P2_Set']
    #P_R32['eta_is'] = eta_is_R32

    dummy_df = P_R32['PI_Set'] == 2.5
    P_R32_pi25 = P_R32[dummy_df]

    dummy_df = P_R32['PI_Set'] == 3
    P_R32_pi3 = P_R32[dummy_df]
    # Res_pi3 = Res_pi3.drop(['PI_Set'], axis=1)

    dummy_df = P_R32['PI_Set'] == 3.5
    P_R32_pi35 = P_R32[dummy_df]

    dummy_df = P_R32['PI_Set'] == 4
    P_R32_pi4 = P_R32[dummy_df]

    dummy_df = P_R32['PI_Set'] == 4.5
    P_R32_pi45 = P_R32[dummy_df]

    dummy_df = P_R32['PI_Set'] == 5
    P_R32_pi5 = P_R32[dummy_df]
    return  P_R32_pi25,P_R32_pi3, P_R32_pi35, P_R32_pi4, P_R32_pi45, P_R32_pi5



def P_R290(R290_Df):
    '''Berechnung des Isentropen Wirkungsgrad'''
    eta_is_R290 = func_eta_is(R290_Df['h1'], R290_Df['h2is'], R290_Df['h2'])
    P_R290 = pd.DataFrame()
    #P_R290['P_loss'], P_R290['P_is'] = func_P_theo(R290_Df['Power'], eta_is_R290)
    P_R290['P_loss'], P_R290['P_is'] = func_P_Rosk(R290_Df['MF_Suc'], R290_Df['h2is'], R290_Df['h1'],
                                                     R290_Df['Power'])
    P_R290['PI_Set'] = R290_Df['PI_Set']
    P_R290['P1_Set'] = R290_Df['P1_Set']
    P_R290['P2_Set'] = R290_Df['P2_Set']
    #P_R290['eta_is'] = eta_is_R290

    dummy_df = P_R290['PI_Set'] == 2.5
    P_R290_pi25 = P_R290[dummy_df]
    dummy_df = P_R290['PI_Set'] == 3
    P_R290_pi3 = P_R290[dummy_df]
    # Res_pi3 = Res_pi3.drop(['PI_Set'], axis=1)

    dummy_df = P_R290['PI_Set'] == 3.5
    P_R290_pi35 = P_R290[dummy_df]

    dummy_df = P_R290['PI_Set'] == 4
    P_R290_pi4 = P_R290[dummy_df]

    dummy_df = P_R290['PI_Set'] == 4.5
    P_R290_pi45 = P_R290[dummy_df]

    dummy_df = P_R290['PI_Set'] == 5
    P_R290_pi5 = P_R290[dummy_df]

    dummy_df = P_R290['PI_Set'] == 5.5
    P_R290_pi55 = P_R290[dummy_df]

    dummy_df = P_R290['PI_Set'] == 6
    P_R290_pi6 = P_R290[dummy_df]

    dummy_df = P_R290['PI_Set'] == 6.5
    P_R290_pi65 = P_R290[dummy_df]
    return P_R290_pi25,P_R290_pi3, P_R290_pi35, P_R290_pi4, P_R290_pi45, P_R290_pi5, P_R290_pi55, P_R290_pi6, P_R290_pi65


def P_R454C(R454C_Df):
    '''Berechnung des Isentropen Wirkungsgrad'''
    #eta_is_R454C = func_eta_is(R454C_Df['h1'], R454C_Df['h2is'], R454C_Df['h2'])
    P_R454C = pd.DataFrame()
    #P_R454C['P_loss'], P_R454C['P_is'] = func_P_theo(R454C_Df['Power'], eta_is_R454C)
    P_R454C['P_loss'], P_R454C['P_is'] = func_P_Rosk(R454C_Df['MF_Suc'], R454C_Df['h2is'], R454C_Df['h1'],
                                                     R454C_Df['Power'])
    P_R454C['PI_Set'] = R454C_Df['PI_Set']
    P_R454C['P1_Set'] = R454C_Df['P1_Set']
    P_R454C['P2_Set'] = R454C_Df['P2_Set']
    #P_R454C['eta_is'] = eta_is_R454C

    dummy_df = P_R454C['PI_Set'] == 4.5
    P_R454C_pi45 = P_R454C[dummy_df]

    dummy_df = P_R454C['PI_Set'] == 5
    P_R454C_pi5 = P_R454C[dummy_df]
    # Res_pi3 = Res_pi3.drop(['PI_Set'], axis=1)

    dummy_df = P_R454C['PI_Set'] == 5.5
    P_R454C_pi55 = P_R454C[dummy_df]

    dummy_df = P_R454C['PI_Set'] == 6
    P_R454C_pi6 = P_R454C[dummy_df]

    dummy_df = P_R454C['PI_Set'] == 6.5
    P_R454C_pi65 = P_R454C[dummy_df]


    return   P_R454C_pi45, P_R454C_pi5, P_R454C_pi55,P_R454C_pi6,P_R454C_pi65



def P_R32_Pi25(R32_PI25_Df):
    '''Berechnung des Isentropen Wirkungsgrad'''
    #eta_is_R454C = func_eta_is(R454C_Df['h1'], R454C_Df['h2is'], R454C_Df['h2'])
    P_R32_PI25 = pd.DataFrame()
    #P_R454C['P_loss'], P_R454C['P_is'] = func_P_theo(R454C_Df['Power'], eta_is_R454C)
    P_R32_PI25['P_loss'], P_R32_PI25['P_is'] = func_P_Rosk(R32_PI25_Df['MF_Suc'], R32_PI25_Df['h2is'], R32_PI25_Df['h1'],
                                                     R32_PI25_Df['Power'])

    P_R32_PI25['P1_Set'] = R32_PI25_Df['P1_Set']
    P_R32_PI25['P2_Set'] = R32_PI25_Df['P2_Set']
    P_R32_PI25['P1_Process'] = R32_PI25_Df['P1_Process']
    P_R32_PI25['P2_Process'] = R32_PI25_Df['P2_Process']
    #P_R454C['eta_is'] = eta_is_R454C


    return   P_R32_PI25

def P_R32_Pi3(R32_PI3_Df):
    '''Berechnung des Isentropen Wirkungsgrad'''
    #eta_is_R454C = func_eta_is(R454C_Df['h1'], R454C_Df['h2is'], R454C_Df['h2'])
    P_R32_PI3 = pd.DataFrame()
    #P_R454C['P_loss'], P_R454C['P_is'] = func_P_theo(R454C_Df['Power'], eta_is_R454C)
    P_R32_PI3['P_loss'], P_R32_PI3['P_is'] = func_P_Rosk(R32_PI3_Df['MF_Suc'], R32_PI3_Df['h2is'], R32_PI3_Df['h1'],
                                                     R32_PI3_Df['Power'])

    P_R32_PI3['P1_Set'] = R32_PI3_Df['P1_Set']
    P_R32_PI3['P2_Set'] = R32_PI3_Df['P2_Set']
    P_R32_PI3['P1_Process'] = R32_PI3_Df['P1_Process']
    P_R32_PI3['P2_Process'] = R32_PI3_Df['P2_Process']
    #P_R454C['eta_is'] = eta_is_R454C


    return   P_R32_PI3


def P_R32_Pi35(R32_PI35_Df):
    '''Berechnung des Isentropen Wirkungsgrad'''
    #eta_is_R454C = func_eta_is(R454C_Df['h1'], R454C_Df['h2is'], R454C_Df['h2'])
    P_R32_PI35 = pd.DataFrame()
    #P_R454C['P_loss'], P_R454C['P_is'] = func_P_theo(R454C_Df['Power'], eta_is_R454C)
    P_R32_PI35['P_loss'], P_R32_PI35['P_is'] = func_P_Rosk(R32_PI35_Df['MF_Suc'], R32_PI35_Df['h2is'], R32_PI35_Df['h1'],
                                                     R32_PI35_Df['Power'])

    P_R32_PI35['P1_Set'] = R32_PI35_Df['P1_Set']
    P_R32_PI35['P2_Set'] = R32_PI35_Df['P2_Set']
    P_R32_PI35['P1_Process'] = R32_PI35_Df['P1_Process']
    P_R32_PI35['P2_Process'] = R32_PI35_Df['P2_Process']
    #P_R454C['eta_is'] = eta_is_R454C


    return   P_R32_PI35

def P_R32_Pi4(R32_PI4_Df):
    '''Berechnung des Isentropen Wirkungsgrad'''
    #eta_is_R454C = func_eta_is(R454C_Df['h1'], R454C_Df['h2is'], R454C_Df['h2'])
    P_R32_PI4 = pd.DataFrame()
    #P_R454C['P_loss'], P_R454C['P_is'] = func_P_theo(R454C_Df['Power'], eta_is_R454C)
    P_R32_PI4['P_loss'], P_R32_PI4['P_is'] = func_P_Rosk(R32_PI4_Df['MF_Suc'], R32_PI4_Df['h2is'], R32_PI4_Df['h1'],
                                                     R32_PI4_Df['Power'])

    P_R32_PI4['P1_Set'] = R32_PI4_Df['P1_Set']
    P_R32_PI4['P2_Set'] = R32_PI4_Df['P2_Set']
    P_R32_PI4['P1_Process'] = R32_PI4_Df['P1_Process']
    P_R32_PI4['P2_Process'] = R32_PI4_Df['P2_Process']
    #P_R454C['eta_is'] = eta_is_R454C


    return   P_R32_PI4

def P_R32_Pi45(R32_PI45_Df):
    '''Berechnung des Isentropen Wirkungsgrad'''
    #eta_is_R454C = func_eta_is(R454C_Df['h1'], R454C_Df['h2is'], R454C_Df['h2'])
    P_R32_PI45 = pd.DataFrame()
    #P_R454C['P_loss'], P_R454C['P_is'] = func_P_theo(R454C_Df['Power'], eta_is_R454C)
    P_R32_PI45['P_loss'], P_R32_PI45['P_is'] = func_P_Rosk(R32_PI45_Df['MF_Suc'], R32_PI45_Df['h2is'], R32_PI45_Df['h1'],
                                                     R32_PI45_Df['Power'])

    P_R32_PI45['P1_Set'] = R32_PI45_Df['P1_Set']
    P_R32_PI45['P2_Set'] = R32_PI45_Df['P2_Set']
    P_R32_PI45['P1_Process'] = R32_PI45_Df['P1_Process']
    P_R32_PI45['P2_Process'] = R32_PI45_Df['P2_Process']
    #P_R454C['eta_is'] = eta_is_R454C


    return   P_R32_PI45



def P_R290_Pi25(R290_PI25_Df):
    '''Berechnung des Isentropen Wirkungsgrad'''
    #eta_is_R454C = func_eta_is(R454C_Df['h1'], R454C_Df['h2is'], R454C_Df['h2'])
    P_R290_PI25 = pd.DataFrame()
    #P_R454C['P_loss'], P_R454C['P_is'] = func_P_theo(R454C_Df['Power'], eta_is_R454C)
    P_R290_PI25['P_loss'], P_R290_PI25['P_is'] = func_P_Rosk(R290_PI25_Df['MF_Suc'], R290_PI25_Df['h2is'], R290_PI25_Df['h1'],
                                                     R290_PI25_Df['Power'])

    P_R290_PI25['P1_Set'] = R290_PI25_Df['P1_Set']
    P_R290_PI25['P2_Set'] = R290_PI25_Df['P2_Set']
    P_R290_PI25['P1_Process'] = R290_PI25_Df['P1_Process']
    P_R290_PI25['P2_Process'] = R290_PI25_Df['P2_Process']
    #P_R454C['eta_is'] = eta_is_R454C


    return   P_R290_PI25

def P_R290_Pi3(R290_PI3_Df):
    '''Berechnung des Isentropen Wirkungsgrad'''
    #eta_is_R454C = func_eta_is(R454C_Df['h1'], R454C_Df['h2is'], R454C_Df['h2'])
    P_R290_PI3 = pd.DataFrame()
    #P_R454C['P_loss'], P_R454C['P_is'] = func_P_theo(R454C_Df['Power'], eta_is_R454C)
    P_R290_PI3['P_loss'], P_R290_PI3['P_is'] = func_P_Rosk(R290_PI3_Df['MF_Suc'], R290_PI3_Df['h2is'], R290_PI3_Df['h1'],
                                                     R290_PI3_Df['Power'])

    P_R290_PI3['P1_Set'] = R290_PI3_Df['P1_Set']
    P_R290_PI3['P2_Set'] = R290_PI3_Df['P2_Set']
    P_R290_PI3['P1_Process'] = R290_PI3_Df['P1_Process']
    P_R290_PI3['P2_Process'] = R290_PI3_Df['P2_Process']
    #P_R454C['eta_is'] = eta_is_R454C


    return   P_R290_PI3

def P_R290_Pi35(R290_PI35_Df):
    '''Berechnung des Isentropen Wirkungsgrad'''
    #eta_is_R454C = func_eta_is(R454C_Df['h1'], R454C_Df['h2is'], R454C_Df['h2'])
    P_R290_PI35 = pd.DataFrame()
    #P_R454C['P_loss'], P_R454C['P_is'] = func_P_theo(R454C_Df['Power'], eta_is_R454C)
    P_R290_PI35['P_loss'], P_R290_PI35['P_is'] = func_P_Rosk(R290_PI35_Df['MF_Suc'], R290_PI35_Df['h2is'], R290_PI35_Df['h1'],
                                                     R290_PI35_Df['Power'])

    P_R290_PI35['P1_Set'] = R290_PI35_Df['P1_Set']
    P_R290_PI35['P2_Set'] = R290_PI35_Df['P2_Set']
    P_R290_PI35['P1_Process'] = R290_PI35_Df['P1_Process']
    P_R290_PI35['P2_Process'] = R290_PI35_Df['P2_Process']
    #P_R454C['eta_is'] = eta_is_R454C


    return   P_R290_PI35

def P_R290_Pi4(R290_PI4_Df):
    '''Berechnung des Isentropen Wirkungsgrad'''
    #eta_is_R454C = func_eta_is(R454C_Df['h1'], R454C_Df['h2is'], R454C_Df['h2'])
    P_R290_PI4 = pd.DataFrame()
    #P_R454C['P_loss'], P_R454C['P_is'] = func_P_theo(R454C_Df['Power'], eta_is_R454C)
    P_R290_PI4['P_loss'], P_R290_PI4['P_is'] = func_P_Rosk(R290_PI4_Df['MF_Suc'], R290_PI4_Df['h2is'], R290_PI4_Df['h1'],
                                                     R290_PI4_Df['Power'])

    P_R290_PI4['P1_Set'] = R290_PI4_Df['P1_Set']
    P_R290_PI4['P2_Set'] = R290_PI4_Df['P2_Set']
    P_R290_PI4['P1_Process'] = R290_PI4_Df['P1_Process']
    P_R290_PI4['P2_Process'] = R290_PI4_Df['P2_Process']
    #P_R454C['eta_is'] = eta_is_R454C


    return   P_R290_PI4

def P_R290_Pi45(R290_PI45_Df):
    '''Berechnung des Isentropen Wirkungsgrad'''
    #eta_is_R454C = func_eta_is(R454C_Df['h1'], R454C_Df['h2is'], R454C_Df['h2'])
    P_R290_PI45 = pd.DataFrame()
    #P_R454C['P_loss'], P_R454C['P_is'] = func_P_theo(R454C_Df['Power'], eta_is_R454C)
    P_R290_PI45['P_loss'], P_R290_PI45['P_is'] = func_P_Rosk(R290_PI45_Df['MF_Suc'], R290_PI45_Df['h2is'], R290_PI45_Df['h1'],
                                                     R290_PI45_Df['Power'])

    P_R290_PI45['P1_Set'] = R290_PI45_Df['P1_Set']
    P_R290_PI45['P2_Set'] = R290_PI45_Df['P2_Set']
    P_R290_PI45['P1_Process'] = R290_PI45_Df['P1_Process']
    P_R290_PI45['P2_Process'] = R290_PI45_Df['P2_Process']
    #P_R454C['eta_is'] = eta_is_R454C


    return   P_R290_PI45


def P_R290_Pi5(R290_PI5_Df):
    '''Berechnung des Isentropen Wirkungsgrad'''
    #eta_is_R454C = func_eta_is(R454C_Df['h1'], R454C_Df['h2is'], R454C_Df['h2'])
    P_R290_PI5 = pd.DataFrame()
    #P_R454C['P_loss'], P_R454C['P_is'] = func_P_theo(R454C_Df['Power'], eta_is_R454C)
    P_R290_PI5['P_loss'], P_R290_PI5['P_is'] = func_P_Rosk(R290_PI5_Df['MF_Suc'], R290_PI5_Df['h2is'], R290_PI5_Df['h1'],
                                                     R290_PI5_Df['Power'])

    P_R290_PI5['P1_Set'] = R290_PI5_Df['P1_Set']
    P_R290_PI5['P2_Set'] = R290_PI5_Df['P2_Set']
    P_R290_PI5['P1_Process'] = R290_PI5_Df['P1_Process']
    P_R290_PI5['P2_Process'] = R290_PI5_Df['P2_Process']
    #P_R454C['eta_is'] = eta_is_R454C


    return   P_R290_PI5


def P_R290_Pi55(R290_PI55_Df):
    '''Berechnung des Isentropen Wirkungsgrad'''
    #eta_is_R454C = func_eta_is(R454C_Df['h1'], R454C_Df['h2is'], R454C_Df['h2'])
    P_R290_PI55 = pd.DataFrame()
    #P_R454C['P_loss'], P_R454C['P_is'] = func_P_theo(R454C_Df['Power'], eta_is_R454C)
    P_R290_PI55['P_loss'], P_R290_PI55['P_is'] = func_P_Rosk(R290_PI55_Df['MF_Suc'], R290_PI55_Df['h2is'], R290_PI55_Df['h1'],
                                                     R290_PI55_Df['Power'])

    P_R290_PI55['P1_Set'] = R290_PI55_Df['P1_Set']
    P_R290_PI55['P2_Set'] = R290_PI55_Df['P2_Set']
    P_R290_PI55['P1_Process'] = R290_PI55_Df['P1_Process']
    P_R290_PI55['P2_Process'] = R290_PI55_Df['P2_Process']
    #P_R454C['eta_is'] = eta_is_R454C


    return   P_R290_PI55

def P_R290_Pi6(R290_PI6_Df):
    '''Berechnung des Isentropen Wirkungsgrad'''
    #eta_is_R454C = func_eta_is(R454C_Df['h1'], R454C_Df['h2is'], R454C_Df['h2'])
    P_R290_PI6 = pd.DataFrame()
    #P_R454C['P_loss'], P_R454C['P_is'] = func_P_theo(R454C_Df['Power'], eta_is_R454C)
    P_R290_PI6['P_loss'], P_R290_PI6['P_is'] = func_P_Rosk(R290_PI6_Df['MF_Suc'], R290_PI6_Df['h2is'], R290_PI6_Df['h1'],
                                                     R290_PI6_Df['Power'])

    P_R290_PI6['P1_Set'] = R290_PI6_Df['P1_Set']
    P_R290_PI6['P2_Set'] = R290_PI6_Df['P2_Set']
    P_R290_PI6['P1_Process'] = R290_PI6_Df['P1_Process']
    P_R290_PI6['P2_Process'] = R290_PI6_Df['P2_Process']
    #P_R454C['eta_is'] = eta_is_R454C


    return   P_R290_PI6
def P_R290_Pi65(R290_PI65_Df):
    '''Berechnung des Isentropen Wirkungsgrad'''
    #eta_is_R454C = func_eta_is(R454C_Df['h1'], R454C_Df['h2is'], R454C_Df['h2'])
    P_R290_PI65 = pd.DataFrame()
    #P_R454C['P_loss'], P_R454C['P_is'] = func_P_theo(R454C_Df['Power'], eta_is_R454C)
    P_R290_PI65['P_loss'], P_R290_PI65['P_is'] = func_P_Rosk(R290_PI65_Df['MF_Suc'], R290_PI65_Df['h2is'], R290_PI65_Df['h1'],
                                                           R290_PI65_Df['Power'])

    P_R290_PI65['P1_Set'] = R290_PI65_Df['P1_Set']
    P_R290_PI65['P2_Set'] = R290_PI65_Df['P2_Set']
    P_R290_PI65['P1_Process'] = R290_PI65_Df['P1_Process']
    P_R290_PI65['P2_Process'] = R290_PI65_Df['P2_Process']
    #P_R454C['eta_is'] = eta_is_R454C


    return   P_R290_PI65



def P_R410A_Pi3(R410A_PI3_Df):
    '''Berechnung des Isentropen Wirkungsgrad'''
    #eta_is_R454C = func_eta_is(R454C_Df['h1'], R454C_Df['h2is'], R454C_Df['h2'])
    P_R410A_PI3 = pd.DataFrame()
    #P_R454C['P_loss'], P_R454C['P_is'] = func_P_theo(R454C_Df['Power'], eta_is_R454C)
    P_R410A_PI3['P_loss'], P_R410A_PI3['P_is'] = func_P_Rosk(R410A_PI3_Df['MF_Suc'], R410A_PI3_Df['h2is'], R410A_PI3_Df['h1'],
                                                             R410A_PI3_Df['Power'])

    P_R410A_PI3['P1_Set'] = R410A_PI3_Df['P1_Set']
    P_R410A_PI3['P2_Set'] = R410A_PI3_Df['P2_Set']
    P_R410A_PI3['P1_Process'] = R410A_PI3_Df['P1_Process']
    P_R410A_PI3['P2_Process'] = R410A_PI3_Df['P2_Process']
    #P_R454C['eta_is'] = eta_is_R454C


    return   P_R410A_PI3

def P_R410A_Pi35(R410A_PI35_Df):
    '''Berechnung des Isentropen Wirkungsgrad'''
    #eta_is_R454C = func_eta_is(R454C_Df['h1'], R454C_Df['h2is'], R454C_Df['h2'])
    P_R410A_PI35 = pd.DataFrame()
    #P_R454C['P_loss'], P_R454C['P_is'] = func_P_theo(R454C_Df['Power'], eta_is_R454C)
    P_R410A_PI35['P_loss'], P_R410A_PI35['P_is'] = func_P_Rosk(R410A_PI35_Df['MF_Suc'], R410A_PI35_Df['h2is'], R410A_PI35_Df['h1'],
                                                             R410A_PI35_Df['Power'])

    P_R410A_PI35['P1_Set'] = R410A_PI35_Df['P1_Set']
    P_R410A_PI35['P2_Set'] = R410A_PI35_Df['P2_Set']
    P_R410A_PI35['P1_Process'] = R410A_PI35_Df['P1_Process']
    P_R410A_PI35['P2_Process'] = R410A_PI35_Df['P2_Process']
    #P_R454C['eta_is'] = eta_is_R454C


    return   P_R410A_PI35

def P_R410A_Pi4(R410A_PI4_Df):
    '''Berechnung des Isentropen Wirkungsgrad'''
    #eta_is_R454C = func_eta_is(R454C_Df['h1'], R454C_Df['h2is'], R454C_Df['h2'])
    P_R410A_PI4 = pd.DataFrame()
    #P_R454C['P_loss'], P_R454C['P_is'] = func_P_theo(R454C_Df['Power'], eta_is_R454C)
    P_R410A_PI4['P_loss'], P_R410A_PI4['P_is'] = func_P_Rosk(R410A_PI4_Df['MF_Suc'], R410A_PI4_Df['h2is'], R410A_PI4_Df['h1'],
                                                               R410A_PI4_Df['Power'])

    P_R410A_PI4['P1_Set'] = R410A_PI4_Df['P1_Set']
    P_R410A_PI4['P2_Set'] = R410A_PI4_Df['P2_Set']
    P_R410A_PI4['P1_Process'] = R410A_PI4_Df['P1_Process']
    P_R410A_PI4['P2_Process'] = R410A_PI4_Df['P2_Process']
    #P_R454C['eta_is'] = eta_is_R454C


    return   P_R410A_PI4

def P_R410A_Pi45(R410A_PI45_Df):
    '''Berechnung des Isentropen Wirkungsgrad'''
    #eta_is_R454C = func_eta_is(R454C_Df['h1'], R454C_Df['h2is'], R454C_Df['h2'])
    P_R410A_PI45 = pd.DataFrame()
    #P_R454C['P_loss'], P_R454C['P_is'] = func_P_theo(R454C_Df['Power'], eta_is_R454C)
    P_R410A_PI45['P_loss'], P_R410A_PI45['P_is'] = func_P_Rosk(R410A_PI45_Df['MF_Suc'], R410A_PI45_Df['h2is'], R410A_PI45_Df['h1'],
                                                             R410A_PI45_Df['Power'])

    P_R410A_PI45['P1_Set'] = R410A_PI45_Df['P1_Set']
    P_R410A_PI45['P2_Set'] = R410A_PI45_Df['P2_Set']
    P_R410A_PI45['P1_Process'] = R410A_PI45_Df['P1_Process']
    P_R410A_PI45['P2_Process'] = R410A_PI45_Df['P2_Process']
    #P_R454C['eta_is'] = eta_is_R454C


    return   P_R410A_PI45

def P_R410A_Pi5(R410A_PI5_Df):
    '''Berechnung des Isentropen Wirkungsgrad'''
    #eta_is_R454C = func_eta_is(R454C_Df['h1'], R454C_Df['h2is'], R454C_Df['h2'])
    P_R410A_PI5 = pd.DataFrame()
    #P_R454C['P_loss'], P_R454C['P_is'] = func_P_theo(R454C_Df['Power'], eta_is_R454C)
    P_R410A_PI5['P_loss'], P_R410A_PI5['P_is'] = func_P_Rosk(R410A_PI5_Df['MF_Suc'], R410A_PI5_Df['h2is'], R410A_PI5_Df['h1'],
                                                               R410A_PI5_Df['Power'])

    P_R410A_PI5['P1_Set'] = R410A_PI5_Df['P1_Set']
    P_R410A_PI5['P2_Set'] = R410A_PI5_Df['P2_Set']
    P_R410A_PI5['P1_Process'] = R410A_PI5_Df['P1_Process']
    P_R410A_PI5['P2_Process'] = R410A_PI5_Df['P2_Process']
    #P_R454C['eta_is'] = eta_is_R454C


    return   P_R410A_PI5



def P_R410A_Pi55(R410A_PI55_Df):
    '''Berechnung des Isentropen Wirkungsgrad'''
    #eta_is_R454C = func_eta_is(R454C_Df['h1'], R454C_Df['h2is'], R454C_Df['h2'])
    P_R410A_PI55 = pd.DataFrame()
    #P_R454C['P_loss'], P_R454C['P_is'] = func_P_theo(R454C_Df['Power'], eta_is_R454C)
    P_R410A_PI55['P_loss'], P_R410A_PI55['P_is'] = func_P_Rosk(R410A_PI55_Df['MF_Suc'], R410A_PI55_Df['h2is'], R410A_PI55_Df['h1'],
                                                             R410A_PI55_Df['Power'])

    P_R410A_PI55['P1_Set'] = R410A_PI55_Df['P1_Set']
    P_R410A_PI55['P2_Set'] = R410A_PI55_Df['P2_Set']
    P_R410A_PI55['P1_Process'] = R410A_PI55_Df['P1_Process']
    P_R410A_PI55['P2_Process'] = R410A_PI55_Df['P2_Process']
    #P_R454C['eta_is'] = eta_is_R454C


    return   P_R410A_PI55

def P_R410A_Pi6(R410A_PI6_Df):
    '''Berechnung des Isentropen Wirkungsgrad'''
    #eta_is_R454C = func_eta_is(R454C_Df['h1'], R454C_Df['h2is'], R454C_Df['h2'])
    P_R410A_PI6 = pd.DataFrame()
    #P_R454C['P_loss'], P_R454C['P_is'] = func_P_theo(R454C_Df['Power'], eta_is_R454C)
    P_R410A_PI6['P_loss'], P_R410A_PI6['P_is'] = func_P_Rosk(R410A_PI6_Df['MF_Suc'], R410A_PI6_Df['h2is'], R410A_PI6_Df['h1'],
                                                               R410A_PI6_Df['Power'])

    P_R410A_PI6['P1_Set'] = R410A_PI6_Df['P1_Set']
    P_R410A_PI6['P2_Set'] = R410A_PI6_Df['P2_Set']
    P_R410A_PI6['P1_Process'] = R410A_PI6_Df['P1_Process']
    P_R410A_PI6['P2_Process'] = R410A_PI6_Df['P2_Process']
    #P_R454C['eta_is'] = eta_is_R454C


    return   P_R410A_PI6


def P_R410A_Pi65(R410A_PI65_Df):
    '''Berechnung des Isentropen Wirkungsgrad'''
    #eta_is_R454C = func_eta_is(R454C_Df['h1'], R454C_Df['h2is'], R454C_Df['h2'])
    P_R410A_PI65 = pd.DataFrame()
    #P_R454C['P_loss'], P_R454C['P_is'] = func_P_theo(R454C_Df['Power'], eta_is_R454C)
    P_R410A_PI65['P_loss'], P_R410A_PI65['P_is'] = func_P_Rosk(R410A_PI65_Df['MF_Suc'], R410A_PI65_Df['h2is'], R410A_PI65_Df['h1'],
                                                             R410A_PI65_Df['Power'])

    P_R410A_PI65['P1_Set'] = R410A_PI65_Df['P1_Set']
    P_R410A_PI65['P2_Set'] = R410A_PI65_Df['P2_Set']
    P_R410A_PI65['P1_Process'] = R410A_PI65_Df['P1_Process']
    P_R410A_PI65['P2_Process'] = R410A_PI65_Df['P2_Process']
    #P_R454C['eta_is'] = eta_is_R454C


    return   P_R410A_PI65

def P_R454C_Pi35(R454C_PI35_Df):
    '''Berechnung des Isentropen Wirkungsgrad'''
    #eta_is_R454C = func_eta_is(R454C_Df['h1'], R454C_Df['h2is'], R454C_Df['h2'])
    P_R454C_PI35 = pd.DataFrame()
    #P_R454C['P_loss'], P_R454C['P_is'] = func_P_theo(R454C_Df['Power'], eta_is_R454C)
    P_R454C_PI35['P_loss'], P_R454C_PI35['P_is'] = func_P_Rosk(R454C_PI35_Df['MF_Suc'], R454C_PI35_Df['h2is'], R454C_PI35_Df['h1'],
                                                               R454C_PI35_Df['Power'])

    P_R454C_PI35['P1_Set'] = R454C_PI35_Df['P1_Set']
    P_R454C_PI35['P2_Set'] = R454C_PI35_Df['P2_Set']
    P_R454C_PI35['P1_Process'] = R454C_PI35_Df['P1_Process']
    P_R454C_PI35['P2_Process'] = R454C_PI35_Df['P2_Process']
    #P_R454C['eta_is'] = eta_is_R454C


    return   P_R454C_PI35

def P_R454C_Pi45(R454C_PI45_Df):
    '''Berechnung des Isentropen Wirkungsgrad'''
    #eta_is_R454C = func_eta_is(R454C_Df['h1'], R454C_Df['h2is'], R454C_Df['h2'])
    P_R454C_PI45 = pd.DataFrame()
    #P_R454C['P_loss'], P_R454C['P_is'] = func_P_theo(R454C_Df['Power'], eta_is_R454C)
    P_R454C_PI45['P_loss'], P_R454C_PI45['P_is'] = func_P_Rosk(R454C_PI45_Df['MF_Suc'], R454C_PI45_Df['h2is'], R454C_PI45_Df['h1'],
                                                               R454C_PI45_Df['Power'])

    P_R454C_PI45['P1_Set'] = R454C_PI45_Df['P1_Set']
    P_R454C_PI45['P2_Set'] = R454C_PI45_Df['P2_Set']
    P_R454C_PI45['P1_Process'] = R454C_PI45_Df['P1_Process']
    P_R454C_PI45['P2_Process'] = R454C_PI45_Df['P2_Process']
    #P_R454C['eta_is'] = eta_is_R454C


    return   P_R454C_PI45

def P_R454C_Pi5(R454C_PI5_Df):
    '''Berechnung des Isentropen Wirkungsgrad'''
    #eta_is_R454C = func_eta_is(R454C_Df['h1'], R454C_Df['h2is'], R454C_Df['h2'])
    P_R454C_PI5 = pd.DataFrame()
    #P_R454C['P_loss'], P_R454C['P_is'] = func_P_theo(R454C_Df['Power'], eta_is_R454C)
    P_R454C_PI5['P_loss'], P_R454C_PI5['P_is'] = func_P_Rosk(R454C_PI5_Df['MF_Suc'], R454C_PI5_Df['h2is'], R454C_PI5_Df['h1'],
                                                               R454C_PI5_Df['Power'])

    P_R454C_PI5['P1_Set'] = R454C_PI5_Df['P1_Set']
    P_R454C_PI5['P2_Set'] = R454C_PI5_Df['P2_Set']
    P_R454C_PI5['P1_Process'] = R454C_PI5_Df['P1_Process']
    P_R454C_PI5['P2_Process'] = R454C_PI5_Df['P2_Process']
    #P_R454C['eta_is'] = eta_is_R454C


    return   P_R454C_PI5

def P_R454C_Pi55(R454C_PI55_Df):
    '''Berechnung des Isentropen Wirkungsgrad'''
    #eta_is_R454C = func_eta_is(R454C_Df['h1'], R454C_Df['h2is'], R454C_Df['h2'])
    P_R454C_PI55 = pd.DataFrame()
    #P_R454C['P_loss'], P_R454C['P_is'] = func_P_theo(R454C_Df['Power'], eta_is_R454C)
    P_R454C_PI55['P_loss'], P_R454C_PI55['P_is'] = func_P_Rosk(R454C_PI55_Df['MF_Suc'], R454C_PI55_Df['h2is'], R454C_PI55_Df['h1'],
                                                             R454C_PI55_Df['Power'])

    P_R454C_PI55['P1_Set'] = R454C_PI55_Df['P1_Set']
    P_R454C_PI55['P2_Set'] = R454C_PI55_Df['P2_Set']
    P_R454C_PI55['P1_Process'] = R454C_PI55_Df['P1_Process']
    P_R454C_PI55['P2_Process'] = R454C_PI55_Df['P2_Process']
    #P_R454C['eta_is'] = eta_is_R454C


    return   P_R454C_PI55


def P_R454C_Pi6(R454C_PI6_Df):
    '''Berechnung des Isentropen Wirkungsgrad'''
    #eta_is_R454C = func_eta_is(R454C_Df['h1'], R454C_Df['h2is'], R454C_Df['h2'])
    P_R454C_PI6 = pd.DataFrame()
    #P_R454C['P_loss'], P_R454C['P_is'] = func_P_theo(R454C_Df['Power'], eta_is_R454C)
    P_R454C_PI6['P_loss'], P_R454C_PI6['P_is'] = func_P_Rosk(R454C_PI6_Df['MF_Suc'], R454C_PI6_Df['h2is'], R454C_PI6_Df['h1'],
                                                               R454C_PI6_Df['Power'])

    P_R454C_PI6['P1_Set'] = R454C_PI6_Df['P1_Set']
    P_R454C_PI6['P2_Set'] = R454C_PI6_Df['P2_Set']
    P_R454C_PI6['P1_Process'] = R454C_PI6_Df['P1_Process']
    P_R454C_PI6['P2_Process'] = R454C_PI6_Df['P2_Process']
    #P_R454C['eta_is'] = eta_is_R454C


    return   P_R454C_PI6



def P_R454C_Pi65(R454C_PI65_Df):
    '''Berechnung des Isentropen Wirkungsgrad'''
    #eta_is_R454C = func_eta_is(R454C_Df['h1'], R454C_Df['h2is'], R454C_Df['h2'])
    P_R454C_PI65 = pd.DataFrame()
    #P_R454C['P_loss'], P_R454C['P_is'] = func_P_theo(R454C_Df['Power'], eta_is_R454C)
    P_R454C_PI65['P_loss'], P_R454C_PI65['P_is'] = func_P_Rosk(R454C_PI65_Df['MF_Suc'], R454C_PI65_Df['h2is'], R454C_PI65_Df['h1'],
                                                             R454C_PI65_Df['Power'])

    P_R454C_PI65['P1_Set'] = R454C_PI65_Df['P1_Set']
    P_R454C_PI65['P2_Set'] = R454C_PI65_Df['P2_Set']
    P_R454C_PI65['P1_Process'] = R454C_PI65_Df['P1_Process']
    P_R454C_PI65['P2_Process'] = R454C_PI65_Df['P2_Process']
    #P_R454C['eta_is'] = eta_is_R454C


    return   P_R454C_PI65