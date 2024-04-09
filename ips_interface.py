# Importation des modules nécessaires
import os
import tkinter as tk
import requests
from bs4 import BeautifulSoup
from tkinter.messagebox import *

# Mise en place de la fonction pour tuer tous les processus interdits
def button_kill_all():
    for processus in programmes:
        try:
            kill_command = f"taskkill /IM {processus} /F" # Commande pour tuer un processus
            os.system(kill_command) # Exécution de la commande
        except Exception as e:
            print(f"Erreur lors de l'arrêt du processus {processus}: {e}")

# Mise en place de la fonction pour tuer un processus spécifique
def button_kill_spe(processus_name):
    for processus in programmes:
        if processus_name.lower() in processus.lower():
            try:
                os.popen(f"taskkill /IM {processus} /F") # Exécution de la commande pour tuer un processus spécifique
            except Exception as e:
                print(f"Erreur lors de l'arrêt du processus {processus}: {e}")

# Mise en place de la fonction pour afficher une boîte de dialogue de confirmation
def appelle():
    if askyesno('Titre 1', 'Êtes-vous sûr de vouloir faire ça?'):
        button_kill_all()
    else:
        root.destroy

# Mise en place de la fonction pour créer un bouton pour tuer un processus spécifique
def creation_arret_button(processus):
    def kill_processus_appelle():
        button_kill_spe(processus)
    kill_boutton = tk.Button(root, text=f"Arret {processus}", command=kill_processus_appelle)
    kill_boutton.pack()

# Mise en place des chemins des fichiers
blacklist_path = "blacklist.csv"
log_filename = "interdiction.log"
log_path = log_filename
# os.path.join(os.path.dirname(os.path.realpath(__file__)), log_filename) = solution de secour si il y a un probleme avec le repertoire

programmes = []

# Ouerture du fichier log pour récupérer la liste des processus interdits
try:
    with open(log_path, "r") as file:
        for line in file:
            programmes.append(line.strip().replace('"', ""))
except FileNotFoundError:
    print("Fichier log non trouvé")
except Exception as e:
    print(f"Erreur lors de la lecture du fichier log : {e}")

root = tk.Tk()

# Ajout d'un label pour afficher le titre
titre_label = tk.Label(root, text="Interdictions trouvées :")
titre_label.pack()

# Ajout d'un bouton pour fermer la fenêtre
ok_button = tk.Button(root, text="OK", command=root.destroy)
ok_button.pack()

# Ajout d'un bouton pour arreter tous les processus interdits
taskkill_button = tk.Button(root, text="Terminer les tâches", command=appelle)
taskkill_button.pack()

# Ajout d'un label pour afficher la liste des processus interdits
processus_label = tk.Label(root, text="\n".join(programmes))
processus_label.pack()

# Création d'un bouton pour tuer chaque processus interdit
for processus in programmes:
    creation_arret_button(processus)

root.mainloop()