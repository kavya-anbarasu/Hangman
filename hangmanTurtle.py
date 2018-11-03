from turtle import *
from random import randint
bob = Turtle()

def setup():
	bob.speed(10)
	bob.forward(100)
	bob.left(180)
	bob.forward(50)
	bob.right(90)
	bob.forward(200)
	bob.right(120)
	bob.forward(50)
	       
def drawHangman(incorrectLetters):
	if incorrectLetters == 1:
		bob.penup()
		bob.setheading(0)
		bob.right(90)
		bob.forward(40)
		bob.pendown()
		bob.left(90)
		bob.circle(20)
        
	elif incorrectLetters == 2:
		bob.setheading(-90)
		bob.forward(80)
		bob.right(180)
		bob.forward(40)
        	
	elif incorrectLetters == 3:
		bob.right(45)
		bob.forward(50)
		bob.left(180)
		bob.forward(50)
        	
	elif incorrectLetters == 4:
		bob.right(90)
		bob.forward(50)
		bob.left(180)
		bob.forward(50)
		bob.setheading(-90)
		bob.forward(40)
        	
	elif incorrectLetters == 5:	
		bob.left(30)
		bob.forward(50)
		bob.right(180)
		bob.forward(50)

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

def gameplay():
	players = int(input("How many people are playing?(Input a number) "))
	if players > 1:
		word = input("Player 1, please input a word to play (all lowercase). ")
		for x in range (0, 17):
			print ("\n")
	else:
		name = input("What is your name? ")
		print ("Hello, " + name + ". Time to play hangman!")
		wordList = ["rhythm","jazziness","mathematics","application","capitalism","intern",
		"scoundrel","clockwork","mascot","cuticle","spool","inconceivable","poplulation",
		"flannel","hatch","hedge","sentence","average","computer","keyboard","presentation"]
		number = randint(0 , len(wordList) - 1)
		word = wordList[number]
	guesses = []
	incorrectLetters = 0
	guessedLetters = []
	
	for char in word:
		guesses.append("-")
	
	print ("".join(guesses))

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
			drawHangman(incorrectLetters)
        	
		guessedLetters.append(guess)
		print("".join(guesses))
		if isDone(guesses):
			print("Amazing! You found the word! Click on the hangman to exit! ")
			break
	    
	if incorrectLetters == 6:
		bob.left(120)
		bob.forward(50)
		bob.right(180)
		bob.forward(50)
		print("Oh no! You did not find the word! It was actually " + word + ". Click the hangman to exit.")

def main():
	setup()
	gameplay()
	exitonclick()
	
main()

