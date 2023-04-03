
import statsmodels.api as sm
def stats(df):
    y =df['PI_Set']

    # Prädiktorvariablen definieren
    x = df[['P_loss','P1_Set']]

    # Konstante zu Prädiktorvariablen hinzufügen
    x = sm.add_constant(x)

    # lineares Regressionsmodell anpassen
    model = sm.OLS(y, x).fit()

    # Modellzusammenfassung anzeigen
    print(model.summary())



from sklearn.preprocessing import PolynomialFeatures
def calc_Poly_regression(df):
    poly = PolynomialFeatures(degree=2, include_bias=False)