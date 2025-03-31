numbers = 0

unique_list = []
duplicate_list = []

while True:
	numbers += 1
	try:
		number = int(input(f"Enter number {numbers}: "))
		if number not in unique_list:
			unique_list.append(number)
			print("Unique")
		else:
			duplicate_list.append(number)
			print("Duplicate")
	except ValueError:
		break