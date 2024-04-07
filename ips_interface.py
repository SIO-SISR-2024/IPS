import os
import tkinter as tk
import requests
from bs4 import BeautifulSoup

# Fonction pour touts les processus
def button_kill_all():
    for process in processes:
        kill_command = f"taskkill /IM {process} /F"
        os.system(kill_command)

# Fonction pour kill chaque processus
def button_kill_spe(process_name):
    for process in processes:
        if process_name.lower() in process.lower():
            os.popen(f"taskkill /IM {process} /F")

# Touts les chemins vers les fichiers
blacklist_path = "blacklist.csv"
log_filename = "interdiction.log"
log_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), log_filename)

# Affichage de touts les programmes dans le label de la fenetre
processes = []
with open(log_path, "r") as file:
    for line in file:
        processes.append(line.strip().replace('"', ""))

# Creation de la fenetre
root = tk.Tk()

# Tout les bouttons et label de la fenetre
title_label = tk.Label(root, text="Interdictions trouvés:")
title_label.pack()

ok_button = tk.Button(root, text="OK", command=root.destroy)
ok_button.pack()

taskkill_button = tk.Button(root, text="Terminer les tâches", command=button_kill_all)
taskkill_button.pack()

processes_label = tk.Label(root, text="\n".join(processes))
processes_label.pack()

# Boutton de kill pour chaque processus
for process in processes:
    kill_button = tk.Button(root, text=f"Kill {process}", command=lambda p=process: button_kill_spe(p))
    kill_button.pack()

# Mise en marche de la fenetre
root.mainloop()