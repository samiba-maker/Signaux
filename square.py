from utils import make_sig, plot, decoration
import math
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal 
#---------------------------------
def make_square_vect(a=3.0, f=50.0, fe=1000.0, nT=2, ph=0):
    d = nT / f
    te = 1/fe
    omega = 2 * math.pi * f
    sig_t = np.arange(0, d, te)
    sig_s = np.where(a*np.sin(omega * sig_t + ph) >= 0, a, -a) 
    return sig_t, sig_s

#---------------------------------
def make_square_vect_sci(a=3.0, f=50.0, fe=1000.0, nT=2, ph=0):
    d = nT / f
    te = 1/fe
    omega = 2 * math.pi * f
    sig_t = np.arange(0, d, te)
    sig_s = a * signal.square(omega * sig_t + ph)
    return sig_t, sig_s

#---------------------------------
def square(t, a, f, ph):
    omega = 2 * math.pi * f
    if a * math.sin(omega * t + ph) >= 0:
            return a
    else:
            return -a

def make_square(a=3.0, f=50.0, fe=1000.0, nT=2):
    return make_sig(square, a=a, f=f, fe=fe, nT=nT)

if __name__ == "__main__": 
    sig_t, sig_s = make_square_vect()

    fig, ax = plt.subplots()
    plot(ax, sig_t, sig_s, format="bo-", label="a=3, f=50, fe=1000")
    decoration(ax, "Un carré")
    plt.show()