
#this method checks for empty input and stops when two times the input is empty
def empty_input():
	user_input = input("Enter something: ")
	counter = 0

	if len(user_input) == 0:
		counter += 1
		user_input = input("Enter something: ")
	else:
		while counter < 2:
			user_input = input("Enter something: ")
			if len(user_input) == 0:
				counter += 1

# empty_input()



#this method checks for empty input and stops when two times in a row the input is empty
def empty_input_consec():
	counter = 0
	while counter != 2:
		user_input = input("Enter something: ")
		if len(user_input) == 0:
			counter += 1
		else:
			counter = 0

empty_input_consec()

