'''Dhoni is organizing his tasks for the day and wants to create a simple to-do list using Python.
He plans to input his tasks one by one and then remove them as he completes them.
He wants to create a program that allows him to add tasks, mark them as completed by
removing first and last elements from the list, and visualize his progress.'''

try:
    n=int(input().strip())
except:
    n=0
lst=[]
for _ in range(n):
    try:
        x=int(input().strip())
    except:
        x=0
    lst.append(x)
print("List after appending elements:",lst)
if len(lst)>0:
    popped_last=lst.pop()
else:
    popped_last=None
print("List after popping last element:",lst)
print("Popped element:",popped_last)

if len(lst)>0:
    popped_first=lst.pop(0)
else:
    popped_first=lst.pop(0)
print("List after popping first element:",lst)
print("Popped element:",popped_first)
