number_of_odd_numbers = 0

for i in range(10):
	number = int(input(f"Enter number {i + 1}: "))
	if number % 2 == 1:
		number_of_odd_numbers += 1

print(f"Number of odd numbers: {number_of_odd_numbers}")