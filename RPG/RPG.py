# -*- coding: utf-8 -*-

import os
import sys
from time import sleep

######################
### STYLE DE TEXTE ###
######################

class ANSI():
    def style_text(code):
        return "\33[{code}m".format(code=code)
    def color_text(code):
        return "\33[{code}m".format(code=code)
    def background(code):
        return "\33[{code}m".format(code=code)

def style_by_type(type, text) :
    # codes des couleurs et de style : https://en.wikipedia.org/wiki/ANSI_escape_code#Colors
    if type == "menu" :
        styled_text = ANSI.color_text(30) + ANSI.background(107) + ANSI.style_text(3) + text + ANSI.color_text(0) + ANSI.background(0) + ANSI.style_text(0) + "> "
    elif type == "menu*":
        styled_text = ANSI.color_text(30) + ANSI.background(107) + ANSI.style_text(3) + text + ANSI.color_text(0) + ANSI.background(0) + ANSI.style_text(0)
    else : # textes sans background
        if type == "place" :
            color_code = 92
        elif type == "item" :
            color_code = 94
        styled_text = ANSI.color_text(color_code) + ANSI.style_text(1) + text + ANSI.color_text(0) + ANSI.style_text(0)
    return styled_text

def blank_screen() :
    os.system("cls")
    prompt = "\n\t[p] Menu pause\n\t[i] Inventaire\n\n"
    print(style_by_type("menu*", prompt))

###############################
### MENU ET FONCTIONS LIÉES ###
###############################

def credits():
    print("Ce jeu a été crée par Sabrina, Mattis, Charles, Sira et Enzo.")
    sleep(2)

def leave():
    print("Fermeture du jeu.")
    sleep(1)
    sys.exit()

def new_game():
    session_name = input("Nommez votre session de jeu : ")
    position = "salon"
    floor = 0
    # listes d'items
    list_items_cellier = [croquette]
    list_items_cuisine = [biere, chocolat, cookies, vodka]
    list_items_salle_a_manger = [fois, biere_rouge]
    list_items_salon = [miroir]
    list_items_jardin = [velo, cigarettes]
    position_julia = "chambre d'ami"
    # variables d'historique
    fight_soeur = None
    fight_grandpere = None
    fight_chien = None
    cigarettes_mere = None
    print("Jolie nom, " + session_name + ", commençons.")
    sleep(1)
    return session_name, position, floor, list_items_cellier, list_items_cuisine, list_items_salle_a_manger, list_items_salon, list_items_jardin, position_julia, fight_soeur, fight_grandpere, fight_chien, cigarettes_mere

def main_menu():
    session_name = None
    position = None
    floor = None
    # listes d'items
    list_items_cellier = None
    list_items_cuisine = None
    list_items_salle_a_manger = None
    list_items_salon = None
    list_items_jardin = None
    # variables d'historique
    position_julia = None
    fight_soeur = None
    fight_grandpere = None
    fight_chien = None
    cigarettes_mere = None
    prompt = "\n\t[1] Nouvelle partie\n\t[2] Crédits\n\t[3] Quittez\n\n"
    choice = int(user_input(style_by_type("menu", prompt)))
    if choice == 1:
        session_name, position, floor, list_items_cellier, list_items_cuisine, list_items_salle_a_manger, list_items_salon, list_items_jardin, position_julia, fight_soeur, fight_grandpere, fight_chien, cigarettes_mere = new_game()
    elif choice == 2:
        credits()
        session_name, position, floor, list_items_cellier, list_items_cuisine, list_items_salle_a_manger, list_items_salon, list_items_jardin, position_julia, fight_soeur, fight_grandpere, fight_chien, cigarettes_mere = main_menu()
    elif choice == 3:
        leave()
    return session_name, position, floor, list_items_cellier, list_items_cuisine, list_items_salle_a_manger, list_items_salon, list_items_jardin, position_julia, fight_soeur, fight_grandpere, fight_chien, cigarettes_mere

def pause_menu():
    prompt = "\n\t[1] Reprendre la partie\n\t[2] Fermer le jeu\n\n"
    choice = int(user_input(style_by_type("menu", prompt)))
    while choice != 1 and choice != 2 and choice != 3 and choice != 4:
        choice = int(user_input("Saisissez une valeur correcte : "))
    if choice == 1:
        return
    else:
        leave()

########################
### FONCTION D'INPUT ###
########################

