import random


class Word:


    """ 
    class takes Word form the list and provides it at random for game
    for user to guess 

    """
    # words = ['straw', 'fate', 'eye', 'ring', 'bay', 'mind', 'golf', 'nun', 'game', 'slab', 'break', 'lunch', 'care', 'blow', 'score', 'paint', 'job', 'school', 'jump', 'blue']


    def __init__(self):

        
        """
        Constructer function 
        full word from list function put the list in this function

        """

        self.words = ['straw', 'fate', 'eye', 'ring', 'bay', 'mind', 'golf', 'nun', 'game', 'slab', 'break', 'lunch', 'care', 'blow', 'score', 'paint', 'job', 'school', 'jump', 'blue']
        # self.value = random.choice(words)
        # return self.value
        

    def getword(self):    
        """ 
        returns the selected word
        """
        word_index = random.randint(1, len(self.words))
        self.current_word = self.words[word_index -1]
        print(self.current_word)

# to test if random word is picked:
Word.getword(self.current_word)