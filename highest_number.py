numbers = 0

while True:
	numbers += 1
	try:
		number = int(input(f"Enter number {numbers}: "))
	except ValueError:
		break