from utils import make_sig, plot, decoration
import math
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

#---------------------------------
def make_saw_vect(a=3.0, f=50, fe=1000.0, d=0.04):
    T = 1/f
    te = 1/fe
    sig_t = np.arange(0, d, te)
    sig_s = 2 * a * (sig_t/T - np.floor(sig_t/T) - 1/2)
    return sig_t, sig_s

#---------------------------------
def make_saw_vect_sci(a=3.0, f=50, fe=1000.0, d=0.04, ph=0):
    omega = 2*math.pi*f	
    T = 1/f
    te = 1/fe
    sig_t = np.arange(0, d, te)
    sig_s = a * signal.sawtooth(omega * sig_t + ph)
    return sig_t, sig_s

#---------------------------------
def saw(t, a, f):
    T = 1/f
    return 2 * a * (t/T - math.floor(t/T) - 1/2)

#---------------------------------
def make_saw(a=3.0, f=50.0, fe=1000.0, nT=2):
    return make_sig(saw, a=a, f=f, fe=fe, nT=nT)

if __name__ == "__main__":
    sig_t, sig_s = make_saw_vect()

    fig, ax = plt.subplots()
    plot(ax, sig_t, sig_s, format="bo-", label="a=3, f=50.0, fe=1000.0")
    decoration(ax, "Une dent de scie")
    plt.show()






