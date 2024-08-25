# Function to reverse a string
def reverse_string(input_string):
    return input_string[::-1]

# Main function
def main():
    # Accept user input
    user_input = input("Enter a string: ")
    
    # Reverse the string using the reverse_string function
    reversed_string = reverse_string(user_input)
    
    # Display the reversed string
    print("Reversed string:", reversed_string)