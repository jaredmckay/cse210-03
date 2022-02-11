import random



class Word:


    """ 
    class takes Word form the list and provides it at random for game
    for user to guess 

    """
    words = ['straw', 'fate', 'eye', 'ring', 'bay', 'mind', 'golf', 'nun', 'game', 'slab', 'break', 'lunch', 'care', 'blow', 'score', 'paint', 'job', 'school', 'jump', 'blue']


    def __init__(self):

        
        """
        Constructer function 
        full word from list function put the list in this function

        """
        self.words = ['straw', 'fate', 'eye', 'ring', 'bay', 'mind', 'golf', 'nun', 'game', 'slab', 'break', 'lunch', 'care', 'blow', 'score', 'paint', 'job', 'school', 'jump', 'blue']

        # self.words = words
        # print(random.choice(self.words))
        # self.value = random.choice(self.words)
        # return self.value
        

    def _get_word(self):    
        """ 
        returns the selected word
        """
        chose_word = random.choice(self.words)
        return chose_word

print("hello")
words = Word()
print(words._get_word())