def user_input(text):
    global inventory
    variable = input(text)
    if variable.lower() == "p":
        pause_menu()
        variable = user_input(text)
    if variable.lower() == "i":
        inventory_prompt(inventory)
        variable = user_input(text)
    elif variable == "":
        variable = user_input("Saisissez une valeur correcte : ")
    return variable

def choice_action(question, list_choice) :
    # Affiche la question ainsi que la liste des actions disponibles puis demande quelle action faire
    print(question)
    i = 0
    while i < len(list_choice) :
        print("[" + str(i+1) + "]", list_choice[i])
        i += 1
    action = int(user_input("> "))
    while action < 0 or action > len(list_choice) :
        action = int(user_input("Choisissez parmi les choix proposés : "))
    return action

########################
### FONCTIONS DE FIN ###
########################

def win():
    print("Vous avez gagné")
    sleep(20)
    sys.exit()

def loose():
    print("Vous avez perdu la partie")
    sleep(10)
    sys.exit()

###########################
### INVENTAIRE ET ITEMS ###
###########################

class Inventory :
    def __init__(self):
        self.content = []
    def add_item(self, item):
        self.content.append(item)
    def del_item(self, item):
        self.content.remove(item)
class Items :
    def __init__(self, name, strenght, health, description):
        self.name = name
        self.strenght = strenght
        self.health = health
        self.description = description

inventory = Inventory()

# INITIALISATION DES ITEMS DANS LES DIFFERENTES SALLES
#bureau (combat contre papy)
cle = Items(style_by_type("item", "Clé"), 1, 0, "Cette clé à l'air ancienne, peut-être qu'elle permet d'ouvrir quelque chose")
#cellier
croquette = Items(style_by_type("item", "Croquettes pour chien"), 1, 0, "N'a pas l'air très utile, peut-être que cela amadouera le chien...")
#cuisine
biere = Items(style_by_type("item", "Bière"), 2, 0, "Vous permet d'être plus confiant et de multiplier votre force par 2.")
chocolat = Items(style_by_type("item", "Chocolat chaud"), 1, 10, "Vous détend et vous permet de gagner 10 points de vie.")
cookies = Items(style_by_type("item", "Cookies de Noël"), 1, 15, "Vous détend et vous permet de gagner 15 points de vie.")
vodka = Items(style_by_type("item", "Bouteille de Vodka"), 3, 0, "Vous permet d'être plus confiant et de multiplier votre force par 3.")
#salle a manger
fois = Items(style_by_type("item", "Fois gras"), 1, 50, "Vous redonne tout vos points de vie")
biere_rouge = Items(style_by_type("item", "Bière aux fruits rouges"), 1, 1.5, "Vous permet d'être plus confiant et de multiplier votre force par 1,5.")
#salle de bain
miroir = Items(style_by_type("item", "Miroir"), 1, 0, "Je sais pas pourquoi j'ai ça. Faudrait vraiment être super narcissique pour se trimballer avec ça")
#jardin
velo = Items(style_by_type("item", "Vélo pour enfant"), 1, 0, "Comment est-ce que cela rentre dans mes poches ? Un mystère... Cela me servira peut-être plus tard")
cigarettes = Items(style_by_type("item", "Paquet de cigarettes & Briquet"), 1, 0, "Pourquoi j'ai ça ? Peut-être que ça me sera utile")

def take_item(list_items) :
    """Permet de prendre un item parmi une liste d'item, l'ajouter à son inventaire et le retirer de la liste"""
    global inventory
    print("Vous avez trouvé des objets.\nVoici la liste des objets :")
    i = 0
    while i < len(list_items) :
        print("[" + str(i + 1) + "]", list_items[i].name)
        i += 1
    choice = int(user_input("Quel objet souhaitez-vous prendre ? "))
    while choice < 0 or choice > len(list_items) :
        choice = int(user_input("Choisissez parmi les choix proposés : "))
    item = list_items[choice-1]
    inventory.add_item(item)
    del list_items[choice-1]
    print("Nouvel objet acquis :", item.name, "x1")
    return choice

def inventory_prompt(inventory) :
    if inventory.content == [] :
        print("Inventaire vide")
    else :
        print("")
        for item in inventory.content :
            print("[" + item.name + "] |", item.description)

###########################
### FONCTIONS DE COMBAT ###
###########################

class Character:
    def __init__(self, name, attack, health):
        self.name = name
        self.attack = attack
        self.health = health

grand_mere = Character("Grand-Mère", 15, 100)
grand_pere = Character("Grand-Père", 10, 50)
soeur = Character("Soeur", 5, 40)
chien = Character("le chien", 10, 40)

