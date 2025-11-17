# Define the Room class.


class Room:
    """
      Représente un lieu dans le jeu d'aventure.
    
    Un lieu possède un nom, une description et des sorties vers d'autres lieux.
    Les sorties sont stockées dans un dictionnaire reliant les directions (N, E, S, O) 
    aux autres instances de Room.
    
    Attributes:
        name (str): Le nom du lieu
        description (str): La description détaillée du lieu  
        exits (dict): Dictionnaire des sorties {direction: Room}
        
    Methods:
        get_exit(direction): Retourne la Room dans la direction ou None
        get_exit_string(): Retourne une string des sorties disponibles
        get_long_description(): Retourne la description complète avec sorties
    """

    # Define the constructor. 
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}
    
    # Define the get_exit method.
    def get_exit(self, direction):

        # Return the room in the given direction if it exists.
        if direction in self.exits.keys():
            return self.exits[direction]
        else:
            return None
    
    # Return a string describing the room's exits.
    def get_exit_string(self):
        exit_string = "Sorties: " 
        for exit in self.exits.keys():
            if self.exits.get(exit) is not None:
                exit_string += exit + ", "
        exit_string = exit_string.strip(", ")
        return exit_string

    # Return a long description of this room including exits.
    def get_long_description(self):
        return f"\nVous êtes dans {self.description}\n\n{self.get_exit_string()}\n"
