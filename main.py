# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content():
    # [assignment] Add your code here
    with open('story.txt') as f:
        contents = f.read()
        print(contents)

read_file_content()
    

def count_words():
    text = read_file_content("/Downloads/Reading-Text-File/story.txt")
    # [assignment] Add your code here

from collections import Counter
def word_count(fname):
        with open(fname) as f:
                return Counter(f.read().split())

print("Number of words in the file :",word_count("story.txt"))  
