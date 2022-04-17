import pywhatkit as kit
import time
import os
def menu():
    print("-----------------MENU-----------------------------\n")
    print("1..Ecrire un texte en manuscrit (Obtiens son resultat sous forme d'image)")
    print("2..Recherche par mot clé")
    print("3..Recherche sur le navigateur")
    print('4..Envoyer un message Whatsapp à quelqu\'un')
    print('5..Recherche une video sur youtube')
    print('6..Envoyer Message Whatsapp Instantannée')
    print("7.. Quitter")
    return input("Quel action voulez-vous effectuez : ")

def traitement(choix):
    temp = choix
    if temp == 1:
        s = input("Entrez le texte à transformer en manuscrit : ")
        kit.text_to_handwriting(s)
    elif temp == 2:
        s = input("Entrez le mot à Rechercher : ")
        lines = input("Nombre de lignes : ")
        lines = 3 if int(lines) <= 3 else int(lines)
        try:
            kit.info(s, lines=lines)

        except:
            print("Pas de resultats possibles")
    elif temp == 3:
        s = input("Mot a Rechercher : ")
        kit.search(s)
    elif temp == 4:
        print("----ENVOI MESSAGE------")
        num = input("Numero du destinataire (+xx xx xx xx xx) : ")
        message = input("Message :")
        h, m = list(map(int, input("Heure d'envoi (h:m):").split(':')))
        kit.sendwhatmsg(num, message, h, m)
    elif temp == 5:
        print("---------Recherche Sur YouTUBE--------------")
        s = input("Mot a rechercher sur youtube :")
        kit.playonyt(s)
    elif temp == 6:
        print("---------------Message INSTANTANNEE--------")
        num = input("Numero du destinataire (+xx xx xx xx xx) : ")
        message = input("Message :")
        kit.sendwhatmsg_instantly(num,message)
    elif temp == 7:
        print("Goodbye!!Bye bye")
        return 0
    else:
        print('Action non Disponible.Veuillez Ressayer')

    return 1



