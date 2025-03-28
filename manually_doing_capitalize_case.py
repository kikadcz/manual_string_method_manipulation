#Prog09. capitalize() makes the first letter of the string, capital letter. And all other letter in small case. Create a program that do the same functionality without using capitalize() function.

def custom_capitalize(text):
    if not text:  # Handle empty string
        return text

    # Convert everything to lowercase first
    text = text.lower()

    # Capitalize the first character and join with rest of string
    return text[0].upper() + text[1:]


# Get user input
text = input("Enter a string: ")

# Process and display the result
print("Capitalized string:", custom_capitalize(text))