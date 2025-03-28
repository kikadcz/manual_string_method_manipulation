#Prog03. lower() converts all characters of the string into lower case. Create a program that do the same functionality without using lower() function.

def lower(s):
    # Holds the new string
    new_s = ""

    # Go through the string
    for i in s:
        # If it is upper case
        if "A" <= i <= "Z":
            # Change it to lower case and add it
            new_s += chr(ord(i) + 32)
        # If it is not upper case
        else:
            # Just add what it is
            new_s += i

    # Return the new string
    return new_s

# Get user input
text = input("Enter a string: ")

# Print results
print("\nOriginal string:", text)
print("Lowercase string:", lower(text))