import matplotlib.pyplot as pt
ax = pt.axes(projection='3d')
#from mpl_toolkits import mplot3d
def in_ary(): #Function is used to take inpt from user in form of vector components
    print(" i\u0302 : ",end='')
    x=float(input())
    print(" j\u0302 : ",end='')
    y=float(input())
    print(" k\u0302 : ",end='')
    z=float(input())
    return [x,y,z]
def dround(l): #Tailormade fucntion to round off the values in a list
    for i in range(len(l)):
        l[i]=round(l[i],4)
    return l
def lmomentum(v,m): #Function to calculate linear momentum, returns a list containing linear momentum of all particles
    lm=[]           #Credits: AKARSH CHAURASIA
    for j in range(3):
        lm.append(m*v[j])
    return lm
def energy(v,m): #Function to calculate energy, which uses KE equation and returns a scalar energy value
    e=0          #Credits: ANURODH PANCHOLI
    vm=0
    for j in range(3):
        vm+=(v[j]**2)
    e=(0.5)*m*vm
    return e
def force(m,a): #Function to calculate force on the particles using Newton's Law
    f=[]        #Credits: DHANANCHEZIYAN
    for i in range(3):
        f.append(m*a[i])
    return f
def com(m,p):#Function to calculate the centre of mass of all particles
    c=[] #=> Credits: PIYUSH KARMHE, Akash P
    n=0.0
    d=0.0
    for i in range(3):
        for j in range(len(m)):
           n+=(m[j]*p[j][i])
           d+=m[j]
        c.append(n/d)
    return c
def dis(cm,p):#Function to calculate the position vector in accordance with COM
    r=[]
    for i in range(3):
        r.append(p[i]-cm[i])
    return(r)
def dot(x,y):#Function to calculate the DOT PRODUCT of 2 Vectors(LISTS) 
    d=0 #=> Credits: PIYUSH KARMHE
    for i in range(3):
        d+=x[i]*y[i]
    return d
def cross(x,y):#Function to calculate the CROSS PRODUCT of 2 Vectors(LISTS)
    cp=[] #=> Credits: PIYUSH KARMHE, Akash P
    cp.append((x[1]*y[2])-(x[2]*y[1]))
    cp.append((x[0]*y[2])-(y[0]*x[2]))
    cp.append((x[0]*y[1])-(y[0]*x[1]))
    return cp
def amomentum(p,cm,lm):#Function to calculate the angular momentum of the particle w.r.t COM of system,returns a list of components
    am=[]              #Credits: VINIT L
    r=dis(cm,p)
    am=cross(r,lm)
    return am
def torque(p,cm,f):#Function to calculate the torque on the particle w.r.t COM of the system, returns a list with components
    tor=[]         #Credits: Ujjwal
    r=dis(cm,p)
    tor=cross(r,f)
    return tor
def col(p,v,a,m,t):#Function which calclates the velocity and acceleration in case collision occurs between particles,it checks if 2 of them have collided ot not
    l=[]           #Here collision between only 2 pairs of particles are taken into consideration
    v1=[]          #Credits: AKASH P
    v2=[]
    for i in range(len(p)):
        for j in range(len(p)):
            if p[i] and p[j] not in l:
                if(p[i]==p[j]):
                    if(i == j):
                        continue
                    else:
                        u1,u2=v1[i],v2[j]
                        v1,v2 = colvel(m[i],m[j],v[i],v[j])
                        a[i]=colacc(u1,v1,t)
                        a[j]=colacc(u2,v2,t)
                        print("\n***Collision Between ",str(i+1)," and ",str(j+1),"***\n")
                        l.append(p[i])
                        l.append(p[j])
                        v[i],v[j]=v1,v2
    return v,a 
def colacc(u,v,t):#Function to calculate Acceleration after collision
    a=[]
    for i in range(3):
        a.append((v[i]-u[i])/t)
    return a
def colvel(m1,m2,vi1,vi2):#Function to calculate velocity after collision
    v1f=[]
    v2f=[]
    m_1=0.0
    m_2=0.0
    for i in range(3):
        m_1=(m1-m2)/(m1+m2)
        m_2=(2*m2)/(m1+m2)
        v1f.append(round((m_1*vi1[i]) + (m_2*vi2[i]),4))
        v2f.append(round((m_2*vi1[i]) + (m_1*vi2[i]),4))
    return v1f,v2f
def vp(vec):#Tailor made function to print the output in vector format(xi+yj+zk)
    str1=""
    str1=str(vec[0])+" i\u0302 + "+str(vec[1])+" j\u0302 + "+str(vec[2])+" k\u0302"
    return str1
