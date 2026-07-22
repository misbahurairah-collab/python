'''Nithi, a creative programmer, wants to design a program that prints a beautiful pattern using asterisks ('*') and spaces.
She wants to impress her friends with her pattern printing skills. Help Nithi write a program to create the desired
pattern based on the given specifications.Write a program that takes an integer N as input and prints a pattern of size N, 
where N is the number of rows in the pattern.'''

n = int(input())
for i in range(1, n + 1):
    
    print(" " * (n - i) + "* " * i, end="")
    
    print(" " * (2 *(n - i)), end="")
    
    print("* " * i)