#writes a list of list to a textfile

def list_of_lists(a_list, an_archive):
	#create list of lists
	the_list = []
	the_list.append(a_list)

	#write the list of list to archive
	archive = open(an_archive, "w", encoding="ISO-8859-1")
	list_of_a_list2 = str(the_list)
	archive.write("- " + list_of_a_list2 + "\n")

	#write single entries of list to archive
	for item in the_list:
		for i in item:
			i = str(i)
			archive.write("- " + i + "\n")

	archive.close()


list_of_lists([1,2,3,4,5,6,7,7,8,56,75,7.667,232, 5356.57, 3435353636.474, 18], "list.txt")
