# Module 6, Problem 2

# Define main() function
def main():

	# Prompt user to enter part number
	part_number = int(input("Enter part number: "))

	# Prompt user to entery quantity 
	quantity = int(input("Enter quantity: "))

	# Declare unit cost variable
	unit_cost = 0

	# Determine cost per unit 
	if (part_number == 10 or part_number == 55):
		unit_cost = 1.00
	elif (part_number == 99):
		unit_cost = 2.00
	elif (part_number == 70 or part_number == 80):
		unit_cost = 3.00
	else:
		unit_cost = 5.00

	# Calculate total cost 
	total_cost = quantity * unit_cost

	# Display output back to user
	print("Part Number: " + str(part_number))
	print("Cost Per Unit: $" + format(unit_cost, ".2f"))
	print("Total Cost: $" + format(total_cost, ".2f"))

# Call main() function
if __name__ == "__main__":
	main()
