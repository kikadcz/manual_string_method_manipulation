#Prog06. ljust() add space characters at the end of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using ljust() function.

def custom_ljust(s, width):
    # If width is less than or equal to string length, return original string
    if width <= len(s):
        return s

    # Calculate number of spaces needed
    spaces_needed = width - len(s)

    # Add spaces to the end
    return s + ' ' * spaces_needed


# Get user input
text = input("Enter a string: ")
width = int(input("Enter the desired width: "))

# Show result
print(f"\nResult: '{custom_ljust(text, width)}'")