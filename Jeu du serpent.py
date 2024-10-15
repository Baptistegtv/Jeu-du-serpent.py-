import random
import os
import time

# Configuration du jeu
taille_terrain = 10
direction = "STOP"
serpent = [(5, 5)]
nourriture = (random.randint(0, taille_terrain-1), random.randint(0, taille_terrain-1))

# Fonction pour afficher le terrain de jeu
def afficher_terrain():
    for y in range(taille_terrain):
        for x in range(taille_terrain):
            if (x, y) in serpent:
                print("O", end="")
            elif (x, y) == nourriture:
                print("X", end="")
            else:
                print(".", end="")
        print()

# Fonction pour déplacer le serpent
def deplacer_serpent():
    global nourriture
    x, y = serpent[0]
    if direction == "HAUT":
        y -= 1
    elif direction == "BAS":
        y += 1
    elif direction == "GAUCHE":
        x -= 1
    elif direction == "DROITE":
        x += 1
    nouvelle_tete = (x % taille_terrain, y % taille_terrain)
    
    if nouvelle_tete in serpent:
        return False  # Game Over
    serpent.insert(0, nouvelle_tete)
    
    if nouvelle_tete == nourriture:
        nourriture = (random.randint(0, taille_terrain-1), random.randint(0, taille_terrain-1))
    else:
        serpent.pop()

    return True

# Fonction principale du jeu
def jouer():
    global direction
    while True:
        os.system("clear")
        afficher_terrain()
        print("Utilisez E/X/f/D pour bouger, Q pour quitter.")
        choix = input().upper()
        if choix == "E":
            direction = "HAUT"
        elif choix == "X":
            direction = "BAS"
        elif choix == "D":
            direction = "GAUCHE"
        elif choix == "F":
            direction = "DROITE"
        elif choix == "Q":
            break

        if not deplacer_serpent():
            print("Game Over!")
            break

        time.sleep(0.1)

# Démarrer le jeu
jouer()
