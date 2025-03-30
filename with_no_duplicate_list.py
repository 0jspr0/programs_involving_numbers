unique_list = []
duplicate_list = []

for i in range(10):
	number = int(input(f"Enter number {i + 1}: "))
	
	if number not in unique_list:
		unique_list.append(number)
	else:
		duplicate_list.append(number)