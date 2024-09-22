def main():
  """Prompts user for task details and provides a customized reminder."""

  # Get user input for the task
  task = input("Enter your task: ")

  # Get user input for priority
  while True:
    priority = input("Priority (high/medium/low): ").lower()
    if priority in ("high", "medium", "low"):
      break
    else:
      print("Invalid priority. Please enter high, medium, or low.")

  # Get user input for time sensitivity
  while True:
    time_bound = input("Is it time-bound? (yes/no): ").lower()
    if time_bound in ("yes", "no"):
      break
    else:
      print("Invalid input. Please enter yes or no.")

  # Process task based on priority and time sensitivity
  reminder = f"'{task}' is a {priority} priority task. "

  match priority:
    case "high":
      reminder += "Don't forget to complete it!"
      if time_bound == "yes":
        reminder += " It requires immediate attention today!"
    case "medium":
      reminder += "Consider completing it when you have a chance."
    case "low":
      reminder += "This can wait, but don't forget about it."

  # Additional message for non-time-bound high priority tasks
  if not time_bound and priority == "high":
    print(reminder)
    print("\nWell done on completing this project! Let the world hear about this milestone achieved.")
    print(" Click here to tweet! ")
  else:
    print(reminder)

if __name__ == "__main__":
  main()