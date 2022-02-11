from wordcreate import Word

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

        self.letter_options = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "u", "x", "y", "z"]
        self.letter_guesses = []
    
        self._letter = ""

    def compare(self):
        """Gets the letter from the input function in terminal_services and
        and compares to the letters in word from wordcreate
        
        Returns
            letter is revealed if guess is correct; 
            'incorrect guess' is revealed if not correct""" 
        word = Word()
        wordlist = list(word._get_word)
        for i in wordlist:
            print(list(i))

        if self in word:
            print("Correct")
            return self
        else:
            print("Incorrect")

    # I was thinking by checking the self (letter) in(against) word (wordcreate()) we would then
    # return the letter so that in a separate function we could collect all the correct guesses (maybe in a list) and 
    # then print the correct letters ... but I don't know how to print them in the correct order of the word, instead
    # of the list order. Thoughts? 
test = Letter()
print(test.compare())