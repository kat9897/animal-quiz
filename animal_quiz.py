# Libraries
import keyboard
import random

# Variables
ATTEMPT_LIMIT = 3
POINTS_PER_ANSWER = 1
HELP_KEY = "h"
QUIT_KEY = "z"
QUESTION_KEY = "q"

score = 0
playing = True

# Title
print("Guess the Animal!\n")

# Questions and Answers
guesses = {
    "Which bear lives at the North Pole?": "polar bear",
    "What is the fastest land animal?": "cheetah",
    "What is the largest animal?": "blue whale"
}

# Check if game is in play
def game_in_play():
    global playing
    if keyboard.is_pressed("q"):
        playing = False
    return playing

# Check the Guess
def check_guess(guess, answer, question):
    global score, playing
    attempt = 0
    while attempt < ATTEMPT_LIMIT and game_in_play():
        if guess == answer:
            print("Correct answer!\n")
            score += POINTS_PER_ANSWER
            return
        else:
            # Help
            if guess == HELP_KEY:
                print("These are the list of commands we currently have:\n")
                print(HELP_KEY + " = help\n" + QUESTION_KEY + " = repeat question\n" + QUIT_KEY + " = quit")
            # Repeat Question
            elif guess == QUESTION_KEY:
                print(question)
            # Quit
            elif guess == QUIT_KEY:
                playing = False
                break
            # Wrong Guess
            elif attempt < ATTEMPT_LIMIT - 1:
                print("Sorry wrong answer. Try again.")
                attempt += 1
            # Next attempt
            guess = input()
    if attempt >= ATTEMPT_LIMIT:
        print("The correct answer is " + answer + "\n")

# Game loop
while game_in_play():
    # Randomly pick a question
    question = random.choice(list(guesses))
    answer = guesses[question]
    guess = input(question + "\n")
    # Check answer
    check_guess(guess.lower(), answer.lower(), question)

# Finished the game
print("Congratulations on finishing!")
print("You finished with a score of " + str(score) + " points.")
