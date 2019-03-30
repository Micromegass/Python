
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

empty_input()



