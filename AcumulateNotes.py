#Acumulate notes
#Ask user to add a note to the file
#using a while loop and writing to archives

def write_to_archive(an_archive):

	input_user = input("Please add a note to your notebook (quit with q): ")

	while (input_user != "q"):
		archive = open(an_archive, "a+", encoding="ISO-8859-1")
		archive.write("- "+input_user+"\n")
		archive.close()
		input_user = input("Please write what you would like to add to the file (quit with q): ")


def overwrite_archive(an_archive):

	input_user = input("Overwriting notebook (quit with q): ")

	if (input_user != "q"):
		archive = open(an_archive, "w", encoding="ISO-8859-1")
		archive.write("- "+input_user+"\n")
		archive.close()

		input_user = input("Appending to notebook (exit with 'q'): ")

		while (input_user != "q"):
			archive = open(an_archive, "a+", encoding="ISO-8859-1")
			archive.write("- " + input_user + "\n")
			archive.close()
			input_user = input("Appending to notebook (exit with 'q'): ")

	else:
		print("exiting")


def show_content_archive(an_archive):
	try:
		archive = open(an_archive, "r")
		content = archive.read().splitlines()
		print()
		for items in content:
				print(items)
		archive.close()

	except FileNotFoundError:
		print()
		print("File does not yet exist. Please write a notebook first, with 'w'")
		choose("notebook.txt")


def choose(an_archive):
	archive = an_archive
	print()
	user_input = input("Do you want to see the notebook('s'), write to your notebook('w') or overwrite your notebook?('o'). Use 'q' to quit: ")

	if (user_input == "w"):
		write_to_archive(archive)
		choose("notebook.txt")

	elif (user_input == "o"):
		overwrite_archive(archive)
		choose("notebook.txt")

	elif (user_input == "s"):
		show_content_archive(archive)
		choose("notebook.txt")

	elif (user_input == "q"):
		print("exiting")

	else:
		print()
		print("unexpected input. Try again")
		choose("notebook.txt")


choose("notebook.txt")










