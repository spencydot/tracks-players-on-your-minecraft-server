from os import name, system
import os

pyLog = 'pyLogs.txt'
mcLogs = 'logs\latest.log'

openLookIp = '[/'
closeLookIp = '] logged in'
playerIps = []

openLook = '/INFO]: '
closeLook = '[/'
playerNames = []


while True:
    f = open(mcLogs, 'rb')
    f.seek(-2, os.SEEK_END)

    while f.read(1) != b'\n':
        f.seek(-2, os.SEEK_CUR) 
    
    line = f.readline().decode()
    if openLookIp in line:
        string = line[line.find(openLook)+8:line.find(closeLook)]
        stringIp = line[line.find(openLookIp)+2:line.find(closeLookIp)]
        
        if stringIp in playerIps:
            pass
        else:
            playerNames.append(string)
            playerIps.append(stringIp)
            system("cls") # Cleans Up console
            print(f'Names: {playerNames}')
            print(f'Ip: {playerIps}')
            pass
        f.close
    else:
        f.close
    f.close
    
    