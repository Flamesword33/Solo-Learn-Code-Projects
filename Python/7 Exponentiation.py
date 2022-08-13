"""Exponentiation
Exponentiation is the raising of one number to the power of another.
This operation is performed using two asterisks **.

Let's use exponentiation to solve a known problem.
You are offered a choice of eitehr $1,000,000 or 
$0.01 doubled every day for 30 days.

Task:
Write a program to calculate the amount that will result
from doubling to understand which choice results
in a larger amount.

Hint:
Let's see how exponentiation can be useful to perform
the calculation.
For example, if we want to calculate how much
money we will have on the 5th day, we can use this
expression: 0.01*(2**5) = 0.32 dollars.
"""

def main(days):
    x = 1000000
    y = 0.01 * 2**days
    if x > y:
        print("Take the million, its simpler")
    else:
        print("Take the penny, it amounts to: " + str(y))

main(30)