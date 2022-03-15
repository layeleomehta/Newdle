""" Python script to test functionality """

import itertools
from nltk.corpus import wordnet 
from nltk.corpus import words


# returns list of all permutations of input word; starting from length 3 to length of word. 
def make_word_permutations(word):
    if(len(word) <= 2):
        print("Please input a word with length greater than 2 letters")
        return
    
    word = word.lower()
    wordList = list(word)
    combos = set()

    for i in range(3, len(wordList)+1):
        for subset in itertools.permutations(wordList, i):
            str_subset = "".join(subset)
            if(validate_word(str_subset) and str_subset != word):
                combos.add(str_subset)

    return list(combos)

# return True if input word is a valid English word, False otherwise.  
def validate_word(word):
    if(word in wordnet.words() and words.words().__contains__(word)):
        return True
    else:
        return False

def main():
    word = "cabin"
    print(make_word_permutations(word))

    


if __name__ == "__main__":
    main()