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
            kill_command = f"taskkill /IM {processus[2]} /F" # Commande pour tuer un processus
            os.system(kill_command) # Exécution de la commande
        except Exception as e:
            print(f"Erreur lors de l'arrêt du processus {processus[2]}: {e}")

# Mise en place de la fonction pour tuer un processus spécifique
def button_kill_spe(processus_name):
    for processus in programmes:
        if processus_name.lower() in str(processus).lower():
            try:
                os.popen(f"taskkill /IM {processus[2]} /F") # Exécution de la commande pour tuer un processus spécifique
            except Exception as e:
                print(f"Erreur lors de l'arrêt du processus {processus[2]}: {e}")

# Mise en place de la fonction pour afficher une boîte de dialogue de confirmation
def appelle():
    if askyesno('Titre 1', 'Êtes-vous sûr de vouloir faire ça?'):
        button_kill_all()
    else:
        root.destroy()

# Mise en place de la fonction pour créer un bouton pour tuer un processus spécifique
def creation_arret_button(processus):
    def kill_processus_appelle():
        button_kill_spe(processus[2]) # Pass the process name as an argument to the function
    kill_boutton = tk.Button(root, text=f"Arret {processus[2]}", command=kill_processus_appelle)
    kill_boutton.pack()
    
# Fonction pour vider le fichier log
def vider_fichier_log():
    with open(log_path, "w") as file:
        pass
    root.destroy()
# Mise en place des chemins des fichiers
blacklist_path = "blacklist.csv"
log_filename = "interdiction.log"
log_path = log_filename
# os.path.join(os.path.dirname(os.path.realpath(__file__)), log_filename) = solution de secour si il y a un probleme avec le repertoire

programmes = []

# Ouverture du fichier log pour récupérer la liste des processus interdits
try:
    with open(log_path, "r") as file:
        for ligne in file:
            host, ip, programme = ligne.strip().split('|')
            programmes.append((host, ip, programme.replace('"', "")))
except FileNotFoundError:
    print("Fichier log non trouvé")
except Exception as e:
    print(f"Erreur lors de la lecture du fichier log : {e}")

root = tk.Tk()

# Ajout d'un label pour afficher le titre
titre_label = tk.Label(root, text="Interdictions trouvées :")
titre_label.pack()

# Ajout d'un bouton pour fermer la fenêtre et vider le fichier log
ok_button = tk.Button(root, text="OK", command=vider_fichier_log)
ok_button.pack()

# Ajout d'un bouton pour arreter tous les processus interdits
taskkill_button = tk.Button(root, text="Terminer les tâches", command=appelle)
taskkill_button.pack()

# Ajout d'un label pour afficher la liste des processus interdits
processus_label = tk.Label(root, text="\n".join([f"{host} | {ip} | {programme}" for host, ip, programme in programmes]))
processus_label.pack()

# Création d'un bouton pour tuer chaque processus interdit
for host, ip, programme in programmes:
    creation_arret_button((host, ip, programme))

root.mainloop()