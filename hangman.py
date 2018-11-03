
import pygame, sys
from pygame.locals import *

pygame.init()

white = (255,255,255)

def replace(array, index, newVal):
    array[index] = newVal

def check(string, guess, guesses):
    spot = 0
    for x in string:
        if x == guess:
            replace(guesses, spot, x)
        spot += 1

def isDone(guesses):
	flag = True
	for element in guesses:
		if element == "-":
			flag = False
	return flag

word = "secret"
guesses = []
incorrectLetters = 0
guessedLetters = []
        
name = input("What is your name? ")

print ("Hello, " + name + ". Time to play hangman!")

for char in word:
    guesses.append("-")

while incorrectLetters < 6:
    guess = input("Guess a letter. ")

    while guess in guessedLetters:
        guess = input("You've already guessed that. Try again! ")
		
    if guess in word:
        print("Good job! That's in the word!")
        check(word, guess, guesses)
    else:
        print("Uh-oh! That letter is not in the word")
        incorrectLetters = incorrectLetters + 1

    guessedLetters.append(guess)
    print("".join(guesses))
    if isDone(guesses) == True:
        print("Amazing! You found the word!")
        break
	    

if incorrectLetters == 6:
    print("Oh no! You did not find the word! It was actually " + word)

	
while True:

    screen = pygame.display.set_mode((500,500))
    pygame.display.set_caption("Hangman")

    screen.fill(white)
    pygame.draw.line(screen, (0,0,0), (250, 250), (250, 100))


    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
