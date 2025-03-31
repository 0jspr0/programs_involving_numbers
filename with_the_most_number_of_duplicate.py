numbers = 0

number_list = []

with_the_most_number_of_duplicate_list = []

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

			if i not in with_the_most_number_of_duplicate_list:
				with_the_most_number_of_duplicate_list.append(i)

for i in with_the_most_number_of_duplicate_list:
	print(i)