numbers = 0

number_list = []

while True:
	numbers += 1
	try:
		number = int(input(f"Enter number {numbers}: "))
		number_list.append(number)
	except ValueError:
		break

if number_list:
	highest_number = max(number_list)
	print(f"Highest number: {highest_number}")