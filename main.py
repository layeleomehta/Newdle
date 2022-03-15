import itertools
from nltk.corpus import wordnet 
from nltk.corpus import words
from random_word import RandomWords

# returns a randomly generated 5 letter English word
def generate_word():
    r = RandomWords()
    new_word = r.get_random_word(minLength=5, maxLength=5)
    new_word = new_word.lower()

    return new_word


# return True if input word is a valid English word, False otherwise.  
def validate_word(word):
    if(word in wordnet.words() and words.words().__contains__(word)):
        return True
    else:
        return False

# returns list of all valid English permutations of input word; starting from length 3 to length of word. 
def make_valid_permutations(word):
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

# generates random 5 letter word, finds all valid English permutations
# returns a tuple of the random word, a list of valid combinations and number of combinations. 
def main():
    output = []
    word = ""
    num_valid_words = 0

    while(num_valid_words < 3 or num_valid_words > 7):
        word = generate_word()
        output = make_valid_permutations(word)
        num_valid_words = len(output)
    
    return (word, output, num_valid_words)

if __name__ == "__main__":
    word, output, num_valid_words = main()
    print("Word:", word)
    print("All combinations:", output)
    print("Number of combinations:", num_valid_words)