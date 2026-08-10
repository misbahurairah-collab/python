'''Meenu loves working with numbers and sets. She has a list of integers and wants to remove any duplicate values and 
sort the remaining numbers in ascending order. She is looking for your help to write a program that can accomplish this task. 
Given a list of integers, your task is to convert the list into a set to remove duplicates, and then return the sorted list of unique integers.'''

a=input()
b=a.split()
c=[int(x) for x in b]
d=set(c)
e=sorted(list(d))
print(e)
