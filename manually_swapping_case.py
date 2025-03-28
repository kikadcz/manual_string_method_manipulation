#Prog08. swapcase() reverse the casing of each of the character of the string. Create a program that do the same functionality without using swapcase() function.

def custom_swap_case(text):
    result = []
    for char in text:
        if char.isupper():
            result.append(char.lower())
        elif char.islower():
            result.append(char.upper())
        else:
            result.append(char)
    return ''.join(result)

# Get user input
text = input("Enter a string: ")

# Process and display the result
print("Swapped case string:", custom_swap_case(text))