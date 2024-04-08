#Pour le main mettre dans un fichier interdiction.log
import logging
import os
import socket

#Déclaration de variables
hostname   = socket.gethostname()
ip_address = socket.gethostbyname(socket.gethostname())

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
            if ligne != tasks.strip() and not readed:
                readed = False
            else:
                readed = True
        if not readed:
            #Ecrit les tasks analysé
            with open("readed.csv", "a") as write_process:
                write_process.write(ligne + '\n')
                #Analyse les tasks en blacklist
                with open("blacklist.csv", "r") as blacklist:
                    for process in blacklist:
                        process = process.strip()
                        if process == ligne:
                            logging.info(f'{hostname} - {ip_address} - {ligne}')
fichier.close()