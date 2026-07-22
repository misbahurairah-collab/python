'''Jonas, a teacher aiming to engage his students visually, 
requires a program to create a sequence of characters. 
The sequence should alternate between two given characters, 
char1 and char2, for a specified number, N. 
Help Jonas with a program that prints the required sequence.'''
c1=input().strip()
c2=input().strip()

n=int(input())

line=1
while line <= n :
    if line % 2 == 1 :
        print(c1 * line, end=" ")
    else:
        print(c2 * line, end=" ")
    line += 1

