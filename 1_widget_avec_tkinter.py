#coding:utf-8

"""
    TKINTER :   une bibliothèque qui nous permet de créer des intérfaces graphique
                avec un esemble de widgets
    Pour ajouter une widget il faut :
                <nom_variable> = <nom_widget>(<widget_parent>, <params>, ...)
"""

# import module pour la création des widgets
import tkinter

# import module pour la création des fenêtres de demande de confirmation
# ou déclancher une fenêtre erreur via une intérface modale qui va prendre le contrôle du wideget 
from tkinter import messagebox

# 0/ Création de fenêtre app
app = tkinter.Tk()

# 1/ ajouter un titre
app.title("Widget avec tkinter")


# 2/ donner une taille à notre fenêtre
app.geometry("400x800")

# 3/ création label
label_welcome = tkinter.Label(app, text="Bienvenue à tous !")
print(label_welcome["text"])

# afficher le label
label_welcome.pack()

# 4/ ajouter un champs de saisie
entry_name = tkinter.Entry(app, width=45)
entry_name.pack()

# 5/ ajouter des bouttons
def direBonjour():
    print("Bonjour sur le terminal !")
button_quit = tkinter.Button(app, text="ok",  command=direBonjour)
button_quit.pack()

# 6/ ajouter des chek boutton. lorsque on clic valeur = 5 
check_widget = tkinter.Checkbutton(app, text="Publier ?", offvalue=2, onvalue=5)
check_widget.pack()

# 7/ radio boutton
radio_widget_homme = tkinter.Radiobutton(app, text="Homme", value=0)
radio_widget_femme = tkinter.Radiobutton(app, text="Femme", value=1)
radio_widget_homme.pack()
radio_widget_femme.pack()

# 8/ créer un curseure
scale_widget = tkinter.Scale(app)
scale_widget.pack()
spin_widget = tkinter.Spinbox(app, from_=1, to=10)
spin_widget.pack()

# 9/ créer une liste des éléments
listBox_widget = tkinter.Listbox(app)
listBox_widget.insert(1, "Windows")
listBox_widget.insert(2, "Linux")
listBox_widget.insert(3, "MacOS")
listBox_widget.pack()


# 10/ Demander une confirmation après une action avec messagebox
def show_modal_window_error():
    messagebox.showerror("ERREUR", "Un problème est survenu !!!")
def show_modal_window_info():
    messagebox.showinfo("INFO", "Pour information !!!")
def show_modal_window_warning():
    messagebox.showwarning("WARNING", "Un warning !!!")   
def show_modal_window_ouiNon():
    messagebox.askquestion("SANDAGE", "Vous voulez suivre ?")  
# définir un élément 
btnError = tkinter.Button(app, text="Déclencher une erreur", command=show_modal_window_error) 
btnError.pack()
btninfo = tkinter.Button(app, text="Déclencher un message d'information", command=show_modal_window_info) 
btninfo.pack()
btnwar = tkinter.Button(app, text="Déclencher un warning", command=show_modal_window_warning) 
btnwar.pack()
btnOuiNon = tkinter.Button(app, text="Déclencher un choix", command=show_modal_window_ouiNon) 
btnOuiNon.pack()

# Boucle infini pour que la fenêtre reste ouverte
app.mainloop()