from math import log

input_file_path = 'cleaned_wordle_words.txt'

dictionary = open(input_file_path, 'r')

char_not_in_word = ''
char_in_word = ''

def read_in_dict(file):
    words = []
    for line in file:
        words.append(line.strip())
    return words

# go through the dictionary and find the words that have the given characters
def words_with_letters(letters, dictionary):
    if len(letters) == 0: return dictionary

    num_letters = len(letters)
    valid_words = []
    for word in dictionary:
        word = word.strip()
        match_amount = 0
        for letter in letters:
            if letter in word:
                match_amount += 1
            if match_amount == num_letters:
                valid_words.append(word)
    
    return valid_words

def words_without_letters(letters, dictionary):
    if len(letters) == 0: return dictionary 

    valid_words = []
    for word in dictionary:
        word = word.strip()
        is_valid = True
        for letter in letters:
            if letter in word:
                is_valid = False
                break
        if is_valid:
            valid_words.append(word)
    
    return valid_words

def words_with_letter_positions(guess, dictionary):
    match_amount = 0
    for letter in guess:
        if letter != "_": match_amount += 1
    if match_amount == 0: return dictionary
    if len(dictionary) == 0: return dictionary

    valid_words = []
    for word in dictionary:
        word = word.strip()
        match = 0
        for i, letter in enumerate(guess):
            if letter == "_":
                continue
            if word[i] == letter:
                match += 1
            if match == match_amount:
                valid_words.append(word)
                continue
    return valid_words

''' this funcion takes a dictionary like this
dictionary = {
    'a' : [False, False, False, False, False],
    'b' : [False, True, False, False, False]
}
'''

def words_letter_not_position(guess, dictionary):
    if len(guess) == 0: return dictionary
    valid_words = []
    for word in dictionary:
        match = 5
        for letter in guess:
            for i, value in enumerate(guess[letter]):
                if word[i] == letter and value == True:
                    match -= 1
                #print(word, word[i], letter, i, value, match)
        if match == 5:
            valid_words.append(word)
    return valid_words

def get_dict_stats(dictionary):
    letter_occurrences = {'a' : 0,
    'b' : 0,'c' : 0,'d' : 0,'e' : 0,'f' : 0,
    'g' : 0,'h' : 0,'i' : 0,'j' : 0,'k' : 0,
    'l' : 0,'m' : 0,'n' : 0,'o' : 0,'p' : 0,
    'q' : 0,'r' : 0,'s' : 0,'t' : 0,'u' : 0,
    'v' : 0,'w' : 0,'x' : 0,'y' : 0,'z' : 0}
    if len(dictionary) == 0: return letter_occurrences
    letter_count = 0
    for word in dictionary:
        word = word.strip()
        for letter in word:
            letter_count += 1
            if letter in letter_occurrences:
                letter_occurrences[letter] += 1
    for letter in letter_occurrences:
        letter_occurrences[letter] = letter_occurrences[letter] / letter_count
        
    return letter_occurrences

def get_entropy(guess, dict_stats):
        percentage = 0
        used_letters = []
        for letter in guess:
            if letter in used_letters:
                continue
            percentage += dict_stats[letter]
            used_letters.append(letter)
        return log(1/percentage,2)

def entropy_sort_list(dictionary, dict_stats):
    # sort valid_words according to entropy
    return dictionary.sort(key=lambda word: get_entropy(word, dict_stats))


def wordle_guess(not_letters, has_letters, position_letters, not_position_letters):
    input_file_path = 'cleaned_wordle_words.txt'
    dictionary = open(input_file_path, 'r')
    guesses = read_in_dict(dictionary)
    guesses = words_without_letters(not_letters, guesses)
    guesses = words_with_letters(has_letters, guesses)
    guesses = words_with_letter_positions(position_letters, guesses)
    guesses = words_letter_not_position(not_position_letters, guesses)

    dict_stats = get_dict_stats(guesses)
    entropy_sort_list(guesses, dict_stats)
    dictionary.close()

    return guesses

if __name__ == "__main__":
    not_letters = ""
    has_letters = ""
    position_letters = "_____"
    not_position_letters = {
    }

    print(wordle_guess(not_letters, has_letters, position_letters, not_position_letters)[:10])