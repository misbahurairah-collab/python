list1 = list(map(int,input().split()))
list2 = list(map(int,input().split()))
list3 = list(map(int,input().split()))
list4 = list(map(int,input().split()))

diff1 = sorted([x for x in list1 if x not in list2], reverse=True)

diff2 = sorted([x for x in list3 if x not in list4], reverse=True)

union_diff = sorted(list(set(diff1)|set(diff2)),reverse=True)

print(diff1)
print(diff2)
print(union_diff)