def use_item(player, win_item):
    global inventory
    i = 0
    print("Sélectionnez l'objet à utiliser")
    while i < len(inventory.content) :
        print("[" + str(i+1) + "]", inventory.content[i].name, "|", inventory.content[i].description)
        i += 1
    item_to_use = int(user_input("> ")) - 1
    while item_to_use < 0 or item_to_use > len(inventory.content) :
        item_to_use = int(user_input("Choisissez parmi les choix proposés : ")) - 1
    if inventory.content[item_to_use] == win_item :
        return player, True
    strenght = inventory.content[item_to_use].strenght
    health = inventory.content[item_to_use].health
    print("Vous avez utilisé " + inventory.content[item_to_use].name)
    inventory.del_item(inventory.content[item_to_use])
    player.attack *= strenght
    player.health += health
    if player.health > 50 :
        player.health = 50
    return player, False

def fight(mob, win_item, result):
    global inventory
    player = Character("Vous", 20, 50)
    print("Vous avez déclanché un combat contre " + mob.name)
    while mob.health > 0 and player.health > 0 :
        pass
        ### Action du joueur ###
        action = choice_action("Que voulez-vous faire ?", ["Attaquer", "Utiliser un objet"])
        ### Attaque ###
        if action == 1 :
            mob.health -= player.attack
            print("Vous attaquez " + mob.name + " avec une attaque et lui infligez " + str(player.attack) + " points de dégâts")
        ### Objet ###
        elif action == 2 :
            if inventory != [] :
                player, end_fight = use_item(player, win_item)
                if end_fight == True :
                    mob.health = 0
                    break
            else :
                print("Vous n'avez pas d'objet à utiliser.")
                continue
        ### Attaque du mob ###
        player.health -= mob.attack
        print(mob.name + " vous attaque et vous inflige " + str(mob.attack) + " points de dégâts")
    ### Fin du combat ###
    if mob.health <= 0:
        print("Vous avez battu " + mob.name + " !")
        result = True
    else:
        print("Vous avez perdu le combat face à " + mob.name + " !")
        loose()
    return result

####################################################
### CODE A EFFECTUER DANS LES DIFFERENTES SALLES ###
####################################################

def bibliotheque():
    global position
    global floor
    print("Vous êtes dans la bibliothèque de la maison.")
    while True:
        choice_1 = choice_action("Que souhaitez-vous faire ?", ["Parler", "Observer", "Se déplacer"])
        ### Parler ###
        if choice_1 == 1:
            print("Il n'y a personne dans la Bibliothèque.")
        ### Observer ###
        if choice_1 == 2:
            print("Vous analysez la pièce et observez une étagère avec des faux livres")
            choice_2 = choice_action("Souhaitez-vous manipuler les faux livres ?", ["Oui", "Non"])
            if choice_2 == 1:
                choice_3 = choice_action("Vous manipulez les livres et observez un mécanisme, souhaitez - vous l'actionner ?", ["Oui", "Non"])
                if choice_3 == 1:
                    choice_4 = choice_action("Une partie de la bibliothèque s’ouvre, souhaitez-vous emprunter le chemin ?", ["Oui", "Non"])
                    if choice_4 == 1 :
                        # changement de salle vers le cellier du rez de chaussee
                        position = "cellier"
                        floor = 0
                        cellier()
                        break
        ### Se déplacer ###
        else:
            break

def bureau():
    global fight_grandpere
    global position
    print("Vous êtes arrivé dans le bureau de votre grand-père, qui est présent dans la pièce.")
    while True:
        if fight_grandpere != True :
            choice_1 = choice_action("Que souhaitez-vous faire ?", ["Parler", "Observer", "Se déplacer"])
            ### Parler ###
            if choice_1 == 1:
                print("Vous : “ Bonsoir papy. Pourquoi t’es-tu enfermé dans ton bureau.\nGP : Parce-que je m'ennuie, sinon que fais-tu dans mon bureau.\nVous : Alphonso m’a dit qu'il y a un passage secret dans la maison. Est-ce vrai ?\nGrand-Père : Si tu veux le savoir tu devras me battre")
                choice_2 = choice_action("Souhaitez-vous vous battre ?", ["Oui", "Non"])
                if choice_2 == 1:
                    fight_grandpere = fight(grand_pere, None, None)
                    print("Grand-Père : Tu n’est plus un petit garçon, tu m’as battu, voilà la clé et le passage s’ouvre par le haut\nVous : Hein ?!\nGrand-Père: Bonne chance mon petit.\n\nPapy vous a viré de son bureau.")
                    inventory.add_item(cle)
                    position = "couloir"
                    couloir_etage()
                    break
            ### Observer ###
            elif choice_1 == 2:
                print("Vous avez observez aucun objet utile.")
            ### Se déplacer ###
            else:
                break
        else :
            choice_1 = choice_action("Que souhaitez-vous faire ?", ["Observer", "Se déplacer"])
            ### Observer ###
            if choice_1 == 1:
                print("Aucun objet utile est présent dans la pièce.")
            ### Se déplacer ###
            else:
                break

