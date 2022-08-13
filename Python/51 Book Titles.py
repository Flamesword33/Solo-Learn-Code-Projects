"""Book Titles.py
You have been asked to make a special book
categorization program, which assigns each book a
special code based on its title.
The code is equal to the first letter of the book,
followed by the number of characters in the title.
For example the book "Harry Potter", the code 
would be: H12, (Note to self: spaces and punctuation count but \n does not)
as it contains 12 characters.

You are provided a book.txt (I made one from scratch) file, 
which includes the book titles, each one written on a 
seperate line.
Read the title one by one and output the code for each
book on a seperate line.

Input:
Some book
Another book

Output:
S9
A12
"""

def main():
    try:
        my_file = open("Books.txt", "r")
        
        for line in my_file:
            print(repr(line))
            line = line.strip()
            line_length = len(line)
            print(line[0] + str(line_length))

    except:
        print("ERROR: File does not exist.")

    finally:
        my_file.close()

main()
