from sinus import make_sin, make_sin_vect, sinusoïde
from utils import decoration, plot
import math
import matplotlib.pyplot as plt

#---------------------------------
def deux_sin_vect(a=1.25, ph=0, f=50, fe=500.0, d=0.040, a1=0.5, ph1=math.pi, fe1=1000):
    tp_b, sig_b = make_sin_vect(a=a, f=f, ph=ph, fe=fe, d=d)
    tp_r, sig_r = make_sin_vect(a=a1, f=f, ph=ph1, fe=fe1, d=d)
    return tp_b, sig_b, tp_r, sig_r

#---------------------------------
def deux_sin(a=1.25, ph=0, f=50, fe=500.0, d=0.040, a1=0.5, ph1=math.pi, fe1=1000):
    tp_b, sig_b = make_sin(a=a, f=f, ph=ph, fe=fe, d=d)
    tp_r, sig_r = make_sin(a=a1, f=f, ph=ph1, fe=fe1, d=d)
    return tp_b, sig_b, tp_r, sig_r 

tp_b, sig_b, tp_r, sig_r = deux_sin_vect()

fig, ax = plt.subplots()
plot(ax, tp_b, sig_b, 'ob', label='s1 : a=1.25, f=50Hz, ph=0, fe=500Hz')
plot(ax, tp_r, sig_r, 'or', label='s2 : a=0.5, f=50Hz, ph=pi, fe=1000Hz')
decoration(ax, "sinusoïde")
plt.show()



    

    





