number_of_even_numbers = 0

for i in range(10):
	number = int(input(f"Enter number {i + 1}: "))
	if number % 2 == 0:
		number_of_even_numbers += 1

print(f"Number of even numbers: {number_of_even_numbers}")