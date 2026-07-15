'''Mandy is debating with her friend Rachel about an interesting mathematical claim.
Rachel asserts that for any positive integer n, the ratio of the sum of n and its triple to the integer itself is always 4.
Mandy, intrigued by this statement, decides to validate it using logical operators and basic arithmetic. 
She wants to confirm if the statement holds true for any positive integer n.'''
                                                
n = int(input())
k = 3*n
l = n+3*n
m = l/n

print("Sum:" ,l)
if m==4:
    print("Rachel's statement is: True")
else:
    print("Rachel's statement is: False")
