#Pour le main mettre dans un fichier interdiction.log
import logging
import os

logging.basicConfig(
    level=logging.DEBUG, 
    filename='interdiction.log', 
    filemode='a', 
    format='%(message)s'  
)

fichier = os.popen('tasklist /FO CSV')
for ligne in fichier:
    with open("blacklist.csv", "r") as blacklist:
        for process in blacklist:
            if process == ligne:
                logging.info(ligne)
fichier.close()