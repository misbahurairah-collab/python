'''Emma, a mathematics teacher, wants to demonstrate Floyd's triangle to her students during a class activity. She plans to use a program to generate and print Floyd's triangle.
Floyd's triangle is a triangular array of natural numbers. It is defined by filling the rows of the triangle with consecutive numbers, starting with a 1 in the top left corner.
Write a program that takes an integer as input and prints Floyd's triangle up to the specified number of rows.'''

n = int(input())
num = 1
for i in range(1,n+1):
    for j in range(i):
        print(num, end=' ')
        num += 1
    print()
