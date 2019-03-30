def factors(num):
	factors = []
	for item in range(1,num):
		if (num%item == 0):
			factors.append(item)

	factors.append(num)
	return (factors)

print(factors(245))


