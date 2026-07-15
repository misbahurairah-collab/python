A = int(input())
N = int(input())

mask = (1<<N) - 1
result = A & mask
print("result:",result)
