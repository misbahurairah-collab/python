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
