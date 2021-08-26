

while True:
	try:
		x = int(input("Please enter a number: "))
		
	except ValueError:
		print("Opps, invalid number. please try again.")
	else:
		if x < 0:
			print("Negative")
		elif x == 0:
			print("zero")
		elif x == 1:
			print("one.")
		else:
			print("Greater than one.")
			break

			