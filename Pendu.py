import time
import random
from collections import Counter

#Permet de générer une liste de mots, de la diviser, d'attribuer mot au choix aléatoire.
listedemots = "chien chat poisson noix coca ordinateur python ipad couteau"
listedemots = listedemots.split(" ")
mot = random.choice(listedemots)

def pendu(mot):
    essai =10
    while (essai>0):
        print("Hola amigo ! Bienvenue dans le merveilleux monde du pendu ! Accrochez vous à votre slip, vous n'avez que dix essais ! Essayez de deviner le mot ou une Lettre, sachant que le mot fait "+str((len(mot)))+" lettres de longeur")
        print("Il vous reste "+str(essai) + " tentatives")
    
        saisi = str(input())
        if trouverMot(mot,saisi) == True:
            print ("Bravo amigo, vous avez trouvé le mot, vous êtes un vrai tueur !"+ mot)
            return 1
        print (Foccurence(mot,saisi))
        essai = essai -1

        
def Foccurence (mot, lettre):
    occurence = 0
    position = []
    print("mon mot " +mot)
    print("ma lettre " +lettre)
    for i in range (len(mot)):
     
        if (mot[i] == lettre):
            occurence = occurence +1
            position.append(i+1)
            print ("Voici le nb d occurence(s) et leur(s) position(s)")
            
    return occurence, position
def trouverMot (Vraimot,mot):
    for i in range (len(Vraimot)):
        try:
            if (mot[i] != Vraimot[i]):
                return False
        except:
            return False
        
    return True
