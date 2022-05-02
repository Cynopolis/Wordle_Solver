input_file_path = 'source_words.txt'
output_file_path = 'cleaned_words.txt'

input_file = open(input_file_path, 'r')
output_file = open(output_file_path, 'w')

def is_five_characters(word):
    return len(word) == 5

def is_only_letters(word):
    return word.isalpha()


for line in input_file:
    word = line.strip()
    if is_five_characters(word) and is_only_letters(word):
        output_file.write(word.lower() + '\n')

input_file.close()
output_file.close()