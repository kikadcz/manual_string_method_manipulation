#Prog02. removeprefix() remove the characters at the beginning of the string that matches the function parameter. Create a program that do the same functionality without using removeprefix() function.

def remove_prefix(s, prefix):
    if s.startswith(prefix):
        return s[len(prefix):]
    return s

# Get input from user
text = input("Enter a string: ")
prefix = input("Enter the prefix to remove: ")

# Show the result
print(f"Original string: {text}")
print(f"Prefix to remove: {prefix}")
print(f"Result: {remove_prefix(text, prefix)}")