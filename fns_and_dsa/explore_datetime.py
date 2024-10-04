# explore_datetime.py

from datetime import datetime, timedelta


def display_current_datetime():
	"""
	Function to display the current date and time in a readable format (YYYY-MM-DD HH:MM:SS).
	"""
	current_date = datetime.now()  # Get the current date and time
	formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")  # Format the current date and time
	print(f"Current date and time: {formatted_date}")


def calculate_future_date(days):
	"""
	Function to calculate and display a future date after adding a number of days.

	Parameters:
	days (int): The number of days to add to the current date.
	"""
	current_date = datetime.now()  # Get the current date
	future_date = current_date + timedelta(days=days)  # Calculate the future date by adding the days
	formatted_future_date = future_date.strftime("%Y-%m-%d")  # Format the future date
	print(f"Future date: {formatted_future_date}")


def main():
	# Part 1: Display the current date and time
	display_current_datetime()
	
	# Part 2: Calculate a future date
	try:
		days = int(
			input("Enter the number of days to add to the current date: "))  # Get the number of days from the user
		calculate_future_date(days)  # Calculate and display the future date
	except ValueError:
		print("Invalid input! Please enter an integer.")


if __name__ == "__main__":
	main()
