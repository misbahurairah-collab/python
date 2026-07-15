'''Emily is studying bitwise operations and is working on a project that involves isolating specific bits from integers. 
She needs to write a program that takes an integer and the number of bits N as input and outputs the value of the lowest N bits of the integer.
Help Emily in her project to understand and visualize how bitwise operations work in practical scenarios.'''

A = int(input())
N = int(input())

mask = (1<<N) - 1
result = A & mask
print("result:",result)
