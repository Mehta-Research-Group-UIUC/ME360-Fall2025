import numpy as np 
import matplotlib.pyplot as plt

T = 30.
Delta = 0.2
ITER = int(T/Delta)
a = .1
b = 0.

def h(t,a=a): # impulse reponse
	if t < 0.:
		return 0.
	else:
		return np.exp(-a*t) 


def u(t): # input function u(t) = sin(t) * u_0(t)
	if t < 0.:
		return 0.
	else:
		return np.sin(t)

#### method of convolution
u_s = np.zeros(ITER)
h_s = np.zeros(ITER)

for n in range(ITER):
	u_s[n] = u(n * Delta)  
	h_s[n] = h(n * Delta)  


y_s = np.zeros(ITER)
	
for n in range(ITER):
	c = 0.  # Initialize the summation variable
	for m in range(n + 1):
		c += Delta * h_s[n - m] * u_s[m]  
	y_s[n] = c

##### finite difference method
y = np.zeros(ITER)

u = np.sin(Delta*np.arange(ITER-1))

for iters in range(ITER-1):
	y[iters+1] = y[iters] + (-a*y[iters] + u[iters])*Delta



##### analytical solution

time = np.arange(ITER)*Delta
y_ana = (1/(1 + a**2))*(a*np.sin(time) - np.cos(time) + np.exp(-a*time))

f1,axs = plt.subplots(1,1)
axs.plot(np.arange(0,ITER)*Delta, y_s,label="convolution",ls="dashed")
axs.plot(np.arange(0,ITER)*Delta, y,label="finite difference",ls="dashdot")
axs.plot(np.arange(0,ITER)*Delta, y_ana,label="analytical",ls="solid")
axs.legend()
axs.set_xlabel("Time(s)")
axs.set_ylabel("Solution of ODE")
f1.set_size_inches(10,8)
f1.savefig("hw10_problem4_solution.pdf")
plt.show()
plt.close()
