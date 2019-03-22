class Animal():
	noise = "grunt"
	size = "large"
	color = "brown"
	hair = "covers body"

	@property
	def get_color(self):
		return self.color

	def make_noise(self):
		return self.noise


class Dog(Animal):
	name = "Bobby"
	# age = 12
	# speed = 0
	# color = "white"

	def getColor(self):
		return self.color

	def getName(self):
		return self.name



dog = Animal()
print(dog.make_noise())

a_dog = Dog()
print(a_dog.get_color)
print(a_dog.name)

print(a_dog.getColor())

jack = Dog()
print(jack.make_noise())

sam = Dog()
sam.getName()



def some_func(arg1, arg2, arg3, kwarg1 = "A string", kwarg2=1):
	if arg1 > 23:
		print(arg2, arg3)
	else:
		print(kwarg1+"\n",kwarg2)


some_func(18, 22, 2)


class Bankaccount():
	def __init__(self, saldo, name):
		self.saldo = saldo
		self.name = name

	def getAccountName(self):
		return self.name

	def getSaldo(self):
		return self.saldo

	def EarnSaldo(self, money):
		self.saldo += money

	def SpendSaldo(self, money):
		self.saldo -= money


paul = Bankaccount(10000, "Paul's Account")

print(paul.getAccountName())
print(paul.getSaldo())

paul.EarnSaldo(10000)
print(paul.getSaldo())

paul.SpendSaldo(5000)
print(paul.getSaldo())





