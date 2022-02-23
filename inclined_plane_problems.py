import math
print("Inclined Plane Problem Solver:-")        
print("         /|")
print("    /\ f/ |")
print("   /m \/  |")
print("   \  /   |")
print("  a \/u   |")
print("    /     |")
print("   /      |")
print("  /)0     |")
print("TTTTTTTTTTTTTT")
m=float(input("Give Mass(m) in kg :"))
o=float(input("Give Theta(0) in Degree :"))
o= (o*math.pi)/180
u=float(input("Give Mue(u) : "))
ch=input("f or a ? : ")
if ch =='f' or ch=='F':
    f=float(input("Give Required Force(f) in N :"))
    if f>=0:
        u=-u
    a=(f-(m*(9.8)*math.sin(o))-(u*m*(9.8)*math.cos(o)))/m
    print("Acceleration : ",a," m/s^2")
else:
    a=float(input("Give Required Acceleration(a) in m/s^2 :"))
    if a>=0:
        u=-u
    f= m*(a+((9.8)*math.sin(o))+(u*(9.8)*math.cos(o)))
    print("Force : ",f," N")