def cellier():
    global list_items_cellier
    global inventory
    print("Vous êtes dans le cellier.")
    while True:
        choice_1 = choice_action("Que souhaitez-vous faire ?", ["Observer", "Se déplacer"])
        ### Observer ###
        if choice_1 == 1:
            if list_items_cellier != [] :
                take_item(list_items_cellier)
            else :
                print("Aucun objet utile est présent dans la pièce.")
        ### Se déplacer ###
        else:
            break

def chambre_ami():
    global position_julia
    global position
    global inventory
    if position_julia == "chambre d'ami" :
        print("Vous vous trouvez dans la chambre d’amis, et vous voyez votre cousine Julia, qui semble allait très mal à cause de l’alcool, vous comprenez maintenant pourquoi on dit que l’alcool est dangereux pour la santé.")
        while True:
            choice_1 = choice_action("Que souhaitez-vous faire ?", ["Parler", "Observer", "Se déplacer", "Aider"])
            ### Parler ###
            if choice_1 == 1:
                print("Votre cousine Julia est trop morte pour communiquer.")
            ### Observer ###
            elif choice_1 == 2:
                print("Vous observez que votre cousine Julia est archi dans le mal.")
            ### Aider ###
            elif choice_1 == 4:
                #changement de salle du Joueur et de Julia
                position = "salle de bain"
                position_julia = "salle de bain"
                salle_de_bain()
                break
            ### Se déplacer ###
            else:
                break
    else :
        while True :
            choice_1 = choice_action("Que souhaitez-vous faire ?", ["Observer", "Se déplacer"])
            if choice_1 == 1:
                print("La chambre maintenant vide, vous remarquez une porte dans le fond de la chambre")
                choice_2 = choice_action("Souhaitez-vous emprunter la porte ?", ["Oui", "Non"])
                if choice_2 == 1 :
                    if cle in inventory.content :
                        print("Après avoir gravi l’échelle, vous êtes arrivés dans le Grenier. Vous pensiez voir de vieux meuble recouvert de draps, mais vous voyez une pièce magnifique avec un home cinéma, un frigo rempli de bière, de champagne et d’une bouteille d’eau, de placards qui débordent de nourriture. C’est alors que vous abandonnez l’idée de fuir et vous préférez passer votre soirée dans votre coin de paradis secret.")
                        win()
                    else :
                        print("La porte est fermé à clé. Peut-être que la clé est dans le bureau avec les autres clés...")
            else:
                break

def couloir_etage():
    print("Vous êtes dans le couloir de l'étage")

def couloir_1():
    global inventory
    print("Vous êtes dans le couloir sud du rez-de chaussée. Votre petit frère fou furieux est aussi dans le couloir.")
    while True:
        choice_1 = choice_action("Que souhaitez-vous faire ?", ["Parler", "Observer", "Se déplacer"])
        ### Parler ###
        if choice_1 == 1:
            print("Vous : “Alphonso que fais-tu ici ?\nAlphonso : Je m’ennuie à mourir, je n’ai rien à faire, maman m’a interdit de faire du vélo dans la maison, et je sais pas où il est. Si tu me le ramène, je te dirai un secret !!!")
            if velo in inventory.content :
                choice_2 = choice_action("Que faites-vous ?", ["Tiens j'ai ton " + velo.name, "Non, vas t'amuser ailleurs, et j’ai pas que ça à faire."])
                if choice_1 == 2:
                    inventory.del_item(velo)
                    print("Alphonso :Ooooh merci grand -frère !!! Tu savais qu’il y a un passage secret dans la maison, j’ai entendu papi le dire !")
                elif choice_2 == 2:
                    print("Alphonso : t'es le plus nul des grands-frères")
        ### Observer ###
        elif choice_1 == 2:
            print("Aucun objet utile est présent dans la pièce.")
        ### Se déplacer ###
        else:
            break

