#Appel des librairies
import logging
import os
import socket

#Déclaration de variables
hostname   = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
is_blacklisted = False
in_blacklist   = False

#Config du logging
logging.basicConfig(
    level=logging.DEBUG, 
    filename='interdiction.log', 
    filemode='a', 
    format='%(message)s'  
)

#Récupère un CSV des tasks dans Windows
fichier = os.popen('tasklist /FO CSV')
for ligne in fichier:
    #Mise en forme
    ligne = ligne.split(',')
    ligne = ligne[0].replace('"', '')
    ligne = ligne.strip()
    #Vérifie les tasks déjà analysés
    readed = False
    with open("readed.csv", "r") as readed_process:
        for tasks in readed_process:
            with open("blacklist.csv", "r") as blacklist:
                    for process in blacklist:
                        if ligne != tasks.strip() and not readed:
                            readed = False
                            if ligne == process:
                                in_blacklist = True
                        else:
                            readed = True
        if not readed:
            #Ecrit les tasks analysé
            with open("readed.csv", "a") as write_process:
                if not in_blacklist:
                    write_process.write(ligne + '\n')
                #Analyse les tasks en blacklist
                with open("blacklist.csv", "r") as blacklist:
                    for process in blacklist:
                        process = process.strip()
                        if process == ligne:
                            logging.info(f'{hostname}|{ip_address}|{ligne}')
                            is_blacklisted = True
if is_blacklisted:
    os.system("python ips_interface.py")
fichier.close()