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
	most_count = 0

	for i in number_list:
		count = number_list.count(i)

		if count >= most_count:
			most_count = count