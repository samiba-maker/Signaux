import math
import matplotlib.pyplot as plt 
import numpy as np
from utils import make_sig, decoration, plot

#---------------------------------
def make_sin_vect(a=1.0, f=440.0, fe=8000.0, ph=0, d=1):
    omega = 2*math.pi*f	
    te = 1/fe
    sig_t = np.arange(0, d, te)
    sig_s = a * np.sin(omega * sig_t + ph)
    return sig_t, sig_s

#---------------------------------
def sin(t, a, f, ph):
    omega = 2 * math.pi * f
    return a*math.sin(omega * t + ph)

#---------------------------------
def make_sin(a=1.0, f=440.0, fe=8000.0, nT=2.5, ph=0):
    return make_sig(sin, a=a, f=f, fe=fe, nT=nT, ph=ph)

#---------------------------------
if __name__ == "__main__":
    fig, ax = plt.subplots()

    sig_t, sig_s = make_sin()
    plot(ax, sig_t, sig_s, format ='-ob', label = "a=1, f=5 Hz, fe=8000 Hz")
    decoration(ax,"Temps (s)", "Voltage (V)", "Sinusoïde")
    

