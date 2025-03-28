number1 = int(input("Enter number 1: "))

sum = 0

for i in range(9):
	number = int(input(f"Enter number {i + 2}: "))
	sum = sum + number
	
difference = number1 - sum

print(difference)