import os
import tkinter as tk
import requests
from bs4 import BeautifulSoup

# Fonction pour touts les processus
def button_kill_all():
    for processus in programmes:
        kill_command = f"taskkill /IM {processus} /F"
        os.system(kill_command)

# Fonction pour kill chaque processus
def button_kill_spe(process_name):
    for processus in programmes:
        if process_name.lower() in processus.lower():
            os.popen(f"taskkill /IM {processus} /F")

# Touts les chemins vers les fichiers
blacklist_path = "blacklist.csv"
log_filename = "interdiction.log"
log_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), log_filename)

# Affichage de touts les programmes dans le label de la fenetre
programmes = []
with open(log_path, "r") as file:
    for line in file:
        programmes.append(line.strip().replace('"', ""))

# Creation de la fenetre
root = tk.Tk()

# Tout les bouttons et label de la fenetre
titre_label = tk.Label(root, text="Interdictions trouvés:")
titre_label.pack()

ok_button = tk.Button(root, text="OK", command=root.destroy)
ok_button.pack()

taskkill_button = tk.Button(root, text="Terminer les tâches", command=button_kill_all)
taskkill_button.pack()

processus_label = tk.Label(root, text="\n".join(programmes))
processus_label.pack()

# Boutton de kill pour chaque processus
for processus in programmes:
    kill_boutton = tk.Button(root, text=f"Kill {processus}", command=lambda p=processus: button_kill_spe(p))
    kill_boutton.pack()

# Mise en marche de la fenetre
root.mainloop()