def couloir_2():
    global fight_soeur
    print("Vous êtes dans le couloir nord du rez-de chaussée. Votre sœur aînée narcissique vous bloque le passage au premier étage.")
    while True:
        if fight_soeur != True :
            choice_1 = choice_action("Que souhaitez-vous faire ?", ["Parler", "Observer", "Attaquer", "Se déplacer"])
            ### Parler ###
            if choice_1 == 1 :
                print("Soeur : Coucou petit frère, où vas-tu comme ça ? ")
                choice_3 = choice_action("Quelle réponse souhaitez-vous donner ?", ["Nulle part je voulais visiter juste visiter la maison", "Je veux aller à l’ étage"])
                if choice_3 == 1:
                    print("Soeur : Visite le Rez de Chaussé, maman à interdit l'accès au premier étage")
                elif choice_3 == 2:
                    print(" Soeur : Interdit, donc retourne dans le salon")
            ### Observer ###
            elif choice_1 == 2:
                print("Aucun objet utile est présent dans la pièce.")
            ### Attaquer ###
            elif choice_1 == 3:
                fight_soeur = fight(soeur, miroir, None)
            ### Se déplacer ###
            else:
                break
        else :
            choice_1 = choice_action("Que souhaitez-vous faire ?", ["Observer", "Se déplacer"])
            ### Observer ###
            if choice_1 == 1:
                print("Aucun objet utile est présent dans la pièce.")
            ### Se déplacer ###
            else:
                break

def cuisine():
    global list_items_cuisine
    print("Vous êtes dans la cuisine.")
    while True:
        choice_1 = choice_action("Que souhaitez-vous faire ?", ["Observer", "Se déplacer"])
        ### Observer ###
        if choice_1 == 1:
            if list_items_cuisine != [] :
                take_item(list_items_cuisine)
            else :
                print("Aucun objet utile est présent dans la pièce.")
        ### Se déplacer ###
        else:
            break

def hall_entree():
    print("Vous êtes arrivé dans le Hall d’entrée de la maison. Vous voyez votre grand-mère.")
    while True:
        choice_1 = choice_action("Que souhaitez-vous faire ?", ["Parler", "Observer", "Attaquer", "Se déplacer"])
        ### Parler ###
        if choice_1 == 1:
            print("Vous : Bonsoir Grand-mère, pourquoi n’es-tu pas dans le salon ? \nVotre grand-mère ne vous répond pas et utilise son regard intimidateur. Vous n’êtes pas assez confiant pour faire face à la doyenne, vous fuyez donc vers le salon.")
        ### Obeserver ###
        elif choice_1 == 2:
            print("Votre Grand-mère vous regarde trop mal. Vous avez peur")
        ### Attaquer ###
        elif choice_1 == 3:
            fight(grand_mere, None, None)
            sleep(5)
            os.system("cls")
            print("La porte maintenant non gardé vous laisse accès à la sortie. Content, vous sortez de la maison et profitez de votre paix dûrement acquise")
            win()
        ### Se déplacer ###
        else :
            break

def jardin():
    global fight_chien
    global list_items_jardin
    print("Vous êtes arrivé dans le jardin, vous voyez les chiens s’amuser autour du vélo de Alphonso.")
    while True:
        if fight_chien != True :
            choice_1 = choice_action("Que souhaitez-vous faire ?", ["Parler", "Observer", "Attaquer", "Se déplacer"])
            ### Parler ###
            if choice_1 == 1:
                print("Il n'y a personne dans le jardin et les chiens ça parlent pas.")
            ### Observer ###
            elif choice_1 == 2:
                if list_items_jardin != [] :
                    take_item(list_items_jardin)
                else :
                    print("Aucun objet utile est présent dans la pièce.")
            ### Attaquer ###
            elif choice_1 == 3:
                fight_chien = (chien, croquette, None)
            ### Se déplacer ###
            else:
                break
        else :
            choice_1 = choice_action("Que souhaitez-vous faire ?", ["Observer", "Se déplacer"])
            ### Observer ###
            if choice_1 == 1:
                print("Aucun objet utile est présent dans la pièce.")
            ### Se déplacer ###
            else:
                break

def salle_a_manger():
    global list_items_salle_a_manger
    print("Vous souhaitez dans la salle à manger, vous voyez la table recouverte de nourriture. ")
    while True:
        choice_1 = choice_action("Que souhaitez-vous faire ?", ["Observer", "Se déplacer"])
        ### Observer ###
        if choice_1 == 1:
            if list_items_salle_a_manger != [] :
                take_item(list_items_salle_a_manger)
            else :
                print("Aucun objet utile est présent dans la pièce.")
        ### Se déplacer ###
        else:
            break

