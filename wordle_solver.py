from math import log

input_file_path = 'cleaned_words.txt'

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

def get_dict_stats(dictionary):
    letter_occurrences = {'a' : 0,
    'b' : 0,'c' : 0,'d' : 0,'e' : 0,'f' : 0,
    'g' : 0,'h' : 0,'i' : 0,'j' : 0,'k' : 0,
    'l' : 0,'m' : 0,'n' : 0,'o' : 0,'p' : 0,
    'q' : 0,'r' : 0,'s' : 0,'t' : 0,'u' : 0,
    'v' : 0,'w' : 0,'x' : 0,'y' : 0,'z' : 0}
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

'''
words = read_in_dict(dictionary)
dict_stats = get_dict_stats(words)
entropy_sort_list(words, dict_stats)


found_irate = False
i = 0
while not found_irate:
    print(words[i], get_entropy(words[i], dict_stats))
    if words[i] == "irate":
        found_irate = True
    i+=1


dictionary.close()'''