import wordle_solver
import multiprocessing as mul

def wordle_guess(not_letters, has_letters, position_letters, not_position_letters):
    input_file_path = 'cleaned_words.txt'
    dictionary = open(input_file_path, 'r')
    guesses = wordle_solver.read_in_dict(dictionary)
    guesses = wordle_solver.words_without_letters(not_letters, guesses)
    guesses = wordle_solver.words_with_letters(has_letters, guesses)
    guesses = wordle_solver.words_with_letter_positions(position_letters, guesses)
    guesses = wordle_solver.words_letter_not_position(not_position_letters, guesses)

    dict_stats = wordle_solver.get_dict_stats(guesses)
    wordle_solver.entropy_sort_list(guesses, dict_stats)
    dictionary.close()

    return guesses

def check_guess(guess, word, not_letters, has_letters, position_letters, not_position_letters):

    for i, letter in enumerate(guess):
        if letter in word and letter not in has_letters:
            has_letters += letter
        elif letter not in not_letters and letter not in has_letters:
            not_letters += letter

        if letter == word[i]:
            position_letters = position_letters[:i] + letter + position_letters[i+1:]
        
        if letter in word and word[i] != letter:
            if letter not in not_position_letters:
                new_letter_list = [False] * 5
                new_letter_list[i] = True
                not_position_letters[letter] = new_letter_list
            else:
                not_position_letters[letter][i] = True
            
    
    return not_letters, has_letters, position_letters, not_position_letters

def get_word_stats(word):
    words =[word]
    total_num_guesses = 0
    not_letters = ""
    has_letters = ""
    position_letters = "_____"
    not_position_letters = {}
    guesses = []
    total_words = 0
    percentage = 0
    last_percentage = 0

    for total_words, word in enumerate(words):
        for x in range(20):
            total_num_guesses += 1
            guess = wordle_guess(not_letters, has_letters, position_letters, not_position_letters)
            if len(guess) == 0:
                print("No more guesses")
                exit()
            new_guess = guess[0]
            i = 0
            while new_guess in guesses:
                new_guess = guess[i]
                i += 1

            not_letters, has_letters, position_letters, not_position_letters = \
            check_guess(new_guess, word, not_letters, has_letters, position_letters, not_position_letters)

            guesses.append(new_guess)
            if position_letters == word:
                percentage = round(total_words*100/len(words), 0)
                if percentage - last_percentage >= 5:
                    print(str(percentage) + r"% finished with", word[0])
                    last_percentage = percentage
                not_letters = ""
                has_letters = ""
                position_letters = "_____"
                guesses = []
                not_position_letters = {}
                break
    return total_num_guesses

from time import time
if __name__ == "__main__":
    alphabet = list("ab")
    input_file_path = 'cleaned_words.txt'
    dictionary = open(input_file_path, 'r')
    words = wordle_solver.read_in_dict(dictionary)
    dictionary.close()
    timer = time()

    testers = mul.Pool()
    total_guesses = 0
    results = []

    for i, word in enumerate(words):
        results.append(testers.apply_async(get_word_stats, (word,)))
        if i % 100 == 0:
            print(i, "words tested")
    print("Recovering Results")
    for i, result in enumerate(results):
        try:
            total_guesses += result.get(timeout=1)
            if i % 100 == 0:
                print(i, "results recovered. Current average:", total_guesses/(i+1))
        except mul.TimeoutError:
            print("Timed out")

    print("Time taken:", time() - timer)
    print("The average number of guesses per {} word is " + str(total_guesses/10))