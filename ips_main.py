#Pour le main mettre dans un fichier interdiction.log
import logging
import os

readed = False

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
    ligne = ligne.split(',')
    id = ligne[1]
    ligne = ligne[0].replace('"', '')
    ligne = ligne.strip()
#    with open("readed.csv", "a") as readed_process:
#        for tasks in readed_process:
#            if ligne == tasks:
#                readed = True
#            else:
#                readed = False
#                readed_process.write(ligne + '\n')
    with open("blacklist.csv", "r") as blacklist:
        for process in blacklist:
            process = process.strip()
            if process == ligne and not readed:
                logging.info(f'{ligne}; {id}')
fichier.close()