from pylab import *

time_0 = np.linspace(-8*np.pi, 8*np.pi, 1024,endpoint=True)
S1,S2 = np.sin(time_0), np.sin(10*time_0)
scale_0 = S1+S2

def scaling(data, time):

	minmax =[]
	minmax_time = []
	result = []
	result_time = []

	for i in range(len(data) - 2):
	    '''a = data[i]
	    b = data[i+1]
	    c = data[i+2]'''
	    
	    if (data[i+1] < data[i]) and (data[i+1] < data[i+2]):
	        minmax.append(data[i+1])
	        minmax_time.append(time[i+1])
	    if (data[i+1] > data[i]) and (data[i+1] > data[i+2]):
	        minmax.append(data[i+1])
	        minmax_time.append(time[i+1])

	if minmax[0] < minmax[1]:
		for i in range(1, len(minmax), 2):
			result.append(minmax[i])
			result_time.append(minmax_time[i])
	else:
		for i in range(0, len(minmax), 2):
			result.append(minmax[i])
			result_time.append(minmax_time[i])

	return (result, result_time)

#scale_1, time_1 = scaling(signal, X)
plot(time_0, scale_0)

i = 1
while min(globals()['scale_' + str(i-1)]) != max(globals()['scale_' + str(i-1)]):
	globals()['scale_' + str(i)] , globals()['time_' + str(i)]  = scaling(globals()['scale_' + str(i-1)], globals()['time_' + str(i-1)])
	plot(globals()['time_' + str(i)], globals()['scale_' + str(i)])
	i = i+1

print i-1
print globals()['scale_' + str(i-1)]
show()