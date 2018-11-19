shape = """
   __\n  |  |\n  |\n  |\n-----\n|   |
"""

class Words(object):

    """In this class we will read all of the words from a text file"""

    def __init__(self, file='words.txt'):
        #self.word_lst = _read_word_list(file)
        self.file = file
        self.word_lst = self.read_word_list(self.file)


    def read_word_list(self, file='words.txt'):
        with open(file, 'r') as myfile:
            word_list = [x.strip().lower() for x in myfile]
        return word_list

words = Words('CollinsScrabbleWords_2015.txt')

def secret_word():

    tgt_word = input("what is your secret word?> ").lower()
    print('\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n')

    while True:
        if tgt_word in words.word_lst:
            break
        print("That word was not in the dictionary please try again")
        tgt_word = input("what is your secret word?> ")
    return tgt_word
