import turtle as t
import random as r

def drawshape(y, x, cotés, couleur):
    t.penup()
    t.goto(x, y)
    t.pendown()
    Angle = 360/ cotés
    t.fillcolor(couleur)
    t.begin_fill()
    for i in range(cotés):
        t.fd(50)
        t.right(Angle)

    t.end_fill()

boucle = "o"
Liste_couleur = []
Choix = ""
while boucle == "o":
    print(f"Voici ta liste de couleur {Liste_couleur}") 
    while Choix not in["a", "b", "c", "d", "e"]:
        Choix = input("""Que veut tu faire:

    A. Ajouter une couleur à la liste
    B. Enveler une couleur à la liste
    C. Déterminer l'index d'une couleur dans la liste
    D. Compter le nombre fois que la couleur se trouve dans la liste
    E. Quitter le programme 

    = """) 
    if Choix == "a":
        Ajout = input("Donne moi une couleur : ").lower()
        Liste_couleur.append(Ajout)

    elif Choix == "b":
        Retirer = input("Donne moi une couleur : ").lower()
        if Retirer in Liste_couleur:
            Liste_couleur.remove(Retirer)
        else:
            print("cet couleur n'est pas dans la liste")

    elif Choix == "c":
        Index = input("Quel couleur de ta liste veux-tu: ")
        if Index in Liste_couleur:
            print(f"La couleur {Index} à l'index {Liste_couleur.index(Index)}")

        else:
            print(f"{Index} n'est pas un nombre")

    elif Choix == "d":
        Compter = input("Donne moi une couleur et je te dirais combien de fois il est dans ta liste: ")
        if Compter in Liste_couleur:
            print(f"La couleur {Compter} est répeter {Liste_couleur.count(Compter)}")

        else:
            print(f"{Compter} n'est dans ta liste")

    elif Choix == "e":
        print(Liste_couleur)
        break
    
    Choix = ""
Choix = input("Donne un chiffre entre 1 et 6 : ")
while type(Choix) is not int:
    try:
        Choix = int(Choix)
        if Choix < 1 or Choix > 6:
            Choix = input("Donne un chiffre entre 1 et 6 : ")

    except:
        Choix = input("Donne un chiffre entre 1 et 6 : ")
cotés = 3
x = -100
y = -100
couleur = "blue"

for i in range(Choix):
    drawshape(y, x, cotés, couleur)
    cotés += 1 
    x += 100
    y += 100
    couleur = r.choice(Liste_couleur)
    #index = i%(len(Liste_couleur))
    #couleur = Liste_couleur[index]
