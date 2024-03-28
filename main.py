# Made by @ Insur

from colorama import init, Fore

init()

def print_ascii(ascii_art):
    gradient = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]
    gradient_length = len(gradient)
    lines = ascii_art.split('\n')
    
    for i, line in enumerate(lines):
        color = gradient[i % gradient_length]
        print(color + line)
        
ascii_art = """
  _____                      
 |_   _|                     
   | |  _ __  ___ _   _ _ __ 
   | | | '_ \/ __| | | | '__|
  _| |_| | | \__ \ |_| | |   
 |_____|_| |_|___/\__,_|_|   

"""

def pendu():
    mot_a_deviner = "nyo"
    lettres_trouves = []
    essais_restants = 7

    print("Bienvenue sur le jeu du pendu !")
    
    while essais_restants > 0:
        mot_affiche = ""
        for lettre in mot_a_deviner:
            if lettre in lettres_trouves:
                mot_affiche += lettre
            else:
                mot_affiche += "_"
            
        if mot_affiche == mot_a_deviner:
            print("Bravo ! Vous avez trouvé le mot ! Mot a deviné :", mot_a_deviner)
            break

        print("Mot a deviner :", mot_affiche)
        print("Essais restants :", essais_restants)
        
        proposition = input("Veuillez saisir une proposition : ").lower()
        
        if proposition in lettres_trouves:
            print("Vous avez déja saisi cette lettre !")
        elif proposition in mot_a_deviner:
            print("Bonne devinette ! La lettre", proposition, "est dans le mot !")
            
            lettres_trouves.append(proposition)
        else:
            print("Désolé ! La lettre", proposition, "n'est pas dans le mot !")
            essais_restants -= 1
            
        if essais_restants == 0:
            print("Vous avez perdu ! Le mot était :", mot_a_deviner)
            break

print_ascii(ascii_art)
pendu()