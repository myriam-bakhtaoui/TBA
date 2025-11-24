# Define the Player class.
class Player():
    """ 
    Représente le joueur dans le jeu d'aventure.
    
    Le joueur possède un nom et une position actuelle dans le monde du jeu.
    Il peut se déplacer entre les différentes salles via les sorties disponibles.
    
    Attributes:
        name (str): Le nom du joueur
        current_room (Room): La salle actuelle du joueur
        
    Methods:
        move(direction): Tente de déplacer le joueur vers une direction donnée
    """
    
    # Define the constructor.
    def __init__(self, name):
        self.name = name
        self.current_room = None
    
    # Define the move method.
    def move(self, direction):
        
        
        # Get the next room from the exits dictionary of the current room.
        next_room = self.current_room.exits[direction]
       

        # If the next room is None, print an error message and return False.
        if next_room is None:
            print("\nTu es rentré(e) dans un mur il n'y a aucune porte dans cette direction !\n")
            return False
        
        # Set the current room to the next room.
        self.current_room = next_room
        print(self.current_room.get_long_description())
        return True

    