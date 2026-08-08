n = int(input())
list = []
for _ in range(n):
    list.append(int(input()))
print("List after appending elements:",list)
n = int(input())
popped = list.pop(n)

print("List after popping element:",list)
print("Popped element:",popped)