def checkb(p,b,n):#Function to check if the particle postion excedes the given boundary condition
    f=0 #=> Credits: PIYUSH KARMHE
    t=0
    if b==[]:
        return p
    else:
        for i in range(n):
            for j in range(3):
                if p[i][j]<0:
                    t=-p[i][j]
                if t>b[j]:
                    p[i][j]=b[j]
                    f=1
    if f==1:
        print("\n******************Given Coordinates more that boundary******************")
        print("******************Coordinates altered according to boundary******************\n")
    return p
def bonc(p,v,a,b): #=> Credits: PIYUSH KARMHE
    t=0
    for j in range(3):
        if p[j]<0:
            t=-p[j]
        else:
            t=p[j]
        if t>b[j]:
            v[j]=-v[j]
            a[j]=-a[j]
            print("\n******************Particle Exceded Boundary******************\n")
            print("\n******************Calculating the reflection direction******************\n")
            break
    return v,a
def display(n,p,v,lm,e,f,am,tor):#Function to display all calculated values in the system
    print("\n****Object No: ",n,"****\n")
    print("Position :",vp(dround(p))," m"," Velocity :",vp(dround(v))," m/s")
    #print("Velocity :",vp(v)," m/s")
    print("Linear Momentum :",vp(dround(lm))," kg·m/s"," Angular Momentum :",vp(dround(am))," kg-m2/sec")
    print("Energy :",round(e,4)," J"," Force :",vp(dround(f))," N")
    #print("Force :",vp(f)," N")
    #print("Angular Momentum :",vp(am)," kg-m2/sec")
    print("Torque :",vp(dround(tor))," Nm\n")
    print("*******************")
#Array of size nX3 for taking the coordinates x,y and z of the quantity
#Takin Inputs=> Credits: DEV GAUTHAM
p=[]#Position
v=[]#Velocity
a=[]#Acceleration
m=[]#Mass
lm=[]#Linear Momentum
am=[]#Angular Momentum
f=[]#Force
tor=[]#Torque
e=0#Energy
cm=[]#centre of mass
b=[]
#Taking Total time Duration and Time step
print("****************************************************************************")
print(">>>>>>>>>>>>>>>>>>>>>>>>>>$Multi-Particle-Simulator$<<<<<<<<<<<<<<<<<<<<<<<<<<")
print("                           ^^^^^^^^^^^^^^^^^^^^^^^^\n\n")
T=float(input("Give Time Duration (s): "))
t=float(input("Give the Time Steps (s): "))
cb=input("Want to give boundary condition ?(Y/N) : ")
if cb=='y' or cb=='Y':
    b.append(float(input("Give Length : ")))
    b.append(float(input("Give Breadth : ")))
    b.append(float(input("Give Height : ")))
n=int(input("Give the no Obj : "))
#Taking Position, Velocity, Acceleration and Mass
print("Give the i\u0302 + j\u0302 + k\u0302  of quantities")
for i in range(n):
    print("\n*******For Object : ",str(i+1),"*******\n")
    print("Give Mass : ",end='')
    m.append(float(input()))
    print("Give Pos : ")
    p.append(in_ary())
    print("Give Vel : ")
    v.append(in_ary())
    print("Give Acc : ")
    a.append(in_ary())
td=0.0
if cb=='y' or cb=='Y':
    p=checkb(p,b,n)
for i in range(n):
    ax.scatter(p[i][0],p[i][1],p[i][2],'k')
print("\n******************Running Simulation******************\n")
#print("Time : ",round(td,4),"Position : ",vp(dround(p))," Velocity : ",v," Acceleration : ",a)
#Running the Simulator #T t td
#MAIN SIMULATOR STARTS=> Credits: PIYUSH KARMHE
while td<=T:
    td+=t
    print("\n*******************At Time : ",round(td,4)," s*******************\n")
    cm=com(m,p)#Center of mass
    print("*******Centre of Mass : ",vp(dround(cm)))
    for j in range(n):
        for i in range(3):
            #Position and Velocity Calculation
            #s=ut+at^2
            p[j][i]=p[j][i]+((v[j][i]*t)+((0.5)*(a[j][i]*(t**2))))
            #v=u+at
            v[j][i]=v[j][i]+(a[j][i]*t)
        #Functions
        ax.scatter(p[j][0],p[j][1],p[j][2],'k')
        lm=lmomentum(v[j],m[j])
        e=energy(v[j],m[j])
        f=force(m[j],a[j])
        am=amomentum(p[j],cm,lm)
        tor=torque(p[j],cm,f)
        #Output Function
        display(j+1,p[j],v[j],lm,e,f,am,tor)
        if cb=='y' or cb=='Y':
            v[j],a[j]=bonc(p[j],v[j],a[j],b) #Boundry Condition
    v,a = col(p,v,a,m,t)#Collision
    print("\n*******************END of Instance*******************\n")
print("\n******************Stopped Simulation******************\n")
pt.show() #=> Credits: Akash P