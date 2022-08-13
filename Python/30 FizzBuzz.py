"""FizzBuzz.py
FizzBuzz is a well known programming assignment,
asked during interviews.

It takes an input n and outputs the numbers from 1 to n where:
    a multiple of 3 outputs Fizz
    a multiple of 5 outputs Buzz
    both output both.

As an added difficulty skip all even numbers
"""

def main():
    print("Please input how many rounds of FizzBuzz you would like to play: ", end='')
    n = int(input())
    for num in range(1,n,2):
        is_num_found = False
        if num % 3 == 0:
            is_num_found = True
            print("Fizz", end='')
        if num % 5 == 0:
            is_num_found = True
            print("Buzz", end='')
        if is_num_found == False:
            print(num, end='')
        print()

main()