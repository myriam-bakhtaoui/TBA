# Description: Game class

# Import modules

from room import Room
from player import Player
from command import Command
from actions import Actions

class Game:

    # Constructor
    def __init__(self):
        self.finished = False
        self.rooms = []
        self.commands = {}
        self.player = None
        self.valid_directions = set()
        self.direction_map = {}
    
    # Setup the game
    def setup(self):

        # Setup commands

        help = Command("help", " : afficher cette aide", Actions.help, 0)
        self.commands["help"] = help
        quit = Command("quit", " : quitter le jeu", Actions.quit, 0)
        self.commands["quit"] = quit
        go = Command("go", " <direction> : se déplacer dans une direction cardinale ou sur les étages (N, E, S, O, U, D)", Actions.go, 1)
        self.commands["go"] = go
        
        # Setup rooms

        source = Room("source enchantée", "Ici se trouvais autrefois la demeure du roi dragon de l'eau bien que sa présence ne soit plus sa magie perdure on dit que l'eau dans la SOURCE ENCHANTE a des vertus incomparable.")
        self.rooms.append(source)
        
        caverne = Room("caverne cristaline", "Une caverne mystérieuse avec des cristaux lumineux incrustés dans les murs vous voici dans la CAVERNE CRISTALINE.")
        self.rooms.append(caverne)
        
        pont = Room("pont de lianes", "Une traversée qui semble si facile...trop paisible pour être vrai, ce PONT DES LIANES n'annonce rien de bon")
        self.rooms.append(pont)
        
        grotte = Room("grotte aux champi", "DES CHAMPI! PLEIN DE CHAMPI!Dans la GROTTE DES CHAMPI Que de couleurs et de parfums lequelles pourrais-je bien manger?")
        self.rooms.append(grotte)
        
        soubassement = Room("Soubassemnt Mystérieux", "Un passage clame et frais sous la terre, avec des racines qui pendent du plafond, des voix murmure ... elle semble vous guider à travers ce SOUBASSEMENT MYSTERIEUX.")
        self.rooms.append(soubassement)
        
        temple = Room("Temple Oublié", "De la lumière voilà le temple qui depuis longtemps n'a pas reçu de visiteurs bienvenue humble humain Dans le TEMPLE OUBLIE.")
        self.rooms.append(temple)
        
        sanctuaire = Room("Sanctuaire D'Alone", "... Alors que la vie commence dans la lumière, ici elle se termine, c'est dans le TEMPLE D'ALONE que vous vous trouvez.")
        self.rooms.append(sanctuaire)
        
        sentier = Room("Sentier Moussues", "Un étroit SENTIER sinueux bordé de vieux arbres. La mousse épaisse recouvre le sol, et une brume légère flotte entre les troncs." )
        self.rooms.append(sentier)
        
        antre = Room("Antres du vieux Blaireau","un terrier qui ressemble à une petite boutique. Des étagères en racines alignent des pots soigneusement étiquetés. Le Vieux Blaireau, un nœud papillon de feuille mal attaché autour du cou, échappe une poignée de glands en vous voyant. 'Ahem! Bienvenue dans mon établissement... Ne regardez pas le désordre, c'est stratégique!'")
        self.rooms.append(antre)
        
        maison = Room("Maison du maître ", "Un refuge qui ressemble à une caserne bien tenue. Les étagères sont rigoureusement organisées, les potions alignées par taille, et une armure immaculée trône au centre. Votre Maître Druide, une femme au port altier et aux yeux déterminés, croise les bras. 'Enfin. J'ai peu de temps à t'accorder - la forêt dépérit et seul le Dragon peut la sauver.' Elle parle avec autorité, mais son poing se serre légèrement, trahissant une inquiétude qu'elle tente de masquer.")
        self.rooms.append(maison)
        
        foret = Room("Forêt des Anciens","Une sylve sacrée où le temps semble s'être arrêté. Les chênes ancestraux, aux écorces gravées de runes à moitié effacées, forment une voûte si haute qu'elle semble toucher le ciel. Des lucières dansent entre les branches, guidant ou égarant les voyageurs. On y perçoit le poids des mémoires accumulées - cette forêt se souvient de tout.")
        self.rooms.append(foret)
        
        chene = Room("Grand Chêne","Un colosse végétal dont l'écorce luit faiblement d'une lueur argentée. Les racines, normalement souterraines, forment ici une cage de bois vivant autour d'un œuf de pierre, certaines racines étant ternes et craquelées. L'arbre émane une autorité silencieuse, mais on devine une lutte interne - la puissance millénaire contrainte par une faiblesse insidieuse.")
        self.rooms.append(chene)
        
        clairiere= Room("Clairière du Dragon", "Un cercle parfait où l'herbe a cédé la place à du cristal pur. La statue du dragon de pierre, haute de dix mètres, domine l'espace de sa silhouette majestueuse et tragique. Des fissures parcourent son corps de granit, et une brume argentée s'échappe de ses narines. On dirait qu'il retient son souffle, prêt à s'éveiller au bon signal.")
        self.rooms.append(clairiere)
        
        pantheon = Room("Panthéon du Dragon de Piere", "Un sanctuaire Aérien où les murs sont sculptés de bas-reliefs racontant l'histoire du Dragon de Pierre. Des torches éternelles jettent une lumière dansante sur les fresques, révélant des scènes de gloire et de chute.")
        self.rooms.append(pantheon)
        

        # Create exits for rooms

        source.exits = {"N": None, "E": caverne, "S": None, "O": None, "U": None, "D": None}
        caverne.exits = {"N": None, "E": None, "S": pont, "O": source, "U": None, "D": None}
        pont.exits = {"N": sentier, "E": foret, "S": grotte, "O": caverne, "U": None, "D": None}
        grotte.exits = {"N": pont, "E": soubassement, "S": None, "O": None, "U": None, "D": None}
        soubassement.exits = {"N": None, "E": None, "S": None, "O": grotte, "U": temple, "D": sanctuaire}
        temple.exits = {"N": None, "E": None, "S": None, "O": None, "U": None, "D": soubassement}
        sanctuaire.exits = {"N": None, "E": None, "S": None, "O": None, "U": None, "D": None}
        sentier.exits = {"N": maison, "E": None, "S": pont, "O": antre, "U": None, "D": None}
        antre.exits = {"N": None, "E": sentier, "S": None, "O": None, "U": None, "D": None}
        maison.exits = {"N": None, "E": None, "S": sentier, "O": None, "U": None, "D": None}
        foret.exits = {"N": None, "E": chene, "S": pont, "O": None, "U": clairiere, "D": None}
        chene.exits = {"N": None, "E": None, "S": None, "O": foret, "U": None, "D": None}
        clairiere.exits = {"N": None, "E": pantheon, "S": None, "O": None, "U": None, "D":foret}
        pantheon.exits = {"N": None, "E": None, "S": None, "O": clairiere, "U": None, "D": maison}

        # Setup player and starting room

        self.player = Player(input("\nEntrez votre nom: "))
        self.player.current_room = maison
        
        for room in self.rooms:
            self.valid_directions.update(room.exits.keys())
        # Setup direction map
        for d in self.valid_directions:
            self.direction_map[d] = d
        self.direction_map.update({
            "NORD": "N",
            "SUD": "S",
            "EST": "E",
            "OUEST": "O",
            "UP": "U",
            "DOWN": "D",
        })
        # Normaliser les clés pour correspondre à la normalisation
        self.direction_map = {k.casefold(): v for k, v in self.direction_map.items()}

    # Play the game
    def play(self):
        self.setup()
        self.print_welcome()
        # Loop until the game is finished
        while not self.finished:
            # Get the command from the player
            self.process_command(input("> "))
        return None

    # Process the command entered by the player
            
    def process_command(self, command_string) -> None:
        list_of_words = command_string.split(" ")
        command_word = list_of_words[0]
        if command_word == "":
            return
        elif command_word in self.commands:
            command = self.commands[command_word]
            command.action(self, list_of_words, command.number_of_parameters)
        else:
            print(f"\nCommande '{command_word}' non reconnue. Tapez 'help' pour l'aide.\n")


    # Print the welcome message
    def print_welcome(self):
        print(f"\nBienvenue {self.player.name} dans ce jeu d'aventure !")
        print("Entrez 'help' si vous avez besoin d'aide.")
        #
        print(self.player.current_room.get_long_description())
    

def main():
    # Create a game object and play the game
    Game().play()
    

if __name__ == "__main__":
    main()
