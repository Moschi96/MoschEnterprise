

from pyfluids import Fluid, FluidsList
import CoolProp
import CoolProp.CoolProp as CP








temp_T2_is = []
temp_h2_is = []
sp_list =[]
def calc_cis_mod(df , KM): #RKm_PIXX_DF
    for i in range(0, len(df)):
        h = pd.DataFrame()
        s1 = df.iloc[i]['s1'] * 1000
        h1 = df.iloc[i]['h1'] * 1000
        p2 = df.iloc[i]['P2_Process'] * 100000
        t2 = df.iloc[i]['T2_Process'] +273.15
        h2_is = CP.PropsSI('H', 'P', p2 , 'S', s1, str(KM))/1000
        T2_is = CP.PropsSI('d(H)/d(S)|P','P',p2,'S',s1, str(KM))
        sp = CP.PropsSI('S'   , 'P', p2 , 'H' , h1, str(KM)) / 1000



        sp_list.append(sp)



    return sp_list

