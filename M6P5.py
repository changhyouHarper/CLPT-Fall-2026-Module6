# Module 6, Problem 5

# Define main() function 
def main():

	# Prompt user to enter employee last name
	last_name = input("Enter last name: ")

	# Prompt user to enter salary 
	salary = float(input("Enter salary: $"))

	# Prompt user to enter job level 
	job_level = int(input("Enter job level: "))

	# Create variable to store bonus rate 
	bonus_rate = 0

	# Determine bonus rate 
	if (job_level >= 10):
		bonus_rate = 0.25
	elif (job_level >= 5 and job_level <= 9):
		bonus_rate = 0.20
	else:
		bonus_rate = .10

	# Calculate bonus 
	bonus_amount = salary * bonus_rate

	# Display output back to user 
	print("Employee Last Name: " + last_name)
	print("Bonus: $" + format(bonus_amount, ".2f"))


# Call main() function
if __name__ == "__main__":
	main()