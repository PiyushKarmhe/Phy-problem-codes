import matplotlib.pyplot as plt
import numpy as np
def cal(tp,p,coff):
    s=0
    for i in range(p+1):  
        s+=coff[i]*(tp**i)
    return s
print("Simple Polynomial Eqaution of Linear Motion solver")
qty=input("Give name of the Quantity entering(v/x/a) : ")
p=int(input("Give the Highest power of the polynomial equation : "))
coff=[]
for i in range(p+1):
    print("Give the Coefficient of t^",i,end="")
    coff.append(float(input(" : ")))
print("So, ",qty," = ",end="")
for i in range(p,-1,-1):
    if coff[i]>0:
        print("+",coff[i],"t^",i,end=" ")
    else:
        print(coff[i],"t^",i,end=" ")
t=float(input("\nGive Time : "))
if qty=='V' or qty=='v':
    dqty='a'
    iqty='x'
    l='Velocity'
elif qty=='a' or qty=='A':
    dqty='J'
    iqty='V'
    l='Acceleration'
elif qty=='x' or qty=='X':
    dqty='V'
    iqty='N/A'
    l='Displacement' 
dq=0
iq=0 
for i in range(p+1): 
    if i==0: 
        dq+=coff[i]*(t**(i))*(i)
    else:
        dq+=coff[i]*(t**(i-1))*(i)
for i in range(p+1): 
    if i==0: 
        iq+=coff[i]*(t**(i+1))
    else:
        iq+=coff[i]*(t**(i+1))/(i+1)
if qty=='x' or qty=='X':
    print(dqty,"=",dq)
else:
    print(dqty,"=",dq,"\n",iqty," = ",iq)
tp = np.arange(0., 5., 0.2)
plt.plot(tp,cal(tp,p,coff))
plt.ylabel(l)
plt.xlabel('Time')
plt.show()