print("Hello World")

from datetime import datetime
hour = datetime.now().hour

if hour < 12:
	time_of_day = "morning"
else:
	time_of_day = "night"

print 'Good %s, World'  %time_of_day

import numpy as np 
import pylab as pl
import matplotlib
pl.ion()

x = np.arange(0,2,0.1)
y = np.random.rand(20,1)
#pl.plot(x,'o')

#data = np.arange(20)
#r = np.random.randn(20)
#idx = r>0.8
#print data[idx]
#print data[~idx]



xb = (np.random.rand(10)*2-1)/2-0.5
yb = (np.random.rand(10)*2-1)/2+0.5
xr = (np.random.rand(10)*2-1)/2+0.5
yr = (np.random.rand(10)*2-1)/2-0.5
inputs = []
for i in range(len(xb)):
	inputs.append([xb[i],yb[i],1])
	inputs.append([xr[i],yr[i],-1])

#pl.plot(xb,yb,'o')
#pl.plot(xr,yr,'x')
inputs = np.asmatrix(inputs)
print (inputs[:,2])

#pl.plot(inputs[:,0],inputs[:,0])