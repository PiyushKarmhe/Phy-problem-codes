import math
print("Equations of Rotation Motion Problem Solver : ")
v=u=a=t=s=r='a'
f=0
while f<3:
    print("Choose the Quantities u have and give it's value in S.I Units Only")
    print("\n1.Final (Linear/Degree/Radian/RPM)Velocity\n2.Initial (Linear/Degree/Radian/RPM)Velocity\n3.(Linear/Angular/Radian/RPM^2)Acceleration\n4.Time\n5.(Degree/Radian/Revolutions)Angular Displacement\n6.Radius\n7.Submit")
    ch=int(input("Choice : "))
    if ch==1:
        ch=input("Final Velocity in (Linear/Degree/Radian/RPM(a)) : ")
        if ch=='L' or ch =='l':
            if r!='a':
                v=input("Give the Final Linear Velocity : ")
                v=float(v)
                v=v/r
                f+=1
            else:
                print("Please provide Radius First!!") 
        elif ch=='d' or ch =='D':
            v=input("Give the Final Angular Velocity in  deg/s : ")
            v=float(v)
            f+=1  
        elif ch=='r' or ch =='R':
            v=input("Give the Final Angular Velocity in  Rad/s : ")
            v=float(v)
            v=(v*math.pi)/180
            f+=1            
        else:
            v=input("Give the Final Angular Velocity in RPM : ")
            v=float(v)
            v=v*6
            f+=1
    elif ch==2:
        ch=input("Initial Velocity in (Linear/Degree/Radian/RPM(a)) : ")
        if ch=='L' or ch =='l':
            if r!='a':
                u=input("Give the Initial Linear Velocity : ")
                u=float(u)
                u=u/r
                f+=1
            else:
                print("Please provide Radius First!!") 
        elif ch=='d' or ch =='D':
            u=input("Give the Initial Angular Velocity in  deg/s : ")
            u=float(u)
            f+=1  
        elif ch=='r' or ch =='R':
            u=input("Give the Initial Angular Velocity in  Rad/s : ")
            u=float(u)
            u=(u*math.pi)/180
            f+=1            
        else:
            u=input("Give the Initial Angular Velocity in RPM : ")
            u=float(u)
            u=u*6
            f+=1
    elif ch==3:
        ch=input("Acceleration in (Linear/Deg/Radian/RPM^2(a)) : ")
        if (ch=='L' or ch =='l') and r!='a':
            if r!='a':
                a=input("Give the Linear Acceleration : ")
                a=float(a)
                a=a/r
                f+=1
            else:
                print("Please provide Radius First!!")
        elif ch=='D' or ch =='d': 
            a=input("Give the Angular Acceleration in deg/s^2 : ")
            a=float(a)
            f+=1  
        elif ch=='R' or ch =='r': 
            a=input("Give the Angular Acceleration in Rad/s^2 : ")
            a=float(a)
            a=a*57.3
            f+=1          
        else:
            a=input("Give the Angular Acceleration in RPM^2 : ")
            a=float(a)
            a=a*0.1
            f+=1
    elif ch==4:
        t=input("Give the Time : ")
        t=float(t)
        f+=1
    elif ch==5:
        ch=input("Angular Displacement in (Degree/Radian/Revolutions(a)): ")
        if ch=='d' or ch=='D':
            s=input("Give Angular Displacement in Degrees : ")
            s=float(s)
        elif ch=='r' or ch=='R':
            s=input("Give Angular Displacement in Radian : ")
            s=float(s)
            s=(s*math.pi)/180
        else:
            s=input("Give Angular Displacement in RPM : ")
            s=float(s)
            s=s*360
        f+=1
    elif ch==6:
        r=input("Give the Radius : ")
        r=float(r)
    elif ch==7:
        if (f<3):
            print("Insufficient data!!\nPlease Provide ",3-f," more!!")
            if r!='a':
                print("Other Than Radius!!")           
        else:
            break; 
    else:
        print("Invalid Input!!\nRetry!!") 
if v=='a' and s=='a':
    v = u+(a*t)
    s = (u*t)+(0.5*a*(t**2))
    print("\n Final Angular Velocity : ",v," deg/s Angular Displacement : ",s,"deg")
elif v=='a' and t=='a':
    if a==0:
        print("Not Possible Angular Acceleration can't be 0 deg/s^2 in this case")
    else:
        v = ((u**2)+(2*a*s))**(0.5)
        t = (v-u)/a
        print("\n Final Angular Velocity : ",v," deg/s Time : ",t," s")
elif v=='a' and a=='a':
    if t==0:
        print("Not Possible Time can't be 0 s in this case")
    else:
        a=((s-(u*t))*2)/(t**2)
        v=u+(a*t)
        print("\n Final Angular Velocity : ",v," deg/s Angular Acceleration : ",a," deg/s^2")
elif v=='a' and u=='a':
    if t==0:
        print("Not Possible Time can't be 0 s in this case")
    else:
        u=(s-(a*(t**2))/2)/t
        v=u+(a*t)
        print("\n Final Angular Velocity : ",v," deg/s Initial Angular Velocity : ",u," deg/s")
elif u=='a' and a=='a':
    if t==0:
        print("Not Possible Time can't be 0 s in this case")
    else:
        a=((2*v*t)-(2*s))/(t**2)
        u=v-(a*t)
        print("\n Initial Angular Velocity : ",u," deg/s Angular Acceleration : ",a," deg/s^2")
elif u=='a' and t=='a':
    if a==0:
        print("Not Possible Angular Acceleration can't be 0 deg/s^2 in this case")
    else:
        u=((v**2)-(2*a*s))**(0.5)
        t=(v-u)/a
        print("\n Initial Angular Velocity : ",u," deg/s Time : ",t," s")
elif u=='a' and s=='a':
    if a==0:
        print("Not Possible Angular Acceleration can't be 0 deg/s^2 in this case")
    else:
        s=(v*t)-(a*(t**2))/2
        u=v-(a*t)
        print("\n Initial Angular Velocity : ",u," deg/s Angular Displacement : ",s,"deg")
elif a=='a' and t=='a':
    if s==0:
        print("Not Possible Angular Displacement can't be 0deg in this case")
    elif a==0:
        print("Not Possible Angular Acceleration can't be 0 deg/s^2 in this case")
    else:
        a=((v**2)-(u**2))/(2*s)
        t=(v-u)/a
        print("\n Angular Acceleration : ",a," deg/s^2 Time : ",t," s")
elif a=='a' and s=='a':
    if t==0:
        print("Not Possible Time can't be 0 s in this case")
    else:
        s=((v+u)*t)/2
        a=(v-u)/t
        print("\n Angular Acceleration : ",a," deg/s^2 Angular Displacement : ",s,"deg")
else :
    if a==0:
        print("Not Possible Angular Acceleration can't be 0 deg/s^2 in this case")
    else:
        t=(v-u)/a
        s=((v+u)*t)/2
        print("\n Angular Displacement : ",s,"deg Time : ",t," s")
if r=='a':
    print("If provided Radius More calculation could be made.")
    ch=input("Want to give Radius(Y/N) : ")
    if ch=="y" or ch=="Y":
        r=input("Give Radius : ")
        r=float(r)
    else:
        print("Okay")
if r!='a':
    print("Final Linear velocity : ",v*r," m/s")
    print("Initial Linear velocity : ",u*r," m/s")
    print("Linear Acceleration : ",a*r," m/s^s")
    print("Linear Displacement: ",((2*math.pi*r)*(s/360))," m/s")
print("Thank You!!")