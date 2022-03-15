""" Python script to test functionality """

# need to use some kind of backtracking approach to generate all possible combinations of words
def make_combinations(word):
    len_word = len(word)
    combos = []

    # all subword combinations
    for i in range(0, len_word):
        tempStr = ""
        for j in range(i, len_word):
            tempStr += word[j]
            combos.append(tempStr)
    
    return combos

def main():
    word = "fancy"
    wordList = list(word)
    print(wordList)


if __name__ == "__main__":
    main()