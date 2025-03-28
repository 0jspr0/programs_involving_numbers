number1 = int(input("Enter number 1: "))
number2 = int(input("Enter number 2: "))

if number1 < number2:
	for i in range(number1, number2+1):
		print(i)
elif number2 < number1:
	for i in range(number2, number1+1):
		print(i)