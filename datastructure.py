'''Gowshik is working on a task that involves taking two lists of integers as input, 
finding the element-wise sum of the corresponding elements, 
and then creating a tuple containing the sum values. Write a program to help Gowshik with this task.'''

n=int(input())
l1=list(map(int,
input().split(',')))
l2=list(map(int,
input().split(',')))
result=tuple(l1[i]+l2[i] for i in range(n))
print(result)
