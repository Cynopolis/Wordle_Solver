import wordle_solver
import wordle_tester
from random import randint

input_file_path = 'cleaned_wordle_words.txt'
dictionary = open(input_file_path, 'r')
words = wordle_solver.read_in_dict(dictionary)
dictionary.close()

word = words[randint(0, len(words) - 1)]

not_letters = ""
has_letters = ""
position_letters = "_____"
not_position_letters = {}

for i in range(7):
    print(wordle_solver.wordle_guess(not_letters, has_letters, position_letters, not_position_letters)[:10])
    user_input = ""
    while len(user_input) != 5 and not user_input.isalpha():
        user_input = input("Guess a word ({}/6): ".format(i+1))
    if user_input == word:
        print("You win! The word is {}!".format(word))
        exit()
    not_letters, has_letters, position_letters, not_position_letters = wordle_tester.check_guess(user_input, word, not_letters, has_letters, position_letters, not_position_letters)
    print("Current state: " + position_letters)

