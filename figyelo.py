import os, sys
from ftplib import FTP
import time 

while True:
    lista = os.listdir('C:\\')
    st = '\t'.join(lista)

    file = open('mappa.tom','w')
    file.write(st)
    file.close()

    ftp = FTP('files.000webhost.com')
    ftp.login('tomipythonfatman', '5f98ed00')

    if(ftp):
        print("Sikeres Frissítés\n\n")
    else:
        print("Valami nem stimmel")

    #Feltöltés
    filename = 'mappa.tom'
    ftp.storbinary('STOR '+filename, open(filename, 'rb'))
    ftp.quit()

    print("Még egy óra a firssítésig")
    strings = time.strftime("%H:%M:%S\n\n")
    print (strings)
    time.sleep(1800)
    print("Még fél óra a firssítésig!")
    strings = time.strftime("%H:%M:%S\n\n")
    print (strings)
    time.sleep(1800)
    


