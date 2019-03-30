import random
def prime_range():
	#create random number between 2 an 10.000.000 and save to variable
	random_num = random.randint(2, 10000000)

	prime_list = []
	# find all prime numbers in that list
	for item in range(2, random_num):
		is_prime = True
		for num in range(2, item):
			if (item % num == 0):
				is_prime = False

		if is_prime:
			prime_list.append(item)

	return (prime_list)


print(prime_range())


