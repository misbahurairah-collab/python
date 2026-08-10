
'''Yogi wants to merge two lists of integers into a sorted set, eliminating any duplicate elements.
He needs your help to create a Python script that takes two lists of integers as input, 
removes the last element in the first list, converts them into sets, merges them, sorts the resulting set,
and finally outputs the sorted merged set.Write a program to assist Yogi in merging and sorting unique elements from two sets.'''


a=input().split()
b=input().split()
c=[int(num) for num in a]
d=[int(num) for num in b]
c.pop()
set1=set(c)
set2=set(d)
e=set1.union(set2)
sorted_list=sorted(list(e))
print(sorted_list)