def salle_de_bain():
    global position_julia
    global inventory
    if position_julia == "salle de bain" :
        print("Vous ramenez votre cousine au toilette, pour qu’elle puisse évacuer le plus d’alcool possible. Ensuite vous la ramenez dans la salle de bain, pour nettoyer son visage et essayer de la faire reprendre conscience.")
        while True:
            choice_1 = choice_action("Que souhaitez-vous faire ?", ["Parler", "Observer", "Se déplacer"])
            ### Parler ###
            if choice_1 == 1:
                print("Cousine Julia : “ Ooooh c’est toi, mais que tu es beau et mais qu’est ce tu fais là ??  Olalala mais tu sais j’ai trouvé un truc oufissime !!! Tu veux que je te dise c’est quoi !")
                choice_2 = choice_action("Que souhaitez-vous faire ?", ["Oui dis moi", "Non, vomis plutôt."])
                if choice_2 == 1:
                    print("Cousine Julia : R1 “ Aaaah je savais que ça allait t'intéresser !! Mais je veux que tu me ramènes de la bière parfum fruits rouges !")
                    if biere_rouge in inventory.content:
                        choice_3 = choice_action("Voulez-vous donner votre " + biere_rouge.name + " à Julia ?", ["Oui", "Non"])
                        if choice_3 == 1:
                            print("OOOOh ma bière !!! Go pour le second round. Bon chose promis chose dû. Genre j’ai trouvé une porte au niveau du plafond du dressing ! Une porte à l'arrière de la chambre, trop bizaaaaare !!!\nJ'ai essayé d'y rentrer mais c'était fermé à clé")
                        else :
                            print("T'es pas cool JB\n*buuuuuuuuuurrkkkk*")
                elif choice_2 == 2:
                    print("*buuuuuuuuuurrkkkk*")
            ### Observer ###
            if choice_1 == 2:
                print("Aucun objet utile est présent dans la pièce.")
            ### Se déplacer ###
            else:
                break
    else :
        while True:
            choice_1 = choice_action("Que souhaitez-vous faire ?", ["Observer", "Se déplacer"])
            ### Observer ###
            if choice_1 == 1:
                print("Aucun objet utile est présent dans la pièce.")
            ### Se déplacer ###
            else:
                break

def salle_de_jeux():
    global cigarettes_mere
    global position
    print("Vous êtes arrivé dans la salle de jeu, votre mère et tante sont en train de jouer une partie d’échec. Soudainement votre mère vous interpelle énervé : \"Retourne dans le salon !\"")
    if cigarettes in inventory.content and cigarettes_mere != True:
        while True:
            choice_1 = choice_action("Que souhaitez-vous faire ?", ["Donner " + cigarettes.name + " à votre mère", "Observer", "Se déplacer"])
            ### Parler ###
            if choice_1 == 1:
                inventory.del_item(cigarettes)
                print("Merci mon grand, j’étais à cran depuis tout à l’heure parce que je n’arrivais pas à trouver ce foutu paquet. Qu’est ce que tu veux ?")
                choice_2 = choice_action("Quelle réponse souhaitez-vous donner ?", ["Vous : “Tu sais où est papi ?", "Pourquoi la porte du bureau est-elle fermée ?"])
                if choice_2 == 1:
                    print("Papi est dans son bureau.")
                elif choice_2 == 2:
                    print("Papi est dans son bureau c’est pour ça que la porte est fermée. Tu veux le voir ?")
                    choice_3 = choice_action("Quelle réponse souhaitez-vous donner ?", ["Oui", "Non"])
                    if choice_3 == 1:
                        print("Tu peux juste passer par cette porte, ton grand-père est juste derrière")
                        position = "bureau"
                        bureau()
                        break
            ### Observer ###
            elif choice_1 == 2:
                print("Vous avez observez aucun objet utile.")
            ### Se déplacer ###
            else:
                break
    else :
        while True :
            choice_1 = choice_action("Que souhaitez-vous faire ?", ["Parler", "Observer", "Se déplacer"])
            ### Observer ###
            if choice_1 == 1:
                print("Vous avez observez aucun objet utile.")
            ### Se déplacer ###
            else:
                break

