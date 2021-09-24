#coding:utf-8

"""
    + Objectif : créer un menu
    + création barre de menu
    + attacher le menu au niveau de notre fenêtre
    + à l'intérieur de la barre on va créer un menu "firstMenu" et "secondMenu"
    + ajouter des option dans chaque menu "firstMenu" et "secondMenu"
    + affichier les deux menus "firstMenu" et "secondMenu" dans la barre menu
    + ajouter des methodes / fonctions dans la menu (exemple quitter ou ecrire un message dans le terminale)
    + ouvrir une seconde fenêtre ou sous fenêtre
        - ajouter des widgets suplimentaire avec "toplevel"

"""


# import module pour la création des widgets
import tkinter

# 0/ Création de fenêtre app
app = tkinter.Tk()

# 1/ ajouter un titre
app.title("Création menu")


# 2/ donner une taille à notre fenêtre
app.geometry("400x400")

# 3 - 6 / création sous fenêtre avec l'option Toplevel
def direBonjour():
    print("Déclanchement de l'Option 1 => bonjour !!!")

# 3 - 7 / création de la commande direBonjour
def afficherSousFenêtre():
    sousFenetre = tkinter.Toplevel(app)
    sousFenetre.title("Une nouvelle fenêtre")
    sousFenetre.geometry("400x100")
    labelSousFenetre = tkinter.Label(sousFenetre, text="Bonjour sous fenêtre")
    labelSousFenetre.pack()

# 3/ widgets
# 3 - 1 / création la barre de menu
mainMenu = tkinter.Menu(app)

# 3 - 2 / attacher le menu au niveau de notre fenêtre
app.config(menu=mainMenu)

# 3 - 3 / création de mon 1er menu avec des valeurs à parcourir
firstMenu = tkinter.Menu(mainMenu)
firstMenu.add_command(label="Option 1", command=direBonjour)
firstMenu.add_command(label="Option 2")
firstMenu.add_command(label="Afficher une sous fenêtre", command=afficherSousFenêtre)

# 3 - 4 / création de mon deuxième menu
secondMenu = tkinter.Menu(mainMenu, tearoff=0) # tearoff pour enlever la ligne -----
secondMenu.add_command(label="Commande x")
secondMenu.add_command(label="Commande y")
secondMenu.add_separator()
secondMenu.add_command(label="Quitter", command=app.quit)

# 3 - 5 / attacher les deux menus en cascade à la menu "mainMenu"
mainMenu.add_cascade(label="Options",   menu=firstMenu)
mainMenu.add_cascade(label="Commandes", menu=secondMenu)



# Boucle infini pour que la fenêtre reste ouverte
app.mainloop()