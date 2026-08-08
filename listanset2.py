n=int(input())
workers=input().split()
r_workers=workers = workers[-2:]+workers[:-2]
print(" ".join(r_workers))
