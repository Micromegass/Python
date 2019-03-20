import datetime
##Capitalize first letter
text = "this is a string"
first_item = text[0].upper()
rest = text[1:]
result = first_item + rest + '.'
print(result)

##Capitalize to title
another_text = "this is another string"
result = another_text.title()
print(result)

##string substitution

text = "This is {variable_a} formatted string".format(variable_a="variable based")
print(text)

name = "Axel"
text2 = "This is {variable_b} formatted string".format(variable_b=name)
print(text2)

cooltext = "This is a {} cool thing".format("cool")
print(cooltext)

percentSub = "Wassup holmes. I am %s" %("Axel")

print(percentSub)



text = "0 decimal places: %.0f" %(20)
print(text)


text = "2 decimal places: %.2f" %(20)
print(text)

text = "10 decimal places: %.10f" %(20)
print(text)

text = "400 decimal places: %.400f" %(20)
print(text)


text = "%.2f" %(20.23131)
print(text)



import datetime
today = datetime.date.today()
text = '{today.month}/{today.day}/{today.year}'.format(today=today)
print(text)

text = today.strftime('%-m/%-d/%y')
print(text)

now = datetime.datetime.utcnow() #utc time
text = now.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
print(text)

now = datetime.datetime.now() #local time
date_text = now.strftime('%Y/%m/%d %H:%M:%S.%f') #[:-3]
text = "Time is: %s" %(date_text)
print(text)

now = datetime.datetime.now()
date_text = now.strftime('%B %d, %Y %H:%M:%S.%f %p')
text = "Time is %s" %(date_text)
print(text)

now = datetime.datetime.now()
date_text = now.strftime('%x')
text = "Time is %s" %(date_text)
print(text)



default_names = ["Justin", "john", "Emilee", "Jim", "Ron", "Sandra", "veronica", "Whitney"]
default_amounts = [123.32, 94.23, 124.32, 323.4, 23, 322.122323, 32.4, 99.99]

unf_message = """Hi {name}! 
Thank you for the purchase on {date}. 
We hope you are excited about using it. Just as a
reminder the purchase total was ${total}.
Have a great one!
"""


def make_messages(names, amounts):
	messages = []

	if len(names) == len(amounts):
		i = 0
	today = datetime.date.today()
	text = '{today.month}/{today.day}/{today.year}'.format(today=today)

	for name in default_names:
		new_amount = "%.2f" %(amounts[i])
		new_msg = unf_message.format(name=name,date=text,total=new_amount)
		i += 1
		print(new_msg)


make_messages(default_names, default_amounts)
