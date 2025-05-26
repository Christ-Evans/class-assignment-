import turtle as t

def DrawShape(long, cotés, x, y, couleur):
    t.penup()
    t.goto(x, y)
    t.pendown()
    Angles = 360 / cotés
    t.begin_fill()
    for i in range(0, cotés, 1):
        t.forward(long)
        t.right(Angles)

    t.end_fill()

boucle = "o"
while boucle == "o":
    cotés = input("Nombre de côtés (de 3 à 10): ")
    while type(cotés) is not int:
        try:
            cotés = int(cotés)
            if cotés < 3 or cotés > 10:
                cotés = input("Nombre de côtés (de 3 à 10): ")

        except:
            cotés = input("Nombre de côtés (de 3 à 10): ")

    long = input("Longueur de côtés (de 10 à 70): ")
    while type(long) is not int:
        try:
            long = int(long)
            if long < 10 or long > 70:
                long = input("Longueur de côtés (de 10 à 70): ")

        except:
            long = input("Longueur de côtés (de 10 à 70): ")

    x = input("Postion du curseur(x) (de -100 à 100): ")
    while type(x) is not int:
        try:
            x = int(x)
            if x < -100 or x > 100:
                x = input("Postion du curseur(x) (de -100 à 100): ")

        except:
            x = input("Postion du curseur(x) (de -100 à 100): ")

    y = input("Postion du curseur(y) (de -100 à 100): ")
    while type(y) is not int:
        try:
            y = int(y)
            if y < -100 or y > 100:
                y = input("Postion du curseur(y) (de -100 à 100): ")

        except:
            y = input("Postion du curseur(y) (de -100 à 100): ")

    couleur = input("Donne moi une couleur en anglais: ")
    try:
        t.fillcolor(couleur)

    except:
        Erreur = print(f"La couleur {couleur} n'a pas marché. Donc se sera le blanc")
        t.fillcolor("white")

    DrawShape(long, cotés, x, y, couleur)

    boucle = input("Recommencer (o/n): ")
    if boucle.lower == "n":
        break


print("Bonne journée")
