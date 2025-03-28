#Prog04. isupper() check if all characters of the string is on upper case. Create a program that do the same functionality without using isupper() function.

def custom_isupper(s):
    # Empty string is uppercase
    if not s:
        return True

    # Check each character
    for char in s:
        # If character is a letter and not uppercase, return False
        if 'A' <= char <= 'Z':
            continue
        # If character is a letter but not uppercase, return False
        elif 'a' <= char <= 'z':
            return False
        # If character is not a letter, return False
        else:
            return False

    # If we get here, all characters were uppercase
    return True


# Get user input
text = input("Enter a string: ")

# Show result
print(f"\nResult: {custom_isupper(text)}")