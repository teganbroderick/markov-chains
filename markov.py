"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    file = open(file_path)
    file_string = file.read()
    #print(file_string)
    
    return file_string

def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    # your code goes here
    text_list = text_string.split()

    # loop over list
    for i in range(len(text_list) - 2):
    # create keys based on index (0,1), (1,2) save them as tuples somehow
        temp_tuple = (text_list[i], text_list[i + 1])
        temp_value = text_list[i + 2]
       
        
        #if key not in dictionary:
        if temp_tuple not in chains:
            #create a list: idea: 
            chains[temp_tuple] = []
            #add value to list
            chains[temp_tuple].append(temp_value)
            
        else:
            #append value to existing list
            chains[temp_tuple].append(temp_value)


    for key, value in chains.items():
        print(f"{key}, {value}")
    #print(chains)

    # use tuples to go back into list and identify next word after (values)
    #loop through the keys in the chains dict
        #for each chain, find key tuple in text_list
        #find word immediately after tuple
        #put that word in a value list
        #asociate value list with key

    #   put them into a value list
    # put everything into chains dict
    return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    # your code goes here

    return " ".join(words)


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)