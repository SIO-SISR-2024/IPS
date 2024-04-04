import os
import tkinter as tk # Mise en place des bibliothèques pour la gestion des fichiers
import curl # Dans le cas ou nous devons faire des recherches webs


Blacklist_PATH = "blacklist.csv" # Chemin vers la blacklist au cas ou nous devons verifier

log_PATH = "interdiction.log" # Chemin vers les fichiers log

liste_interdictions= "" # Variables à remplir la le nom des processus à interdire et rechercher sur internet

fenetre_root = tk.Tk()

Titre = tk.Label(fenetre_root, text="Interdictions trouvés:")

Button_OK = tk.Button(fenetre_root, text="OK", command=fenetre_root.destroy)

Button_TaskKill = tk.Button(fenetre_root, text="Terminer les tâches", command="") # Commande à terminer pour finir les tâches interdites

Affichage = tk.Label(fenetre_root, text=liste_interdictions) # Affichage des interdictions des fichiers logs