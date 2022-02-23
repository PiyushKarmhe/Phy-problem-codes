import math
print("Maximum speed along a ciruclar road calculator : ")
r=float(input("Give the Radius (r) : "))
u=float(input("Give the Mue (u) : "))
print("Vmax = sqrt(urg)")
g=9.8
v=(u*r*g)**(0.5)
print("Maximum Allowed Speed : ",v," m/s")
a=(v**2)/r
print("Cars's Acceleration : ",a," m/s^2")
print("Direction of Acceleration : ",math.atan(a)," Deg from tangent at that point")