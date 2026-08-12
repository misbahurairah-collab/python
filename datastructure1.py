'''Tom wants to create a dictionary that lists the first n prime numbers, where each key represents the position of the prime number,
and the value is the prime number itself. Help Tom generate this dictionary based on the input she provides.'''

n=int(input())
d={}
p=2
count=0
while count < n:
    for i in range(2, int(p**0.5)+1):
        if p%i ==0:
            break
    else:
        count += 1
        d[count]=p
    p += 1
print(d)
