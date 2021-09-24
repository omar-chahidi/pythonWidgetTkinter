#coding:utf-8

"""
    TKINTER :   une bibliothèque qui nous permet de créer des intérfaces graphique
                avec un esemble de widgets
    
    Pour ajouter une widget il faut :
                <nom_variable> = <nom_widget>(<widget_parent>, <params>, ...)
    
    Ajouter des controleurs sur les variables des widgets ==> manipuller des variable via un observateurs
    StringVar() : chaine de caractère [str]
    IntVar()    :  nombre entier [int]
    DoubleVar() :  nombre flotant [float]
    BooleVar()  :  nombre booléen [bool]
"""

# import module pour la création des widgets
import tkinter

# import module pour la création des fenêtres de demande de confirmation
# ou déclancher une fenêtre erreur via une intérface modale qui va prendre le contrôle du wideget 
from tkinter import messagebox

# 0/ Création de fenêtre app
app = tkinter.Tk()

# 1/ ajouter un titre
app.title("Variables tkinter")


# 2/ donner une taille à notre fenêtre
app.geometry("400x600")


# 3/ widgets
varLabel = tkinter.StringVar()
label = tkinter.Label(app, textvariable=varLabel)
varLabel.set("coucou")
print("Label : ", varLabel.get())
label.pack()

# 4/ Création un observateur de tout ce qui est saisie par l'utilisateur
def updateLabel(*args):
    varLabel.set(varEntry.get())

varEntry = tkinter.StringVar()
varEntry.trace("w", updateLabel) # ajouter la connexion entre la saisie et l'affichage
entry = tkinter.Entry(app, textvariable=varEntry)
entry.pack()

# 5/ un observateur sur les bouttons 
def updateRadioButtonObservor(*args):
    print("J'ai vu {}!! ".format(varBotton.get()))
    if varBotton.get() == 1:
        print("==> HOMME")
        varLabelBouttonObservateur.set("C'est un HOMME")
    else:
        print("==> FEMME")
        varLabelBouttonObservateur.set("C'est une FEMME")
varBotton = tkinter.IntVar()
varBotton.trace("w", updateRadioButtonObservor)
radio1 = tkinter.Radiobutton(app, text="HOMME", value=1, variable = varBotton)
radio2 = tkinter.Radiobutton(app, text="FEMME", value=0, variable = varBotton)
radio1.pack()
radio2.pack()


varLabelBouttonObservateur = tkinter.StringVar()
labelPourBoutton = tkinter.Label(app, textvariable=varLabelBouttonObservateur, text="coucocccccccccccccc")
labelPourBoutton.pack()

# Boucle infini pour que la fenêtre reste ouverte
app.mainloop()