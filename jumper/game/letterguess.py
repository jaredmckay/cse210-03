class Letter:
    """
    letter to be compared to provided word

    """

    def __init__(self):
        """
        new constructor

        atrribute:
        self (letter): an instance of Letter.


        """
        self._letter = ""

    def compare(self, word):
        """Gets the letter from the input function in terminal_services and
        and compares to the letters in word from wordcreate
        
        Returns:
            letter is revealed if guess is correct; 
            'incorrect guess' is revealed if not correct"""
        
        if self in word:
            print("Correct")
            return self
        else:
            print("Incorrect")

    # I was thinking by checking the self (letter) in(against) word (wordcreate()) we would then
    # return the letter so that in a separate function we could collect all the correct guesses (maybe in a list) and 
    # then print the correct letters ... but I don't know how to print them in the correct order of the word, instead
    # of the list order. Thoughts? 
