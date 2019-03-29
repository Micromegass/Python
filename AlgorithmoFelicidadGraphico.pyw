#Second implementation with graphics

import tkinter as tk
import tkinter.messagebox as msg
import random


def happiness():
	advices = ["Eat cake", "Change your life", "Meet a friend", "Listen to music", "Drink Guaro", "Watch a movie",
	            "Have sex", "Find a hobby", "Read a book", "Go to the movies", "Eat chocolate"]

	window = tk.Tk()
	window.withdraw()

	message = "Are you happy?"
	title = "Algorithm of happiness"
	answer = msg.askyesno(title, message)

	if (answer == True):
		message = "Great! Continue with what you are doing!"
		title = "Happy! ≠}"
		msg.showinfo(title, message)
	else:
		message = "Would you like to be happy?"
		title = "Unhappy! ≠{"
		answer = msg.askyesno(title, message)

		if (answer == True):
			message = random.choice(advices)
			title = "Advice"
			msg.showinfo(title, message)
		else:
			message = "Great! Continue with what you are doing!"
			title = "Stupid! ≠}"
			msg.showinfo(title, message)


happiness()
