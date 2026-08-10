'''Arjun is a data analyst who needs to process a list of integers from a company's sales data.
The data includes both positive and negative sales figures. His task is to rearrange the sales figures
so that all negative sales are placed first, followed by the positive sales, while maintaining the original order within each group.
Help Arjun implement a program that rearranges the list of sales figures as per the required format.'''

lst = eval(input())
negatives = [x for x in lst if x < 0]
positives = [x for x in lst if x >= 0]
result = negatives + positives
print('[' + ','.join(map(str,result)) + ']')
