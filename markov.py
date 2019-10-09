"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    file = open(file_path)
    file_string = file.read()

    return file_string

def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains"""

    chains = {}

    text_list = text_string.split()

    for i in range(len(text_list) - 2):
        temp_tuple = (text_list[i], text_list[i + 1])
        temp_value = text_list[i + 2]

        if temp_tuple not in chains: #if key not in dictionary
            chains[temp_tuple] = [] #make empty list
            chains[temp_tuple].append(temp_value) #append value to list
            
        else:
            chains[temp_tuple].append(temp_value) #append value to existing list

    # for key, value in chains.items():
    #      print(f"{key}, {value}")

    return chains

def make_text(chains):
    """Return text from chains."""

    words = []

    #Get original text string using open_and_read_file function
    original_text_string = open_and_read_file(input_path)
    text_list = original_text_string.split()
    
    #assign first two words as key
    new_key = (text_list[0], text_list[1])
    
    #append first two words to words list
    words.append(text_list[0])
    words.append(text_list[1])

    while new_key in chains:
        chosen_word = choice(chains[new_key])
        words.append(chosen_word)
        
        #Extra feature: end loop when last character in chosen_word is . or ?
        # if chosen_word[-1] == "." or chosen_word[-1] == "?":
        #     break

        new_key = (new_key[1], chosen_word)

    return " ".join(words)

input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
