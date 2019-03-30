def empty_input_consec(an_archive):
	counter = 0
	while counter != 2:
		user_input = input("Enter something: ")
		if len(user_input) == 0:
			counter += 1
		else:
			archive = open(an_archive, "a+", encoding="ISO-8859-1")
			archive.write("- " + user_input + "\n")
			archive.close()
			counter = 0

empty_input_consec("notebook2.txt")