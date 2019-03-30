#Version 1: Iterative
def factorial(number):
	if (number > 100) or (number < 0):
		return 0
	elif (number == 0) or (number == 1):
		return 1
	else:
		i = 1
		result = 1
		while (i < number):
			result = result * (i+1)
			i += 1

		return(result)


print(factorial(5))


#Version2: recursive
def factorialRec(number):
	if (number > 100) or (number < 0):
		return 0
	elif (number == 0) or (number == 1):
		return 1
	else:
		result = number * factorialRec(number - 1)

	return(result)


print(factorialRec(5))