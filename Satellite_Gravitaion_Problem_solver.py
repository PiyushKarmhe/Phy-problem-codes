print("Satellite Gravitaion Problem solver")
m=float(input("Give the mass of the Satellite : "))
a=float(input("Give the altitude of the Satellite : "))
G=6.67*(10**(-11))
me=5.96*(10**24)
r=8.9*(10**6)
v = ((G*me)/r)**(0.5)
print("Velocity : ",v," m/s")
ke = (0.5)*(m*(v**2))
print("Kinetic Energy : ",ke," J")
t = 2*3.14*(((r**3)/(G*me))**(0.5))
print("Time period : ",t," s")