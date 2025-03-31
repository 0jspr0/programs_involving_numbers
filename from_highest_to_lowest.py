numbers = 0

number_list = []

while True:
	numbers += 1
	try:
		number = int(input(f"Enter number {numbers}: "))
		number_list.append(number)
	except ValueError:
		break

number_list.sort()
number_list.reverse()

for i in number_list:
	print(i)