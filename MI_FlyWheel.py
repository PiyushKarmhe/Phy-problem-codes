import math
print("Moment of Inertia of Fly Wheel Calculator : ")
m = float(input("Enter mass of suspended weight : "))
suff = input("Unit : ")
if suff == 'g' or suff == 'G':
    m = m/1000
r = float(input("Enter the radius of axle : "))
suff = input("Unit : ")
if suff == 'cm' or suff == 'CM':
    r = r/100
n = float(input("Enter the no of chord windings: "))
h = float(input("Enter the Height of Supended Mass :"))
suff = input("Unit : ")
if suff == 'cm' or suff == 'CM':
    h = h/100
N = float(input("Enter the no of Revolutions: "))
t = float(input("Enter time taken for N revolutions: "))
g=9.8
omega = (4*math.pi*N)/t
MI = (N*m)/(N+n)*(((2*g*h)/(omega**2))-(r**2))
print("Average angular velocity is: ",omega," rad/s")
print("The MI of FlyWheel is: ",MI," kg/m^2")