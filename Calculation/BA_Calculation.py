def calc_eta_is(Df):
    Z = Df['h2is'] - Df['h1']
    N = Df['h2'] - Df['h1']
    eta_is = Z/N
    return eta_is


def calc_delta(df):
    df['delta_eta'] = df['eta_is'] - df['eta_is_rosk']
    return df
def calc_h2_mod(Df):
    Df['h2_loss'] = Df['T2_is'] * Df['delta_s']
    Df['h2_mod'] = Df['h2is'] + Df['h2_loss']
    Df['Abweichung_h2'] = (Df['h2'] / Df['h2_mod'] - 1 ) * 100
    return Df



