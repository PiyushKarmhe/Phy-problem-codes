import matplotlib.pyplot as plt
print("Simple Staright Line Linear Motion Graph Solver")
print(" |                 d /\ ")
print(" |      b__________c/  \ ")
print(" |      /           |   \ ")
print(" |     /            |    \ ")
print(" |    /             |     \ ")
print(" |   /              |      \ ")
print(" |  /               |       \ ")
print(" | /                |        \ ")
print("a|/_________________|_________\e______")
print("Give the Coordinates of Points Like a,b,c,d,e")
ch='y'
c=1
x=[]
y=[]
a=[]
s=[]
print("Select the Graph")
print("1.A-T\n2.V-T")
chh=int(input("Choice : "))
if chh==1:
    q1="Jerk"
    q2="Velocity"
    u1="m/s^3"
    u2="m/s"
    ya="Acceleration"
else:
    q1="Acceleration"
    q2="Displacement"
    u1="m/s^3"
    u2="m"
    ya="Velocity"
while ch=='y'or ch=='Y':
    print("For Point no. ",c)
    t = float(input("Give X: "))
    x.append(t)
    t = float(input("Give Y: "))
    y.append(t)
    c+=1
    ch=input("To continue enter Y :")
for i in range(len(x)-1):
    if y[i]==0 or y[i+1]==0:
        d=0.5*(x[i+1]-x[i])*abs(y[i+1]-y[i])
    elif y[i]==y[i+1]:
        d=y[i]*(x[i+1]-x[i])
    else :
        d=((y[i]+y[i+1])*(x[i+1]-x[i]))/2
    acc=(y[i+1]-y[i])/(x[i+1]-x[i])
    print("From Point no.",i+1," to Point no.",str(i+2)," ",q1," = ",acc," ",u1," and ",q2," = ",d," ",u2)
    a.append(acc)
    s.append(d)
d=0
for j in s:
    d+=j
print("Total ",q2," From Point no.",0," to Point no.",i+2," is ",d," ",u2) 
plt.plot(x,y,'bo',x,y,'k')
plt.ylabel(ya)
plt.xlabel('Time')
plt.show()  