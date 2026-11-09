# Module 6, Problem 3

# Define main() function 
def main():

	# Prompt user to enter principle amount 
	amount = float(input("Enter principle amount of CD: $"))

	# Prompt user to enter year to maturity 
	year = int(input("Enter year to maturity of CD: "))

	# Declare interest rate variable
	interest_rate = 0

	# Determine interest rate 
	if (amount > 100000 and year == 5):
		interest_rate = 0.06
	elif ((amount >= 50000 and amount <= 100000) and year == 10):
		interest_rate = 0.05
	elif ((amount >= 50000 and amount <= 100000) and year == 5):
		interest_rate = 0.04
	else:
		interest_rate = 0.02

	# Calculate first year interest 
	first_year = amount * interest_rate

	# Display output back to user 
	print("Principle amount: $" + format(amount, ",.2f"))
	print("Interest rate: " + format(interest_rate * 100, ".0f") + "%")
	print("Interest in first year: " + format(first_year, ",.2f"))

# Call main() function
if __name__ == "__main__":
	main()