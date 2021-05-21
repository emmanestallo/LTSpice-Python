import subprocess

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