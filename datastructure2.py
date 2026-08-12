'''Ishaan is working on a data analysis task involving matrix transformations. 
He needs to clean a 2D grid of numbers by removing the effect of its main diagonal elements. 
Write a program to transform a given 2D array such that all main diagonal elements are replaced with zero while preserving the rest of the values.'''

import numpy as np
R=int(input().strip())
C=int(input().strip())
values=list(map(int, input().strip().split()))
matrix = np.array(values).reshape(R,C)
for i in range(min(R,C)):
    matrix[i,i]=0
print(matrix)
