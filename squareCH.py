from sinus import decoration 
import math
import matplotlib.pyplot as plt

def make_square(a=3, f=50.0, fe=1000.0, nT=2):
    omega = 2 * math.pi * f
    te=1/fe
    T=1/f
    d=nT*T
    NMAX=int(d*fe)
    n = 0
    sig_t=[]
    sig_s=[]
    while n < NMAX:
        t = te * n
        sig_t.append(t)
        if math.sin(omega * t) >= 0:
            sig_s.append(a)
        else:
            sig_s.append(-a)
        n = n + 1

    return sig_t, sig_s 

sig_t, sig_s = make_square()

if __name__ == "__main__":
    fig, ax = plt.subplots()
    ax.plot(sig_t, sig_s, 'b-', label='a=3, f=50Hz, fe=1000Hz')
   
ax.grid()
decoration(ax, "Un carre")
ax.legend()
plt.show()





