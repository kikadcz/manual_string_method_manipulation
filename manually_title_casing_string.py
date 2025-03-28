#Prog10. title() makes all first letter of each word in the string, capital letter. And all other letter in small case. Create a program that do the same functionality without using title() function.

def capitalize_word(word):
    # Convert first character to uppercase and rest to lowercase
    return word[0].upper() + word[1:].lower()

def custom_title(input_text):
    # Split text into words, capitalize each word, and join back together
    words = input_text.split()
    capitalized_words = [capitalize_word(word) for word in words]
    return ' '.join(capitalized_words)

# Get user input
text = input("Enter your text: ")

# Process and display result
result = custom_title(text)
print("Result:", result)