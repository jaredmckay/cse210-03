# from game.wordcreate import ""
# from game.letterguess import ""
# from game.terminal_service import ""

class Director:
    """ A person who directs the game. 
    
    The resonsibilit of a director is to control the sequence of play

    Attributes:
        create work (wordcreate): creates the word to guess
        is_playing (boolean): Whether or not to keepp playing.
        letter guess (letterguess) guesses a letter in the word
        terminal_serice: for getting and displaying information on the terminal
    
    """
    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        pass

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _get_inputs(self):
        """Moves the seeker to a new location.

        Args:
            self (Director): An instance of Director.
        """
        pass
        
    def _do_updates(self):
        """Keeps watch on where the seeker is moving.

        Args:
            self (Director): An instance of Director.
        """
        pass
        
    def _do_outputs(self):
        """Provides a hint for the seeker to use.

        Args:
            self (Director): An instance of Director.
        """
        pass