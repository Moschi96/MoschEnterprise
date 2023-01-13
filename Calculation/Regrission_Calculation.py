
import statsmodels.api as sm
def stats():
    y =P_R410A['PI_Set']

    # Prädiktorvariablen definieren
    x = P_R410A[['P_loss','P1_Set']]

    # Konstante zu Prädiktorvariablen hinzufügen
    x = sm.add_constant(x)

    # lineares Regressionsmodell anpassen
    model = sm.OLS(y, x).fit()

    # Modellzusammenfassung anzeigen
    print(model.summary())

def P_R290_Pi35(R290_PI35_Df):
    '''Berechnung des Isentropen Wirkungsgrad'''
    #eta_is_R454C = func_eta_is(R454C_Df['h1'], R454C_Df['h2is'], R454C_Df['h2'])
    P_R290_PI35 = pd.DataFrame()
    #P_R454C['P_loss'], P_R454C['P_is'] = func_P_theo(R454C_Df['Power'], eta_is_R454C)
    P_R290_PI35['P_loss'], P_R290_PI53['P_is'] = func_P_Rosk(R290_PI35_Df['MF_Suc'], R290_PI35_Df['h2is'], R290_PI3_Df['h1'],
                                                     R290_PI35_Df['Power'])

    P_R290_PI35['P1_Set'] = R290_PI35_Df['P1_Set']
    P_R290_PI35['P2_Set'] = R290_PI3_Df['P2_Set']
    P_R290_PI35['P1_Process'] = R290_PI35_Df['P1_Process']
    P_R290_PI35['P2_Process'] = R290_PI35_Df['P2_Process']
    #P_R454C['eta_is'] = eta_is_R454C


    return   P_R290_PI35