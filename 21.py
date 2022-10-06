import math
A=1.5
beta= 0.035
Qd=0.05
Qdmax=0.05
hmin=0
hmax=10
tsym=24*3600
Tp=0.1
h=[0.0] #pierwszy index rowny 0
kp=0.015
Ti=0.75
Td=0.25
umin=0
umax=10
u=[]
hd=1.5
e=[hd]
for i in range(1,int(tsym/Tp)):
    #h[-1] ostatnia wartosc w liscie
    h.append(1/A*Tp*((-1)*beta*math.sqrt(h[-1])+Qd)+h[-1])
    print(h[i]," ",i)
    e.append(hd-h[i]) #hd wartosc docelowa
    #sum(e)- suma z listy
    #delta e = e[i - 1] - e[i - 2]
    if(i>1):
        u=kp*(e[i]+Tp/Ti*sum(e)+Td/Tp*(e[-1]-e[-2]))
        Qd=(Qdmax/umax)*u
        #print(Qd)