#-------------------------------------------------------------------------------
# Name:        test_interface_graphique.py
# Purpose:     Ce script permet de créer le dossier souhaité avec l'arborescence du Geomakit à l'emplacement souhaité.
#
# Author:      Paul Miancien
#
# Created:     08/06/2022
# Copyright:   (c) Paul Miancien 2022
# Licence:     <your licence>
#
# tuto : python.doctor/interface-graphique
#-------------------------------------------------------------------------------

import tkinter as tk
from functools import partial
import os, os.path
from tkinter import ttk,filedialog
import shutil

"""
Fonction servant à récupérer le chemin sélectionné par l'utilisateur et à l'afficher dans la fenêtre pour que l'utilisateur puisse le vérifier
"""
def chooseSaveFolder(frame, dirpath) :

    dirpath.set(filedialog.askdirectory())
    print(dirpath)
    ttk.Label(frame,text=dirpath.get()).grid(column=0,row=1)

"""
Cette fonction crée et affiche la fenêtre de dialogue
"""
def buildWindow() :
    path = 'G:/NasDiskStation_1/public/SO_SIG/000_DEVELOPPEMENT/GéomaKit'
    availableProjects = getAvailablebleProjectTypes(path)

    root = tk.Tk()

    #-----      Variables entrées par l'utilisateur    -----#
        # Variable contenant le chemin de sauvegarde du dossier créé, initialisée sur le dossier SO_SIG
    dirpath = tk.StringVar()
    dirpath.set('G:/NasDiskStation_1/public/SO_SIG/')
        # Variable contenant le nom du projet, entré par l'utilisateur depuis l'Entry
    entryResult = tk.StringVar()
    entryResult.set('')
        # Variable contenant le type de projet, entré par l'utilisateur via la Combobox
    comboResult = tk.StringVar()
    comboResult.set('')

    #-----      Parametres de la fenetre    -----#
        # nom de la fenetre
    root.title('Fenetre test')
        # taille de la fenetre
    root.geometry('400x300')


    #-----      Contenu de la fenetre       -----#
    frm = ttk.Frame(root, padding=10)
    frm.grid()

        # création du label et du champ de sasie du nom du projet
    ttk.Label(frm, text="Nom du projet").grid(column=0,row=0)
    ttk.Entry(frm, textvariable=entryResult, width=25).grid(column=1,row=0)


        # Création du bouton de sélection du dossier où l'on enregistrera le projet
    ttk.Button(frm, text='Parcourir...', command=partial(chooseSaveFolder,frm, dirpath)).grid(column=1, row=1)

        # Création du choix du type de projet avec Combobox
    ttk.Label(frm,text='Type de projet').grid(column=0,row=2)
    ttk.Combobox(frm, textvariable= comboResult, values=availableProjects,state="readonly").grid(column=1,row=2)

        # bouton de validation
    ttk.Button(frm, text="Ok", command=partial(validation,root, entryResult,comboResult, dirpath)).grid(column=0, row=3)
        # bouton d'annulation                                   
    ttk.Button(frm, text="Annuler", command=root.destroy).grid(column=1, row=3)

    return root
"""
Fonction d'erreur, à tranformer en classe si possible
"""
def errorLog(errorType) :
    errRoot = tk.Tk()
    if (errorType == 0) :
        errorMessage = 'Project type must be selected.'
    elif (errorType == 1) :
        errorMessage = 'Project name must be selected.'
    
    frm = ttk.Frame(errRoot, padding=10)
    frm.grid()
    ttk.Label(frm, text=errorMessage).grid(column=0,row=0)

    ttk.Button(frm, text="OK", command=errRoot.destroy).grid(column=0, row=1)

    errRoot.mainloop()

"""
La fonction ci-dessous récupère le nom des fichiers du Geomakit pour que l'utilisateur puisse choisir quel type projet il veut créer.
Si on rajoute un dossier dans le géomakit ça se met à jour automatiquement.
"""
def getAvailablebleProjectTypes(path) :
    listeProjets= []
    for name in os.listdir(path) :
        listeProjets.append(name)

    return listeProjets

"""
fonction de validation, appelée lors du clic sur le bouton "OK"
"""

def validation(root,entryResult, comboResult, dirpath) :
    
    projectName = entryResult.get()
    projectType = comboResult.get()

    from_directory = 'G:/NasDiskStation_1/public/SO_SIG/000_DEVELOPPEMENT/GéomaKit/' + projectType
    to_directory = dirpath.get() + '/'+ projectName + '/' + projectType


    if (projectName == '') :
        errorLog(1)
    elif (projectType == '') :
        errorLog(0)
    else :
        print(from_directory)
        print(to_directory)
        copyFolder(from_directory, to_directory)
        # fermeture de la fenetre
        root.destroy()

"""
Fonction servant à créer et copier le dossier souhaité à l'endroit souhaité
Fonction à transformer en classe pour une meilleure 
"""
def copyFolder(from_directory, to_directory) :
    shutil.copytree(from_directory, to_directory, symlinks=False, dirs_exist_ok=False)



class folderCopier :
    print('coucou')

if __name__ == '__main__':
    root = buildWindow()

        #-----      Faire apparaitre la fenetre   -----#
    root.mainloop()