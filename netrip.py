import subprocess as sp
import socket
import os 


print('\n',
    '   ================================================= \n',
    ' /                                                    \ \n',
    '| the program gets saved wifi data from local device   | \n',
    '|          and prints them in seperate files           | \n',
    ' \                                                    /  \n',
    '   ================================================='
)

path = ''
while (os.path.isdir(path) != True): 
    path = input('choose a path for wifi log files : ')
    if (os.path.isdir(path) == True):
        break
    elif path == '':
        absolute_path = os.path.abspath(__file__)
        path = os.path.dirname(absolute_path)
        print("Path: " + os.path.dirname(absolute_path) + '\wifilyzer')


path = path + ' '
push = path[len(path)-2] + path[len(path)-1]         

if push == '/ ' or push == '\ ':
    path = path[0:-1]
    path = path + 'wifilizer'
    if (os.path.isdir(path) != True):
        os.mkdir(path)
else:
    path = path[0:-1]    
    path = path + '\wifilizer'
    if (os.path.isdir(path) != True):
        os.mkdir(path)
    
print('path : ',path)




###################################################################
# IP  and stuff (im open for suggestion if there is stuff to add) #
###################################################################

dname = socket.gethostname()
IP = socket.gethostbyname(dname)

lang = ''

#########################
# file: Full log; SSIDs #
#########################
full = path +'\full.txt'
EE = open(full,'w')
cmd = sp.getoutput('netsh wlan show profiles') 
EE.write(cmd)
EE.write('\n')
EE.write('\n')
EE.write('\n')


cmd = cmd.split('\n')
profiles = []


for i in cmd:
    if "Profil Tous les utilisateurs"  in i :
        i = i.split(":")
        i = i[1]
        profiles.append(i)
        lang = 'fr'
    elif "All user profile"  in i :
        i = i.split(":")
        i = i[1]
        profiles.append(i)

wifis = {}

for r in range(len(profiles)) :    
    y = str(profiles[r]).split()
    profiles[r] = ' '.join(y)

    #####################################
    # file :Full log; profile key=clear #
    #####################################
    results = sp.getoutput('netsh wlan show profiles name="'+profiles[r] + '" key=clear')         
    EE.write(results)
    EE.write('\n')
    EE.write('\n')
    EE.write('\n')
    results= results.split('\n')
    
    #for french OSs 
    if lang == 'fr':
        for t in results:
            if 'Nom du SSID' in t:
                t = t.split(":")
                t = t[1]
                global x
                x = {'name':t}

        for i in results:
            if 'Authentification' in i:
                i = i.split(":")
                i = i[1]
                global f
                f = {'auth':i}
    

        for j in results:
            if 'Contenu' in j:
                j = j.split(":")
                j = j[1]
                global z
                z = {'pass':j}
        wifis.update({r:[x,z,f]})

    #for english OSs
    else:
        for t in results:
            if 'SSID name' in t:
                t = t.split(":")
                t = t[1]
                global X
                X = {'name':t}

        for i in results:
            if 'Authentication' in i:
                i = i.split(":")
                i = i[1]
                global F
                F = {'auth':i}
        for j in results:
            if 'Content' in j:
                j = j.split(":")
                j = j[1]
                global Z
                Z= {'pass':j}
        wifis.update({r:[X,Z,F]})
EE.close()



##################################
# file :SSIDs and keys only + ip #
##################################
ness = path + 'ness.txt' 
FF = open(ness,'w')
FF.write('\n')
FF.write('= '*20)
FF.write('\n')
FF.write(' W I F I S')
FF.write('\n')
FF.write('= '*20)
FF.write('\n')

for i in range(len(wifis)):
    FF.write(str(wifis[i]))
    FF.write('\n')

FF.write('\n')
FF.write('= '*20)
FF.write('\n')
FF.write('IP')
FF.write('\n')
FF.write('= '*20)
FF.write('\n')


FF.write(
    "Host Name is:" + dname +'\n'
    "Computer IP Address is:" + IP
)
FF.close()

print('full output at : ',full)
print('quick output at : ',ness)
