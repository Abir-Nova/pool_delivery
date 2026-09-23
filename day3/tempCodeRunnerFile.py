def acronym_from_string(input_string):
    # Split the input string into words
    words = input_string.split()
    # Extract the first letter of each word and join them to make a new word
    result = ''.join(word[0] for word in words)
    return result

#example usage
input_string = "Play your trumpet happily on nights"
result = acronym_from_string(input_string)
print(f"The acronym of the provided string '{input_string}' is: {result}")

#in general
input_string = input("Please enter a string: ")
result = acronym_from_string(input_string)
print(f"The result of the provided string '{input_string}' is: {result}")
