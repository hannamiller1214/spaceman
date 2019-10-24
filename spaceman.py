import random

print("Welcome to Spaceman, the nicer version of Hangman!")

guessed_letters = []

def hide_secret_word(word_to_hide):
    hidden_word = ["-" * len(word_to_hide)]
    return hidden_word

def player_input(hidden_list, remaining_lives):
    print("This is your secret word! >", hidden_list)
    print("And here are your remaining lives >", remaining_lives)
    guessing = True
    while guessing:
        player_guess = input("Guess a letter! > ")
        if player_guess in guessed_letters:
            print("Looks like you've already guessed this letter! Try choosing another one!")
        elif player_guess == int():
            print("Looks like you've guessed a number! Try guessing a letter!")
        elif len(player_guess) != 1:
            print("Looks like you've guessed more than one letter! Try only guessing one!")
        else:
            guessed_letters.append(player_guess)
            guessing = False
        return player_guess

def start_game():
    words = open("words.txt", "r")
    select_secret = words.read().split(" ")
    secret_word = random.choice(select_secret)

    secret_list = list(secret_word)
    hidden_list = hide_secret_word(secret_list)
    remaining_lives = ["<3", "<3", "<3", "<3", "<3", "<3", "<3"]

    guessed_seven = False
    guessed_word = False
    while guessed_seven == False and guessed_word == False:
        player_guess = player_input(hidden_list, remaining_lives)
        result = is_guess_correct(player_guess, secret_list, hidden_list)
        if result is None:
            remaining_lives.pop(0)
        else:
            pass
        if remaining_lives == []:
            guessed_seven = True
        else:
            pass
        if hidden_list == secret_list:
            guessed_word = True
        else:
            pass

    if guessed_seven == True:
        guessed_letters.clear()
        print("Sorry! You lose! The secret word was \"{}\".".format(secret_word))
    elif guessed_word == True:
        guessed_letters.clear()
        print(hidden_list)
        print("Congratulations! You win!")

    play_again()


def is_guess_correct(guessed_letter, secret_list, hidden_list):
    did_replace_letter = False
    for (i, letter) in enumerate(secret_list):
        if guessed_letter == letter:
            #Something about this line is not wroking properly
            hidden_list[i] = guessed_letter
            did_replace_letter = True
        else:
            pass
    if did_replace_letter == True:
        return hidden_list
    else:
        return None

def play_again():
    play_or_not = True
    while play_or_not:
        play_quit = input("Enter 'P' to play again or 'Q' to quit the game > ")
        if play_quit.lower() == "p":
            print("Welcome to Spaceman, the nicer version of Hangman!")
            start_game()
            play_or_not = False
        elif play_quit.lower() == "q":
            print("Thank you for playing! Bye-bye!")
            play_or_not = False
        else:
            print("Please make a selection > ")

start_game()
