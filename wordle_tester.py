import wordle_solver

word = "irate"
not_letters = ""
has_letters = ""
position_letters = "_____"

def wordle_guess(not_letters, has_letters, position_letters):
    input_file_path = 'cleaned_words.txt'
    dictionary = open(input_file_path, 'r')

    guesses = wordle_solver.words_without_letters(not_letters, dictionary)
    guesses = wordle_solver.words_with_letters(has_letters, guesses)
    guesses = wordle_solver.words_with_letter_positions(position_letters, guesses)

    dict_stats = wordle_solver.get_dict_stats(guesses)
    wordle_solver.entropy_sort_list(guesses, dict_stats)
    dictionary.close()

    return guesses

