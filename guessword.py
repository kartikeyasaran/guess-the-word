#usr!/bin/python
import random
name = input('name here: ')
print("Good Luck ! "+name)
words = ['rainbow', 'computer', 'science', 'programming',
		'python', 'mathematics', 'player', 'condition',
		'reverse', 'water', 'board', 'morning','hello','evening','night','day','smooth','torch','good','bad','beautiful','ugly','messy','clean','house','home','garden','building','java','nice','adjust','congrates','then']
word = random.choice(words)
print("Guess the characters")
guesses = ''
turns = 14
while turns > 0:
	failed = 0
	for char in word:
		if char in guesses:
			print(char, end=" ")
		else:
			print("_")
			failed += 1
	if failed == 0:
		print("You Won the game.")
		print("The word is: ", word)
		break
	print()
	guess = input("guess a character:")
	guesses += guess
	if guess not in word:
		turns -= 1
		print("Wrong")
		print("You have", + turns, 'more guesses')
		if turns == 0:
			print("You Lost the game.")
