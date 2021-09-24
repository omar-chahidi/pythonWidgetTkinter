#coding:utf-8

"""
    + Positionnement des widget dans une interface et lorganisation des intérfaces
    + On va utiliser le widget de cadre qui s'appelle FRAME qui va contenir d'autre widget
    + on va utiliser des grid (ligne - colone) pour positionner nos widgets 
"""

# import module pour la création des widgets
import tkinter

# 0/ Création de fenêtre app
app = tkinter.Tk()

# 1/ ajouter un titre
app.title("Positionnement des widget avec des frame")


# 2/ donner une taille à notre fenêtre
app.geometry("400x400")

# 3/ widgets
# 3 - 1/ Création de frame
mainFrame = tkinter.LabelFrame(app, text="Frame 1", width=300, height=300, borderwidth=1)
mainFrame.pack()

# 3 - 1/ Création de widget dans  mon cadre frame
label = tkinter.Label(mainFrame, text="Je suis un label", padx=15, pady=50)
ent = tkinter.Entry(mainFrame)
#btn = tkinter.Button(app, text="BIENVENUE")
btn = tkinter.Button(mainFrame, text="BIENVENUE")

label.grid(row=0, column=0)
ent.grid(row=0, column=1)
btn.grid(row=0, column=2)

# Boucle infini pour que la fenêtre reste ouverte
app.mainloop()