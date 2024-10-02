# Main function

def main():
    # stores a file path in variable book_path.
    book_path = "books/frankenstein.txt"

    # initializes a variable to convert results from get_text function.
    text = get_text(book_path)

    #initializes a variable to convert all text to lowercase.
    lowercase = lower_case_text(text)

    # initializes a variable to convert results from get_word_count function.
    wordcount = get_word_count(text)

    # initializes a variable to convert results from character_count function.
    character = character_count(lowercase)
    
    # prints character variable and f-string for wordcount variable as results
    print(f"--- Begin analysis of {book_path} ---")
    print()
    print(f"There are a total of {wordcount} words found in the document")
    print()
    # prints key, value pair as c for character, v for value iteratively through the dictionary using the .items method
    for c, v in character.items():
        print(f"The {c} character appeared {v} times")
    print()
    print("------------ End Analysis ------------")
    
# takes lowercase variable data and prints each individual letter.    
def character_count(lowercase):
    # add dictionary to track number of occurences of each alphabetic letter.
    counter = {}
    for char in lowercase:
        if char.isalpha(): # disregard non alphabet characters
            if char in counter:  # if the character is already in the counter, add another count to it.  If it's not, then add 1 count to it.
                counter[char] += 1
            else:
                counter[char] = 1

    return counter

# takes text variable value and transforms all text to be lowercase.
def lower_case_text(text):
    lowercase = text.lower()
    return lowercase

# takes file data and splits it into words rather than one large string.
def get_word_count(text):
    words = text.split()
    return len(words)

# opens file found at filepath and parses the data back to the main()
def get_text(book_path):
    with open(book_path) as f:
        return f.read()
main()