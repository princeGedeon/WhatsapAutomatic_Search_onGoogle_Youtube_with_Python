import time

from api import menu,traitement

while True:
    work=traitement(int(menu()))
    print("Fin du traitement\n\n")
    time.sleep(10)

    if not work:
        break
    elif  int(input("Voulez vous continuez (0,1) : "))==0:
        break

#Transformer texte écrit en manuscrit
#kit.text_to_handwriting('Hello world')
#Avoir le resultat de recherche sur un mot clé
#kit.info("Roi")
#Faire recherche et afficher sur navigator
# kit.search('Naruto')
#Envoyer un message
#kit.sendwhatmsg("+22996426575","Hi",0,4)
#Lire une video sur youtube
#kit.playonyt("Sexe")