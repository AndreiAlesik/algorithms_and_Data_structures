import math
import numpy as np
import matplotlib.pyplot as plt
import io
import base64

def fig_to_base64(fig)Ж
    img = io.BytesIO()
    fig.savefig(img, format='png',
                bbox_inches='tight')
    img.seek(0)

    return base64.b64encode(img.getvalue())

encoded = fig_to_base64(fig)
my_html = '<img src="data:image/png;base64, {}">'.format(encoded.decode('utf-8'))
Alpha=1.5
Beta= 0.035
Qd=0.05 #natezenie doplywu
Qdmax=0.05
hmin=0
hmax=10
tsym=24*1000
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
fig = plt.subplots()
for i in range(1, int(tsym/Tp)):
    h.append(1/Alpha*Tp*((-1)*Beta*math.sqrt(h[-1])+Qd)+h[-1])
    #print(h[i], " ", i)
    e.append(hd - h[i])  # hd wartosc docelowa
    if (i>1):
        u = kp * (e[i] + Tp / Ti * sum(e) + Td / Tp * (e[-1] - e[-2]))
        Qd = (Qdmax / umax) * u
        #print(Qd)


x = np.linspace(0, tsym/Tp, len(h))
y=lambda x: h
plt.plot(x, y(x))
plt.show()

    # hd wartosc docelowa
    # sum(e)- suma z listy
    # delta e = e[i - 1] - e[i - 2]
