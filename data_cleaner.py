input_file_path = 'wordle_words_source.txt'
output_file_path = 'cleaned_wordle_words.txt'

input_file = open(input_file_path, 'r')
output_file = open(output_file_path, 'w')

def is_five_characters(word):
    return len(word) == 5

def is_only_letters(word):
    return word.isalpha()


for line in input_file:
    words = line.split(",")
    print(len(words))
    for i, word in enumerate(words):
        word = ''.join(filter(str.isalpha, word))
        if is_five_characters(word):
            output_file.write(word + '\n')
    print(words)

input_file.close()
output_file.close()
