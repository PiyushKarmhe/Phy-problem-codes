print("Wien's Displacement Law : ")
t = float(input("Give Temperature : "))
tu = input("Unit (°F/°C/K): ")
if tu =='f' or tu=='F':
    tf = t
    tc = (t - 32)*(5/9) 
    tk = tc + 273.15
elif tu=='C' or tu=='c':
    tc = t
    tf = (t*(9/5))+32
    tk = tc + 273.15
else:
    tk = t
    tc = tk - 273.15
    tf = (tc*(9/5))+32
lm = 2.898e-3/tk
lnm = lm * 10e-9
lu = lm * 10e-6
Ej = ((6.626e-34)*(2.98e8))/lm
Eev = Ej/1.6022e-19
tc ="{:e}".format(tc)
tf ="{:e}".format(tf)
tk ="{:e}".format(tk)
lm ="{:e}".format(lm)
lnm ="{:e}".format(lnm)
lu ="{:e}".format(lu)
Eev ="{:e}".format(Eev)
Ej ="{:e}".format(Ej)
print(" Temperature = ",tc,"°C = ",tf,"°F = ",tk,"K")
print(" Lambda Peak = ",lm," m = ",lnm," nm = ",lu," um")
print(" Quantum energy = ",Eev," eV = ",Ej," J")