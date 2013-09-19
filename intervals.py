import csv
from pylab import *

solarstring = []
solardata = []
solartime = []
with open('EVE_Fe_X_177_averages.csv', 'rb') as csvfile:
	solarreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
	for row in solarreader:
		solarstring.append(row)

for i in range(1,len(solarstring)):
	current_row = str(solarstring[i])
	solardata.append(float(current_row[23:len(current_row)-2]))
	solartime.append(i)

time_0 = solartime
scale_0 = solardata

def scaling(data, time):
	
	result = []
	result_time = []
	intervals = []

	for i in range(len(data) - 2):
	    	    	   
	    if (data[i+1] >= data[i]) and (data[i+1] >= data[i+2]):
	        if (data[i+1] > data[i]):
	        	result.append(data[i+1])
	        	result_time.append(time[i])
	        	if len(result_time)>0:
	        		intervals.append(result_time[len(result_time)-1] - result_time[len(result_time)-2])
	
	return (result, result_time, intervals)

#scale_1, time_1 = scaling(signal, X)
#plot(time_0, scale_0)

i = 1
while min(globals()['scale_' + str(i-1)]) != max(globals()['scale_' + str(i-1)]):
	globals()['scale_' + str(i)] , globals()['time_' + str(i)], globals()['intervals_' + str(i)]  = scaling(globals()['scale_' + str(i-1)], globals()['time_' + str(i-1)])	
	globals()['distr_' + str(i)] = []
	globals()['int_distr_' + str(i)] = []
	for x in range(min(globals()['intervals_' + str(i)]), max(globals()['intervals_' + str(i)])):		
		globals()['distr_' + str(i)].append(globals()['intervals_' + str(i)].count(x))
		globals()['int_distr_' + str(i)].append(x)	
	plot(globals()['int_distr_' + str(i)], globals()['distr_' + str(i)])
	show()
	hist(globals()['intervals_' + str(i)], bins=10)
	show()	
	i = i+1
	if i == 10: break
#plot(globals()['time_' + str(i-1)], globals()['scale_' + str(i-1)], color="red", linewidth=2.5)
#show()
