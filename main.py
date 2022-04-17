import pywhatkit as kit

from api import menu

while True:
    temp=menu()
    if temp==1:
        s=input("Entrez le texte à transformer en manuscrit : ")
        kit.text_to_handwriting(s)
    elif temp==2:
        s=input("Entrez le mot à Rechercher : ")
        lines=input("Nombre de lignes : ")
        lines=3 if int(lines)<=3 else int(lines)
        kit.info(s,lines=lines)
    elif temp==3:
        s=input("Mot a Rechercher : ")
        kit.search(s)
    elif temp==4:
        print("----ENVOI MESSAGE------")
        num=input("Numero du destinataire (+xx xx xx xx xx) : ")
        message=input("Message :")
        h,m=list(map(int,input("Heure d'envoi (h:m):").split(':')))
        kit.sendwhatmsg(num,message,h,m)
    elif temp==5:
        print("---------Recherche Sur YouTUBE--------------")
        s=input("Mot a rechercher sur youtube")


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