import subprocess
import ltspy3 
import matplotlib.pyplot as plt 
import numpy 

'''
Author: Emmanuel Jesus Estallo
Date: May 21, 2021

*this script is used to automate ltspice transient analysis using python
*create an asc file in ltspice
*view spice netlist
*right click and select -edit as independent netlist-
*save as cir, then save again as txt
*the circuit used here is a low pass filter. original parameters r = 1k, c=0.1u
*python is used to generate netlists with different r and c values.

Credits to UNSW Prof. Torsten Lehmann for the ltspy3 module 

'''
#ltspice executable path
prog_path = 'D:\LTSpice'

#initial parameters of the raw ltspice file 
txt_file = 'LPF.txt'
Res1_orig = 'Res1=1k'
Cap1_orig = 'Cap1=0.1u'

#parameters to be placed
cap_vals = ['100u', '47u']
res_vals = ['3.3k', '9.1k']

#iterate over all the parameters and run a subprocess every iteration
for i in range(len(cap_vals)):

    #read in binary to disregard whitespaces
    with open(txt_file, 'rb') as file:
        data_orig = file.read()
        data_temp = data_orig.replace(Res1_orig.encode('ascii'), f'Res1={res_vals[i]}'.encode('ascii'))\
            .replace(Cap1_orig.encode('ascii'), f'Cap1={cap_vals[i]}'.encode('ascii'))

    #write in binary to disregard whitespaces 
    with open(f'new_file_{i}.txt', 'wb') as file:
        file.write(data_temp)

    #-b for run in background, -Run to open an ltspice window
    subprocess.call(prog_path +f'\XVIIx64.exe -b new_file_{i}.txt')


#access the first raw file
sd1 = ltspy3.SimData(f'new_file_0.raw')
name1 = sd1.variables
num_var1 = sd1.novariables
time1 = sd1.values[0]
v_out1 = sd1.values[2]

#access the second raw file
sd2 = ltspy3.SimData(f'new_file_1.raw')
name2 = sd2.variables
num_var2 = sd2.variables 
time2 = sd2.values[0] 
v_out2 = sd2.values[2]

#plot using matplotlib
fig, (ax1,ax2) = plt.subplots(2)
fig.suptitle('V(out)')
ax1.plot(time1,v_out1)
ax1.grid()
ax2.plot(time2,v_out2)
ax2.grid()
plt.show()


    
