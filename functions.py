items = [1, 2, 3, 1234, 454.2, "Axel", "Sers", "Bob"]


def parse_lists(some_list):
	str_list_items = []
	num_list_items = []

	for things in some_list:
		if isinstance(things, float) or isinstance(things, int):
			num_list_items.append(things)
		elif isinstance(things, str):
			str_list_items.append(things)
		else:
			pass

	return str_list_items, num_list_items


print(parse_lists(items))


def mySum(my_num_list):
	total = 0
	for i in my_num_list:
		if isinstance(i, float) or isinstance(i, int):
			total += i

	return total


def myCount(my_num_list):
	total = 0
	for i in my_num_list:
		if isinstance(i, float) or isinstance(i, int):
			total += 1

	return total


def myAverage(my_num_list):
	sum = mySum(my_num_list)
	nbr = myCount(my_num_list)
	average = sum/nbr

	return average


items3 = [1,2,3,4]

print(sum(items3))
print(mySum(items3))
print(myAverage(items3))
