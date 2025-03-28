#Prog07. center() add space characters at the beginning and at the end of the string to print the string at the center. Create a program that do the same functionality without using center() function.

def center_me(a):
    # Find the longest string
    max_len = len(max(a, key=len))

    # Center each string
    for i in a:
        spaces = max_len - len(i)
        left_spaces = spaces // 2
        right_spaces = spaces - left_spaces
        print(" " * left_spaces + i + " " * right_spaces)


# Get strings from user
print("Enter strings (press Enter twice to finish):")
strings = []
while True:
    s = input()
    if s == "":
        if strings:
            break
        continue
    strings.append(s)

# Center the strings
center_me(strings)