import wordle_solver
import multiprocessing as mul

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
        if letter in word and letter not in has_letters:
            has_letters += letter
        elif letter not in not_letters and letter not in has_letters:
            not_letters += letter

        if letter == word[i]:
            position_letters = position_letters[:i] + letter + position_letters[i+1:]
    
    return not_letters, has_letters, position_letters

def get_word_stats(letter):
    input_file_path = 'cleaned_words.txt'
    dictionary = open(input_file_path, 'r')
    words = wordle_solver.read_in_dict(dictionary)
    dictionary.close()
    words = wordle_solver.words_with_letter_positions("{}____".format(letter), words)

    not_letters = ""
    has_letters = ""
    position_letters = "_____"
    guesses = []
    total_num_guesses = 0
    total_words = 0
    percentage = 0
    last_percentage = 0

    for total_words, word in enumerate(words):
        for x in range(20):
            total_num_guesses += 1
            guess = wordle_guess(not_letters, has_letters, position_letters)
            new_guess = guess[0]
            i = 0
            while new_guess in guesses:
                new_guess = guess[i]
                i += 1

            not_letters, has_letters, position_letters = check_guess(new_guess, word, not_letters, has_letters, position_letters)
            guesses.append(new_guess)
            #print(new_guess, not_letters, has_letters, position_letters)
            if position_letters == word:
                percentage = round(total_words*100/len(words), 0)
                if percentage - last_percentage >= 5:
                    print(str(percentage) + r"% finished with", word[0])
                    last_percentage = percentage
                not_letters = ""
                has_letters = ""
                position_letters = "_____"
                guesses = []
                break
    
    print("The average number of guesses per {} word is ".format(word[0]) + str(total_num_guesses/total_words))

from time import time
if __name__ == "__main__":
    alphabet = list("abcdefghijklmnopqrstuvwxyz")

    input_file_path = 'cleaned_words.txt'
    dictionary = open(input_file_path, 'r')
    words = wordle_solver.read_in_dict(dictionary)
    dictionary.close()
    timer = time()

    testers = mul.Pool()
    testers.map(get_word_stats, alphabet)
    testers.close()
    print("Time taken:", time() - timer)
