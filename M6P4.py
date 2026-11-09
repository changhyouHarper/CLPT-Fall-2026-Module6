# Module 6, Problem 4

# Define main() function 
def main():

	# Prompt user to enter number of concert tickets 
	num_tickets = int(input("Enter number of concert tickets: "))

	# Declare variable for price of ticket 
	price = 0

	# Determine price per ticket 
	if (num_tickets >= 25):
		price = 50
	elif (num_tickets >= 10 and num_tickets <= 24):
		price = 60
	elif (num_tickets >= 5 and num_tickets <= 9):
		price = 70
	elif (num_tickets < 5):
		price = 75

	# Calculate the total
	total = num_tickets * price

	# Display output back to user 
	print("Number of tickets: " + str(num_tickets))
	print("Price per ticket: " + format(price, ".2f"))
	print("Total cost: $" + format(total, ",.2f"))


# Call main() function
if __name__ == "__main__":
	main()