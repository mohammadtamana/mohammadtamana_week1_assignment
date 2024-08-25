# Function to determine if a number is positive, negative, or zero
def check_number(num):
    if num > 0:
        return "The number is positive."
    elif num < 0:
        return "The number is negative."
    else:
        return "The number is zero."
# Main function to handle user input and display the result
def main():
    # Prompt the user to enter a number
    user_input = input("Enter a number: ")

    try:
        # Convert the input to a float
        number = float(user_input)
        
        # Determine and display the result
        print(check_number(number))
    
    except ValueError:
        # Handle invalid input
        print("Invalid input! Please enter a numeric value.")