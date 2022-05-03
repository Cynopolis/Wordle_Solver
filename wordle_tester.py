import wordle_solver

def wordle_guess(not_letters, has_letters, position_letters):
    input_file_path = 'cleaned_words.txt'
    dictionary = open(input_file_path, 'r')
    guesses = wordle_solver.read_in_dict(dictionary)
    guesses = wordle_solver.words_without_letters(not_letters, guesses)
    guesses = wordle_solver.words_with_letters(has_letters, guesses)
    guesses = wordle_solver.words_with_letter_positions(position_letters, guesses)

    dict_stats = wordle_solver.get_dict_stats(guesses)
    wordle_solver.entropy_sort_list(guesses, dict_stats)
    dictionary.close()

    return guesses

def check_guess(guess, word, not_letters, has_letters, position_letters):

    for i, letter in enumerate(guess):
        if letter in word:
            if letter not in has_letters:
                if letter == word[i]:
                    position_letters = position_letters[:i] + letter + position_letters[i+1:]
            has_letters += letter
        else:
            not_letters += letter
    
    return not_letters, has_letters, position_letters

word = "irate"
not_letters = ""
has_letters = ""
position_letters = "_____"

for i in range(10):
    guess = wordle_guess(not_letters, has_letters, position_letters)
    not_letters, has_letters, position_letters = check_guess(guess[0], word, not_letters, has_letters, position_letters)
    print(guess[0], not_letters, has_letters, position_letters)