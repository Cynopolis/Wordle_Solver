input_file_path = 'cleaned_words.txt'

dictionary = open(input_file_path, 'r')

char_not_in_word = ''
char_in_word = ''

# go through the dictionary and find the words that have the given characters
def words_with_letters(letters, dictionary):
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

def get_entropy(dict_size, valid_words)

valid_words = words_without_letters("ira", dictionary)
print(valid_words)