def salon():
    global list_items_salon
    print("Vous êtes dans le Salon, dans la pièce se situe ton oncle John, ton cousin Johnny et ta cousine Julia.")
    while True:
        choice_1 = choice_action("Que souhaitez-vous faire ?", ["Parler", "Observer", "Se déplacer"])
        ### Parler ###
        if choice_1 == 1:
            choice_2 = choice_action("À qui souhaitez-vous parler ?", ["Oncle John", "Cousin Jonny"])
            ### Oncle John ###
            if choice_2 == 1:
                print("Oncle John : Bonsoir Jean-Baptiste, Joyeux Noël ! J’espère que le père noël t’as ramené les cadeaux que tu souhaitais.\nVous :")
                choice_3 = choice_action("Quelle réponse souhaitez-vous donner ?", ["Tonton j’ai 19 ans, je sais que père le noël n’existe pas", "HAHAHA, j’espère que toi aussi"])
                if choice_3 == 1:
                    print("Oncle John : C’est vrai que tu es un homme maintenant, en tout cas profite bien de la soirée.")
                elif choice_3 == 2:
                    print("Oncle John : Ah si seulement mon fils avait le même humour que toi,  en tout cas profite bien de la soirée.")
            ### Cousin Johnny ###
            elif choice_2 == 2:
                print("Cousin Johnny : Salut Joyeux-Noël à toi, comment tu vas ?\nVous : “ça va bien et toi ?\nCousin Johnny : Je m’ennuie à mourir, mais nos mères nous ont interdit de quitter la propriété. J’aurai bien voulu fuir par un passage secret et partir voir mes potes et m’amuser. Bon je te laisse je vais tenter cette ennuyeuse soirée avec de l’alcool et des petits fours.")
        ### Observer ###
        elif choice_1 == 2:
            if choice_1 == 2:
                if list_items_salon != []:
                    take_item(list_items_salon)
                else:
                    print("Aucun objet utile est présent dans la pièce.")
        ### Se déplacer ###
        else:
            break

def room_content(position) :
    # Execute une des fonctions du dessus en fonction de la position
    if position == "bibliotheque" :
        bibliotheque()
    elif position == "bureau":
        bureau()
    elif position == "cellier":
        cellier()
    elif position == "chambre d'ami" :
        chambre_ami()
    elif position == "couloir" : #couloir de l'étage
        couloir_etage()
    elif position == "couloir 1" :
        couloir_1()
    elif position == "couloir 2" :
        couloir_2()
    elif position == "cuisine" :
        cuisine()
    elif position == "entree" :
        hall_entree()
    elif position == "jardin" :
        jardin()
    elif position == "salle a manger" :
        salle_a_manger()
    elif position == "salle de bain" :
        salle_de_bain()
    elif position == "salle de jeux" :
        salle_de_jeux()
    elif position == "salon" :
        salon()
    else :
        print("error")

##############################
### NAVIGATION DANS LA MAP ###
##############################

def navigation_condition(map, actual_position, wanted_position) :
    global fight_soeur
    if wanted_position == "bureau" and actual_position == "couloir 2" :
        print("La porte du " + style_by_type("place", "bureau") + " est fermée de l'intérieur.")
    # Ajouter les autres interdictions d'accès
    elif wanted_position == "chambre des parents" :
        print("La porte de la " + style_by_type("place", "chambre des parents") + " est fermée à clé.")
    elif wanted_position == "toilettes" :
        print("Les " + style_by_type("place", "toilettes") + " sont fermées, elles ont l'air d'être occupées.")
    elif wanted_position == "escalier" and fight_soeur != True:
        print("Votre soeur garde les " + style_by_type("place", "escaliers") + ".")
    else :
        actual_position = wanted_position
    return actual_position

def change_floor(floor) :
    if floor == 0 :
        floor = 1
        new_position = "couloir" #salle ayant accès à l'escalier de l'étage
    elif floor == 1 :
        floor = 0
        new_position = "couloir 2" #salle ayant accès à l'escalier du rdc
    return new_position, floor

def navigation(map) :
    global position, floor
    blank_screen()
    # affichage de la liste des chemins possibles
    i = 1
    for path in map[floor][position]["access_from"] :
        print("[" + str(i) + "]", map[floor][path]["access_prompt"])
        i += 1
    # choix du chemin à prendre
    choice = int(user_input("\nOù souhaitez-vous aller ? ")) - 1
    while choice < 0 or choice >= len(map[floor][position]["access_from"]) :
        choice = int(user_input("Choisissez parmis les chemins proposés : ")) - 1
    new_position = map[floor][position]["access_from"][choice]
    # changement de salle dans le cas de l'escalier
    # vérification des droites d'accès à la pièce
    new_position = navigation_condition(map, position, new_position)
    # vérification d'un changement de salle
    if position == new_position :
        room_content(position)
    else :
        if new_position == "escalier" :
            new_position,floor = change_floor(floor)
        position = new_position
        blank_screen()
        room_content(position) # execution du contenu de la salle
    if position == "entree" or position == "sortie du jardin":
        return
    navigation(map)

