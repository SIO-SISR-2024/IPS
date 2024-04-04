import os
import tkinter as tk # Mise en place des bibliothèques pour la gestion des fichiers
import requests
from bs4 import BeautifulSoup # Dans le cas ou nous devons faire des recherches webs

def button_kill_all():
    for id_processus_1 in log_FILENAME:
            os.kill(id_processus_1)
    
def button_kill_spe(process_name):
 for id_processus_2 in log_FILENAME:
        if titre_processus.lower() in id_processus_2.lower():
            os.kill()

Blacklist_PATH = "blacklist.csv" # Chemin vers la blacklist au cas ou nous devons verifier

log_FILENAME = "interdiction.log"
log_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), log_FILENAME) # Construction du chemin pour l'ouverture du fichier sur tout les postes

liste_interdictions= []  # Variables à remplir la le nom des processus à interdire et rechercher sur internet

fenetre_root = tk.Tk()

Titre = tk.Label(fenetre_root, text="Interdictions trouvés:")

Button_OK = tk.Button(fenetre_root, text="OK", command=fenetre_root.destroy)

Button_TaskKill = tk.Button(fenetre_root, text="Terminer les tâches", command=button_kill_all) # Commande à terminer pour finir les tâches interdites

for titre_processus in liste_interdictions:
    Button_Kill_Process = tk.Button(fenetre_root, text=f"Kill {titre_processus}", command=button_kill_spe(titre_processus))
    Button_Kill_Process.pack()
    

Affichage = tk.Label(fenetre_root, text=liste_interdictions) # Affichage des interdictions des fichiers logs

Button_OK.pack()
Button_TaskKill.pack()
Titre.pack()
Affichage.pack()

# Package de tout les objets dans notre cas cela est pour l'affichage

with open(log_PATH, "r") as fichier:
    for ligne in fichier:
        liste_interdictions.append(ligne.strip().replace("""\"""",""))

liste_interdictions_str = "\n".join(liste_interdictions) # Conversion de la liste en une chaîne pour l'affichage
Affichage.config(text=liste_interdictions_str)


fenetre_root.mainloop()