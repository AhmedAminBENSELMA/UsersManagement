import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
import subprocess
import os

# Fonction pour gérer la fonctionnalité de gestion des comptes utilisateurs
def gerer_comptes_utilisateurs():
    messagebox.showinfo("Gestion des comptes utilisateurs", "Fonctionnalité de gestion des comptes utilisateurs")
    
    # Fonction pour créer un compte utilisateur
    def creer_compte_utilisateur():
        username = input("Entrez le nom d'utilisateur : ")
        full_name = input("Entrez le nom complet : ")
        home_dir = input("Entrez le répertoire de l'utilisateur : ")

        # Vérifier si le répertoire spécifié existe ou le créer
        if not os.path.isdir(home_dir):
            os.makedirs(home_dir)

        subprocess.call(['useradd', '-m', '-d', home_dir, '-c', full_name, username])
        print(f"Le compte utilisateur {username} a été créé avec succès.")
        with open('log.txt', 'a') as log_file:
            log_file.write(f"Création du compte utilisateur : {username}, Nom complet : {full_name}, Répertoire : {home_dir}\n")
    
    # Fonction pour modifier un compte utilisateur
    def modifier_compte_utilisateur():
        username = input("Entrez le nom d'utilisateur à modifier : ")
        full_name = input("Entrez le nouveau nom complet : ")
        home_dir = input("Entrez le nouveau répertoire de l'utilisateur : ")

        subprocess.call(['usermod', '-c', full_name, '-d', home_dir, username])
        print(f"Le compte utilisateur {username} a été modifié avec succès.")
        with open('log.txt', 'a') as log_file:
            log_file.write(f"Modification du compte utilisateur : {username}, Nouveau nom complet : {full_name}, Nouveau répertoire : {home_dir}\n")

    # Fonction pour supprimer un compte utilisateur
    def supprimer_compte_utilisateur():
        username = input("Entrez le nom d'utilisateur à supprimer : ")

        subprocess.call(['userdel', '-r', username])
        print(f"Le compte utilisateur {username} a été supprimé avec succès.")
        with open('log.txt', 'a') as log_file:
            log_file.write(f"Suppression du compte utilisateur : {username}\n")

    # Fonction pour afficher les caractéristiques d'un compte utilisateur
    def afficher_caracteristiques_utilisateur():
        username = input("Entrez le nom d'utilisateur : ")

        subprocess.call(['id', username])

    # Fonction pour créer des comptes utilisateurs à partir d'un fichier
    def creer_comptes_utilisateurs_fichier():
        filename = input("Entrez le nom du fichier contenant la liste des utilisateurs à créer : ")

        with open(filename, 'r') as file:
            for line in file:
                username, full_name, home_dir = line.strip().split(':')
                if not os.path.isdir(home_dir):
                    os.makedirs(home_dir)

                subprocess.call(['useradd', '-m', '-d', home_dir, '-c', full_name, username])
                print(f"Le compte utilisateur {username} a été créé avec succès.")
                with open('log.txt', 'a') as log_file:
                    log_file.write(f"Création du compte utilisateur : {username}, Nom complet : {full_name}, Répertoire : {home_dir}\n")

    # Création de la fenêtre pour la gestion des comptes utilisateurs
    compte_utilisateurs_window = tk.Toplevel(window)
    compte_utilisateurs_window.title("Gestion des comptes utilisateurs")
    compte_utilisateurs_window.geometry("400x300")

    # Création des boutons pour les fonctionnalités de gestion des comptes utilisateurs
    btn_creer_compte = tk.Button(compte_utilisateurs_window, text="Créer un compte utilisateur", command=creer_compte_utilisateur)
    btn_creer_compte.pack(pady=10)

    btn_modifier_compte = tk.Button(compte_utilisateurs_window, text="Modifier un compte utilisateur", command=modifier_compte_utilisateur)
    btn_modifier_compte.pack(pady=10)

    btn_supprimer_compte = tk.Button(compte_utilisateurs_window, text="Supprimer un compte utilisateur", command=supprimer_compte_utilisateur)
    btn_supprimer_compte.pack(pady=10)

    btn_afficher_caracteristiques = tk.Button(compte_utilisateurs_window, text="Afficher les caractéristiques d'un compte utilisateur", command=afficher_caracteristiques_utilisateur)
    btn_afficher_caracteristiques.pack(pady=10)

    btn_creer_comptes_fichier = tk.Button(compte_utilisateurs_window, text="Créer des comptes utilisateurs à partir d'un fichier", command=creer_comptes_utilisateurs_fichier)
    btn_creer_comptes_fichier.pack(pady=10)

# Fonction pour gérer la fonctionnalité de surveillance de l'utilisation du serveur
def surveiller_utilisation_serveur():
    messagebox.showinfo("Surveillance de l'utilisation du serveur", "Fonctionnalité de surveillance de l'utilisation du serveur")

    # Fonction pour afficher l'utilisation du serveur
    def afficher_utilisation_serveur():
        subprocess.call(['top'])

    # Création de la fenêtre pour la surveillance de l'utilisation du serveur
    surveillance_window = tk.Toplevel(window)
    surveillance_window.title("Surveillance de l'utilisation du serveur")
    surveillance_window.geometry("400x300")

    # Création du bouton pour afficher l'utilisation du serveur
    btn_afficher_utilisation = tk.Button(surveillance_window, text="Afficher l'utilisation du serveur", command=afficher_utilisation_serveur)
    btn_afficher_utilisation.pack(pady=10)

# Fonction pour afficher le menu des fonctionnalités
def afficher_menu():
    subprocess.call("./projet.sh", shell=True)

# Callback function pour le bouton "Choisir un fichier" de la fonction "creer_comptes_utilisateurs_fichier"
def choisir_fichier():
    filename = askopenfilename()
    # Utilisez le nom de fichier sélectionné pour exécuter la fonction "creer_comptes_utilisateurs_fichier"

# Création de la fenêtre principale
window = tk.Tk()
window.title("Gestion du serveur")
window.geometry("400x300")

# Création des boutons pour les fonctionnalités
btn_comptes_utilisateurs = tk.Button(window, text="Gestion des comptes utilisateurs", command=gerer_comptes_utilisateurs)
btn_comptes_utilisateurs.pack(pady=10)

btn_surveillance = tk.Button(window, text="Surveillance de l'utilisation du serveur", command=surveiller_utilisation_serveur)
btn_surveillance.pack(pady=10)

btn_menu = tk.Button(window, text="Afficher le menu des fonctionnalités", command=afficher_menu)
btn_menu.pack(pady=10)

# Création du bouton pour choisir un fichier dans la fonction "creer_comptes_utilisateurs_fichier"
btn_choisir_fichier = tk.Button(window, text="Choisir un fichier", command=choisir_fichier)
btn_choisir_fichier.pack(pady=10)

# Lancement de la boucle principale de l'interface graphique
window.mainloop()
