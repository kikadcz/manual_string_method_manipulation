#Prog05. endswith() check if the string end part matches the function parameter. Create a program that do the same functionality without using endswith() function.

def custom_endswith(s, suffix):
    # If suffix is empty or longer than string, return False
    if not suffix or len(suffix) > len(s):
        return False

    # Compare characters from the end
    for i in range(len(suffix)):
        if s[-(i + 1)] != suffix[-(i + 1)]:
            return False

    return True


# Get user input
text = input("Enter a string: ")
suffix = input("Enter the suffix to check: ")

# Show result
print(f"Result: {custom_endswith(text, suffix)}")