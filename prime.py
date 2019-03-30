#Finds out if number is primenumber
def prime(num):

	prime_list = []

	if num > 1:
		for item in range(2,num):
			if (num%item != 0):
				prime_list.append(item)

		if len(prime_list) == (num - 2):
			print("primenumber")
		else:
			print("not a primenumber")
	else:
		"Numbers smaller than 1 can't be primenumbers"


#Asks for user input
def action_prime():
	ui = input("enter a positive number bigger than 1: ")
	ui = int(ui)
	prime(ui)



action_prime()

