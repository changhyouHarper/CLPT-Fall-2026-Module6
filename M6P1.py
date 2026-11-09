# Module 6, Problem 1

# Define main() function
def main():
	# Prompt the user to enter the quantity of widgets 
	quantity_widgets = int(input("Enter the quantity of widgets: "))

	# Declare price variable 
	price = 0

	# Declare tax variable
	tax = 0.07

	# Determine price to charge 
	if (quantity_widgets > 10000):
		price = 10
	elif (quantity_widgets >= 5000 and quantity_widgets <= 10000):
		price = 20
	elif (quantity_widgets < 5000):
		price = 30

	# Calculate extended price 
	extended_price = quantity_widgets * price 

	# Calculate tax 
	tax_amount = extended_price * tax

	# Calculuate total
	total = extended_price + tax_amount

	# Display output back to user 
	print("Extended Price: $" + format(extended_price, ",.2f"))
	print("Tax Amount: $" + format(tax_amount, ",.2f"))
	print("Total: $" + format(total, ",.2f"))

# Call main() function
if __name__ == "__main__":
	main()