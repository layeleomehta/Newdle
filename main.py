""" Python script to test functionality """

import itertools

# generate all permutations of input word; starting from length 3 to length of word. 
def make_word_permutations(word):
    if(len(word) <= 2):
        print("Please input a word with length greater than 2 letters")
        return

    wordList = list(word)
    combos = set()

    for i in range(0, len(wordList)+1):
        for subset in itertools.permutations(wordList, i):
            str_subset = "".join(subset)
            if(len(str_subset) > 2 and str_subset != word):
                combos.add(str_subset)
    return list(combos)

def main():
    word = "fancy"
    print(make_word_permutations(word))

    


if __name__ == "__main__":
    main()