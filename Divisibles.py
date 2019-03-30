
def divisible():
	the_list = (list(range(9000, 9101)))
	for number in the_list:
		if (number%7 == 0) and (number%5 != 0):
			print(number)

divisible()