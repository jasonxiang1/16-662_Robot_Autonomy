import numpy as np
import math

import matplotlib.pyplot as plt


nrBasis=15 #Number of Gaussian basis functions

K=25*25/4 #Virtual spring coefficient
B=25	#Virtual damper coefficient

C=np.linspace(0,1,nrBasis) #Basis function centers
H=(0.65*(1./(nrBasis-1.))**2) #Basis function widths


### Load Trajectory ###############################################

D=np.load('TrajData.npy')

Time= [d[0] for d in D]
Q   = [d[1] for d in D]
Qd  = [d[2] for d in D]
Qdd = [d[3] for d in D]


### Learn Weights ###############################################
T=Time[-1]

PHI= []
F =[]
for k in range(len(Time)):
	#TODO: Compute the basis function activations and the force term
	Phi=
	Phi=    #Normalize the Gaussian basis functions
	PHI.append(Phi)

	f=
	F.append(f)

#TODO: Compute the DMP weights
w=

print"\nw=",w,"\n\n"



### Generate New Trajectory #######################################
Traj=[]
PHI=[]
execTime=[]

#TODO: Set the initial and goal states and duration
[q0, g, T]=[0, 1, T]

[q, qd, qdd, t] =[ q0, 0, 0, 0]

dt=0.001
for k in xrange(3000):
	t=t+dt
	if t<=T:
		#TODO: Compute the basis function values and force term
		
		f=
	else:
		f=0
	
	#TODO: Compute the 
	qdd=
	qd=
	q=
	
	Traj.append(q)
	execTime.append(t)


### Plot results  ###############################################

fig=plt.figure()
ax=fig.add_subplot(111)

ax.plot(Time,Q)
ax.plot(execTime,Traj)


plt.show()
