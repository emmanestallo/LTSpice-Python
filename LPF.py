import subprocess

#location of XVIIx64.exe
prog_path = 'D:\LTSpice'

txt_file = 'LPF.txt'
Res1_orig = 'Res1=1k'
Cap1_orig = 'Cap1=0.1u'

#we can store all values in a list and just iterate using f'string'
for i in range(2):

    #read and write in binary to disregard whitespaces
    with open(txt_file, 'rb') as file:
        data_orig = file.read()
        data_temp = data_orig.replace(Res1_orig.encode('ascii'), 'Res1=10k'.encode('ascii'))\
            .replace(Cap1_orig.encode('ascii'), 'Cap1=1u'.encode('ascii'))

    with open(f'new_file.txt{i}', 'wb') as file:
        file.write(data_temp)

    subprocess.call(prog_path +f'\XVIIx64.exe -b new_file.txt-{i}')