import os
import tkinter as tk
import requests
from bs4 import BeautifulSoup
from tkinter.messagebox import *

def button_kill_all():
    for processus in programmes:
        try:
            kill_command = f"taskkill /IM {processus} /F"
            os.system(kill_command)
        except Exception as e:
            print(f"Erreur lors de l'arrêt du processus {processus}: {e}")

def button_kill_spe(processus_name):
    for processus in programmes:
        if processus_name.lower() in processus.lower():
            try:
                os.popen(f"taskkill /IM {processus} /F")
            except Exception as e:
                print(f"Erreur lors de l'arrêt du processus {processus}: {e}")

def appelle():
    if askyesno('Titre 1', 'Êtes-vous sûr de vouloir faire ça?'):
        button_kill_all()
    else:
        root.destroy

def creation_arret_button(processus):
    def kill_processus_appelle():
        button_kill_spe(processus)
    kill_boutton = tk.Button(root, text=f"Arret {processus}", command=kill_processus_appelle)
    kill_boutton.pack()

blacklist_path = "blacklist.csv"
log_filename = "interdiction.log"
log_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), log_filename)

programmes = []

try:
    with open(log_path, "r") as file:
        for line in file:
            programmes.append(line.strip().replace('"', ""))
except FileNotFoundError:
    print("Fichier log non trouvé")
except Exception as e:
    print(f"Erreur lors de la lecture du fichier log : {e}")

root = tk.Tk()

titre_label = tk.Label(root, text="Interdictions trouvées :")
titre_label.pack()

ok_button = tk.Button(root, text="OK", command=root.destroy)
ok_button.pack()

taskkill_button = tk.Button(root, text="Terminer les tâches", command=appelle)
taskkill_button.pack()

processus_label = tk.Label(root, text="\n".join(programmes))
processus_label.pack()

for processus in programmes:
    creation_arret_button(processus)

root.mainloop()