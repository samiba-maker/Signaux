import math
import matplotlib.pyplot as plt
import numpy as np 

def deux_sin(a=1.25, ph=0, f=50, fe=500.0, d=0.040, a1=0.5, ph1=math.pi, fe1=1000):
    te = 1/fe
    te1 = 1/fe1
    omega=2 * math.pi * f
    n = 0
    n1 = 0
    N =int(d*fe)
    N1=int(d*fe1)
    sbx = []
    sby = []
    srx = []
    sry = []
    while n < N:
        t = te * n
        sbx.append(t)
        sby.append(a*math.sin(omega * t + ph))
        n = n + 1 
    while n1 < N1:
        t = te1 * n1
        srx.append(t)
        sry.append(a1 * math.sin(omega * t + ph1))
        n1 = n1 + 1
    return sbx, sby, srx, sry

sbx, sby, srx, sry = deux_sin()
fig, ax = plt.subplots()
ax.plot(sbx, sby, 'ob', label = ' s1 : a=1.25, f=50, ph=0')
ax.plot(srx, sry, 'or', label = 's2 : a = 0.5, f=50, ph=pi')
ax.legend()
ax.grid()
plt.show()