#Definition de la map

map = {
    0: { #ETAGE 0 : REZ DE CHAUSSEE (dans l'ordre alphabétique)
        "bureau": {
            "access_prompt": "Rentrer dans le " + style_by_type("place", "bureau"),
            "access_from": ["couloir 2", "salle de jeu"]
        },
        "cellier": {
            "access_prompt": "Rentrer dans le " + style_by_type("place", "cellier"),
            "access_from": ["cuisine", "sortie arriere"],
        },
        "couloir 1": {
            "access_prompt": "Aller dans le " + style_by_type("place", "premier couloir"),
            "access_from" : ["cuisine", "entree", "toilettes", "salon"]
        },
        "couloir 2": {
            "access_prompt": "Aller dans le " + style_by_type("place", "deuxième couloir"),
            "access_from": ["bureau", "escalier", "salle a manger", "salle de jeu", "salon"]
        },
        "cuisine": {
            "access_prompt": "Rentrer dans la " + style_by_type("place", "cuisine"),
            "access_from": ["cellier", "couloir 1", "salle a manger", "salon"]
        },
        "entree": {
            "access_prompt": "Prendre la " + style_by_type("place", "porte d'entrée")
        },
        "jardin": {
            "access_prompt": "Aller dans le " + style_by_type("place", "jardin"),
            "access_from": ["salle a manger"]
        },
        "salon": {
            "access_prompt": "Rentrer dans le " + style_by_type("place", "salon"),
            "access_from": ["couloir 1", "couloir 2", "cuisine"]
        },
        "salle a manger": {
            "access_prompt": "Accéder à la " + style_by_type("place", "salle à manger"),
            "access_from": ["couloir 2", "cuisine", "jardin"]
        },
        "toilettes": {
            "access_prompt": "Rentrer dans les " + style_by_type("place", "toilettes"),
            "access_from": ["couloir 1"],
        },
        "salle de jeu": {
            "access_prompt": "Rentrer dans la " + style_by_type("place", "salle de jeu"),
            "access_from": ["bureau", "couloir 2"]
        },
        #ESCALIER
        "escalier": { # Envoie à l'autre etage
            "access_prompt": "Prendre l'" + style_by_type("place", "escalier")
        }
    },
    1: { #ETAGE 1 (dans l'ordre alphabétique)
        "bibliotheque": {
            "access_prompt": "Rentrer dans la " + style_by_type("place", "bibliothèque"),
            "access_from": ["couloir"]
        },
        "couloir": {
            "access_prompt": "Aller dans le " + style_by_type("place", "couloir"),
            "access_from": ["bibliotheque", "chambre d'ami", "escalier", "chambre des parents", "salle de bain"]
        },
        "chambre d'ami": {
            "access_prompt": "Rentrer dans la " + style_by_type("place", "chambre d'ami"),
            "access_from": ["couloir"]
        },
        "chambre des parents": { # Espace non accessible
            "access_prompt": "Rentrer dans la " + style_by_type("place", "chambre des parents")
        },
        "salle de bain": {
            "access_prompt": "Rentrer dans la " + style_by_type("place", "salle de bain"),
            "access_from": ["couloir"]
        },
        #ESCALIER
        "escalier": { # Envoie à l'autre etage
            "access_prompt": "Prendre l'" + style_by_type("place", "escalier")
        }
    }
}

#################
### EXECUTION ###
#################

session_name, position, floor, list_items_cellier, list_items_cuisine, list_items_salle_a_manger, list_items_salon, list_items_jardin, position_julia, fight_soeur, fight_grandpere, fight_chien, cigarettes_mere = main_menu()
# Le menu est appelé comme ça afin de pouvoir créer à l'avenir une fonction de sauvegarde (toutes ces variables sont celles qui garde l'historique de progression du joueur

if session_name != None :
    print("Vous en avez mare de ces fêtes de famille, votre but est de vous échapper de la maison ou bien de trouver un endroit assez calme pour passer un reste de soirée paisible.\nLe problème, c'est que votre grand-mère n'a pas l'air de vouloir vous laisser partir")
    sleep(10)
    blank_screen()
    room_content(position)
    navigation(map)