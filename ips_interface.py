import os
import tkinter as tk # Mise en place des bibliothèques pour la gestion des fichiers
import requests
from bs4 import BeautifulSoup # Dans le cas ou nous devons faire des recherches webs

def button_kill():
    for pid in log_FILENAME:
        os.kill(pid)

Blacklist_PATH = "blacklist.csv" # Chemin vers la blacklist au cas ou nous devons verifier

log_FILENAME = "interdiction.log"
log_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), log_FILENAME)

liste_interdictions= []  # Variables à remplir la le nom des processus à interdire et rechercher sur internet

fenetre_root = tk.Tk()

Titre = tk.Label(fenetre_root, text="Interdictions trouvés:")

Button_OK = tk.Button(fenetre_root, text="OK", command=fenetre_root.destroy)

Button_TaskKill = tk.Button(fenetre_root, text="Terminer les tâches", command=button_kill) # Commande à terminer pour finir les tâches interdites

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