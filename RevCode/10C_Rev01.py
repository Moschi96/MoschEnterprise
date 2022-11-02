from load_data import getdataZHI18K1P

rawdata_ZHI18K1P,coolcap, power, current, sucmassflow = getdataZHI18K1P()

print(coolcap)

'Die Verdampfungstemperatur bei Verdichtereingangsdruck in °C'
Te = float(-5)
'Die Kondensationstemperatur bei Verdichterausgangsdruck in °C'
Tc = float(40)

#Ergebniss bei -35 Verdampfung und 40 Kondensation: 4.683 kW Wärmeleistung
#print(coolcap)

def Calculation(C0,C1,C2,C3,C4,C5,C6,C7,C8,C9 ):
    #Berechnungen der 10C-Polynome später als Funktion verwenden.
    erg = (C0) + (C1 * Te) + (C2 * Tc) + (C3 * Te ** 2) + (C4 * Te * Tc) + (C5 * Tc ** 2) + (C6 * Te ** 3) + (C7 * Te ** 2 * Tc) + (C8 * Te * Tc ** 2) + (C9 * Tc ** 3)

    return erg



C0_cool= coolcap['C0']
C1_cool = coolcap['C1']
C2_cool = coolcap['C2']
C3_cool = coolcap['C3']
C4_cool = coolcap['C4']
C5_cool = coolcap['C5']
C6_cool = coolcap['C6']
C7_cool = coolcap['C7']
C8_cool = coolcap['C8']
C9_cool = coolcap['C9']
Einheit = coolcap['Einheiten']

cp = (C0_cool, C1_cool, C2_cool, C3_cool, C4_cool, C5_cool, C6_cool, C7_cool, C8_cool, C9_cool)

C0_power= power['C0']
C1_power = power['C1']
C2_power = power['C2']
C3_power = power['C3']
C4_power = power['C4']
C5_power = power['C5']
C6_power = power['C6']
C7_power = power['C7']
C8_power = power['C8']
C9_power = power['C9']
Einheit = power['Einheiten']

x = C0_power + (C1_power * Te)
y = (C2_power * Tc)
d = (C3_power * Te ** 2)
e =    (C4_power * Te * Tc)
z = (C5_power * Tc ** 2)
a =(C6_power * Te ** 3) + (C7_power * Te ** 2 * Tc)
b=(C8_power * Te * Tc ** 2)
c=(C9_power * Tc ** 3)
print(x+y+z+a+b+c+d+e , x , y ,d, e, z, a ,b,c)




C0_current= current['C0']
C1_current= current['C1']
C2_current= current['C2']
C3_current= current['C3']
C4_current= current['C4']
C5_current= current['C5']
C6_current= current['C6']
C7_current= current['C7']
C8_current= current['C8']
C9_current= current['C9']

C0_sucmassflow= sucmassflow['C0']
C1_sucmassflow= sucmassflow['C1']
C2_sucmassflow= sucmassflow['C2']
C3_sucmassflow= sucmassflow['C3']
C4_sucmassflow= sucmassflow['C4']
C5_sucmassflow= sucmassflow['C5']
C6_sucmassflow= sucmassflow['C6']
C7_sucmassflow= sucmassflow['C7']
C8_sucmassflow= sucmassflow['C8']
C9_sucmassflow= sucmassflow['C9']

for n in range(4):
    if n==0 :
        print('Ich bin die Cooling Capacity')
        for j in range(10):
            varname =  'C' +str(j)
            cp = coolcap[str(varname)]
            print(varname,'Cool' , cp)

    if n ==1:
        print('Ich bin die Power')
        for j in range(10):
            varname = 'C' + str(j)
            pw = power[str(varname)]
            print(varname,'power',pw)
    if n == 2:
        print('Ich bin die Current')
        for j in range(10):
            varname = 'C' + str(j)
            ct = current[str(varname)]
            print(varname, 'current', ct)
    if n ==3:
        print('ich bin der MassFlow')
        for j in range(10):
            varname = 'C' + str(j)
            mf = sucmassflow[str(varname)]
            print(varname,'Mass Flow', mf)

        #print('Die Cooling Capacity laut Hersteller liegt bei:' , round(coolerg,3)  , '[kW]' )
    n+=1


coolerg = Calculation(C0_cool, C1_cool, C2_cool, C3_cool, C4_cool, C5_cool, C6_cool, C7_cool, C8_cool, C9_cool)
print('Die Cooling Capacity laut Hersteller liegt bei:', round(coolerg,3)  , '[kW]'  , 'Te:' , Te , 'Tc:',Tc )
powererg= Calculation(C0_power,C1_power,C2_power,C3_power,C4_power,C5_power,C6_power,C7_power,C8_power,C9_power)
print('Die Power liegt bei:', round(powererg,3), '[kW]','Te:' , Te , 'Tc:',Tc)
currenterg = Calculation(C0_current,C1_current,C2_current,C3_current,C4_current,C5_current,C6_current,C7_current,C8_current,C9_current)
print('Die Current liegt bei:', round(currenterg,3), '[A]','Te:' , Te , 'Tc:',Tc)
massflowerg= Calculation(C0_sucmassflow ,C1_sucmassflow,C2_sucmassflow,C3_sucmassflow,C4_sucmassflow,C5_sucmassflow,C6_sucmassflow,C7_sucmassflow,C8_sucmassflow,C9_sucmassflow)
print('Der Suc Mass Flow liegt bei:', round(massflowerg,3), '[g/s]','Te:' , Te , 'Tc:',Tc)





