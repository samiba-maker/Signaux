import matplotlib.pyplot as plt
import math

#---------------------------------
def plot(ax, inx, iny, format, label):
    ax.plot(inx, iny, format, label=label)

#---------------------------------
def decoration(ax, xlabel, ylabel, title):
    ax.set(xlabel=xlabel, ylabel=ylabel)           
    ax.set(title=title)    
    ax.grid()
    ax.legend()
    plt.show()
    
#---------------------------------
def make_sig(formule, a, f, fe, nT, ph):
    d = nT / f 
    NMAX = int(d * fe)
    te = 1.0 / fe
    sig_t = []
    sig_s = []
    n = 0
    while n < NMAX:
        t = te * n
        sig_t.append(t)
        s = formule(t,a,f,ph)
        sig_s.append(s)
        n = n + 1
    return sig_t, sig_s


