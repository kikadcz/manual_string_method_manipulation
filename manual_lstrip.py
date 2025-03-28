#Prog01. lstrip() remove the space characters at the beginning of the string. Create a program that do the same functionality without using lstrip() function.

def custom_lstrip(s):
    i = 0
    while i < len(s) and s[i].isspace():
        i += 1
    return s[i:] #Returns everythin after the first non-space character


#Ask user the enter their name
name = input("What's your full name? (Include several space character before typing your name):")
print(f"Original : '{name}'")
print(f"Result   : '{custom_lstrip(name)}'")