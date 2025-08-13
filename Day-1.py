# Statement: 
# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0 
# in-place. 
# You must do it in place, i.e., modify the original matrix with O(1) extra space (constant space) 
# — you are allowed to use the first row and first column of the matrix for marking. 
# Constraints: 
# ● 1 <= m, n <= 200 
# ● -2³¹ <= matrix[i][j] <= 2³¹ - 1 
# Input: 
# ● A 2D list of integers: matrix 
# Output: 
# ● The input matrix modified in-place 
# Test Case1: 
# Input: 
# matrix = [ 
#     [1, 1, 1], 
#     [1, 0, 1], 
#     [1, 1, 1] 
# ] 
# Output: 
# [1, 0, 1], 
# [0, 0, 0], 
# [1, 0, 1] 
# Test Case2: 
# Input: 
# matrix = [ 
#     [5, 6, 0, 8], 
#     [1, 2, 3, 4], 
#     [0, 7, 9, 1] 
# ] 
# Output: 
# [5, 0, 0, 0], 
# [1, 0, 0, 4], 
# [0, 0, 0, 0] 


# code:

def zeros(matrix):
    m,n=len(matrix),len(matrix[0])
    zero_row=set()
    zero_column=set()
    for i in range(m):
        for j in range(n):
            if matrix[i][j]==0:
                zero_row.add(i)
                zero_column.add(j)
    for i in zero_row:
        for j in range(n):
            matrix[i][j]=0
    for i in zero_column:
        for j in range(m):
            matrix[j][i]=0
    return matrix
m=int(input("enter number of rows:"))
n=int(input("enter number of columns:"))
matrix=[]
for i in range(m):
    row=list(map(int,input().split()))
    matrix.append(row)
result=zeros(matrix)
for row in result:
    print(row)
