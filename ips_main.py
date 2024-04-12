#Appel des librairies
import logging
import os
import socket

#Déclaration de variables
hostname   = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

#Config du logging
logging.basicConfig(
    level=logging.DEBUG, 
    filename='interdiction.log', 
    filemode='a', 
    format='%(message)s'  
)

#Vérification existance de readed
def check_readed():
    if not os.path.isfile('readed.csv'):
        with open('readed.csv', 'w') as readed_csv:
            readed_csv.write('Readed \n')

#Vérification des tâches safe
def is_safe(process, safe_process):
    if process == safe_process:
        return True
    else:
        return False

#Blacklistage des tâches
def is_blacklist(process, blacklisted_process):
    if process == blacklisted_process.strip():
        logging.info(f'{hostname}|{ip_address}|{process}')
        return True
    else:
        return False

#Ecriture dans readed.csv
def write_readed(process):
    with open("readed.csv", "a") as write_process:
        write_process.write(process + '\n')

#Traitement des tâches
def processing(process, blacklist, readed_file):
    is_blacklisted = False
    start_interface= False
    safe = False
    for safe_process in readed_file:
        if not safe:
            safe_process = safe_process.strip()
            safe = is_safe(process, safe_process)
    if not safe:   
        for blacklisted_process in blacklist:
            is_blacklisted = is_blacklist(process, blacklisted_process)
            if is_blacklisted:
                start_interface = True
        if not start_interface:
            write_readed(process)
    return start_interface


#Récupère un CSV des tasks dans Windows
fichier = os.popen('tasklist /FO CSV')
check_readed()
stop_nb = 0
is_stop = False
for ligne in fichier:
    #Mise en forme
    ligne = ligne.split(',')
    ligne = ligne[0].replace('"', '')
    ligne = ligne.strip()
    blacklist   = open('blacklist.csv', 'r')
    readed_file = open('readed.csv', 'r')  
    #Vérifie les tasks déjà analysés     
    is_stop = processing(ligne, blacklist, readed_file)
    if is_stop:
        stop_nb = stop_nb + 1
if stop_nb > 0:
    os.system("python ips_interface.py")
fichier.close()