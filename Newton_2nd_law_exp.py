from prettytable import PrettyTable
def mean(data):
  n = len(data)
  mean = sum(data) / n
  return mean
def variance(data):   
  n = len(data)   
  mean = sum(data) / n   
  deviations = [(x - mean) ** 2 for x in data]   
  variance = sum(deviations) / n
  return variance 
def cal(m,M,u,t,s):
    nf = (m*(9.8))-(u*M*(9.8))
    tm = m+M
    macc = nf/tm
    cacc = (2*s)/(t**2)
    er=((macc-cacc)/cacc)*100 
    return round(nf,2),round(tm,2),round(macc,2),round(cacc,2),er,round(s,2) 
print("Newton's Second Law of motion Simulator : ")
n=input("For how many data set u want to do simulation(Single/Multiple) : ")
print("Set 1 : ")
m=float(input("Hanging wt in g: "))
if n=='M' or n=='m':
    chm=input("How u want to enter it(Manually/Keep Constant/Auto Increment):")
    if chm=='a' or chm=='A':
        ma=float(input("Give Steps to increment in g : "))
M=float(input("Sledge wt in g: "))
if n=='M' or n=='m':
    chM=input("How u want to enter it(Manually/Keep Constant/Auto Increment):")
    if chM=='a' or chM=='A':
        Ma=float(input("Give Steps to increment in g : "))
u=float(input("Friction coefficient wt : "))
if n=='M' or n=='m':
    chu=input("How u want to enter it(Manually/Keep Constant/Auto Increment):")
    if chu=='a' or chu=='A':
        ua=float(input("Give Steps to increment in : "))
s=float(input("Distance in cm: "))
if n=='M' or n=='m':
    chs=input("How u want to enter it(Manually/Keep Constant/Auto Increment):")
    if chs=='a' or chs=='A':
        sa=float(input("Give Steps to increment in cm : "))
        sa=sa/100
s=s/100
t=float(input("Time wt in s: "))
if n=='M' or n=='m':
    print("Will have to enter Manually")
h = ["S.No","m","M","uk","T","EF(N)","Total Mass","Mea Acc","Cal Acc","Error%"]
ler = []
nf,tm,macc,cacc,er,s=cal(m,M,u,t,s)
ler.append(er)
d = [1,m,M,u,t,nf,tm,macc,cacc,(str(round(er,2))+"%")]
ch=''
myTable = PrettyTable(h)
myTable.add_row(d) 
i=1
while ch=='':
    i+=1
    print("Set ",str(i)," : ")
    #m
    if chm=='a' or chm=='A':
        m+=ma
    elif chm=='m' or chm=='M':
        m=float(input("Hanging wt in g: "))
    else:
        pass    
    #M
    if chM=='a' or chM=='A':
        M+=Ma
    elif chM=='m' or chM=='M':
        M=float(input("Sledge wt in g: "))
    else:
        pass
    #u
    if chu=='a' or chu=='A':
        u+=ua
    elif chu=='m' or chu=='M':
        u=float(input("Friction coefficient wt : "))
    else:
        pass 
    #s
    if chs=='a' or chs=='A':
        s+=sa
    elif chs=='m' or chs=='M':
        s=float(input("Distance in cm: "))
        s=s/100
    else:
        pass   
    t=float(input("Time wt in s: "))
    nf,tm,macc,cacc,er,s=cal(m,M,u,t,s)
    d = [i,m,M,u,t,nf,tm,macc,cacc,(str(round(er,2))+"%")] 
    myTable.add_row(d)
    ler.append(er)
    ch=input("To add more Press Enter else P to Print Table:")
    if ch!='':
        print("Ok All data set entered.")
        break
print(myTable)
print("\nMean Error : ",round(mean(ler),2))
print("Error Varience: ",round(variance(ler),2))
print("Error Standard Deviation: ",round((variance(ler)**(0.5)),2))