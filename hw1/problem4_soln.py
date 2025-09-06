# !sudo apt-get install texlive-full
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({"text.usetex": True})

FONTSIZE = 16

def signal1(time):
    y = np.zeros(time.shape)
    for i, t in enumerate(time):
        if t >= 0:
            y[i] = (np.sin(t))
    return y

def signal2(time):
    y = np.zeros(time.shape)
    for i, t in enumerate(time):
        if t >= 0:
            y[i] = (np.exp(-1.*t))*(1. - 2.*t)
    return y

t = np.linspace(-3, 22, 1000)
y1 = signal1(t)
y2 = signal2(t)

fig, ax = plt.subplots(1,1,figsize=(10, 6))

ax.plot(t, y1, linewidth=5,color="blue",label=r"$\sin(t)$")
ax.plot(t, y2, linewidth=5,color="orange",label=r"$e^{-t}(1 - 2t)$")

fig.suptitle(
    r'Plot of signals', 
    fontsize=FONTSIZE+2
)
ax.set_xlabel(r'$t$', fontsize=FONTSIZE)
ax.set_ylabel(r'$y$', fontsize=FONTSIZE)
ax.grid(True)
ax.axhline(y=0, color='black', linestyle='-', alpha=1)
ax.axvline(x=0, color='black', linestyle='-', alpha=1)
ax.set_xlim(-2, 21)
ax.tick_params(axis='both', which='major', labelsize=FONTSIZE)
ax.legend(framealpha=1.0)
plt.savefig('q4_soln.png')
plt.show()
