import numpy as np

def is_magic(matrix):
    # check if matrix is nxn
    dim = matrix.shape
    if len(dim)!=2 or dim[0] != dim[1]: return False
    N = dim[0]        
    
    # calculate the sum of the prime diagonal 
    s = 0
    for i in range(0, N): 
        s = s + matrix[i][i]      
        
    # calculate the sum of the other diagonal
    s2 = 0
    for i in range(0,N):
        s2 = s2 + matrix[i][N-i-1]
        
    if (s != s2): return False
    
    # For sums of Rows
    for i in range(0, N):
        rowSum = 0;      
        for j in range(0, N): 
            rowSum += matrix[i][j]   
            
        # check if every row sum is equal to prime diagonal sum 
        if (rowSum != s): 
            return False
        
    # For sums of Columns 
    for i in range(0, N): 
        colSum = 0
        for j in range(0, N): 
            colSum += matrix[j][i]   
            
        # check if every column sum is equal to prime diagonal sum
        if (s != colSum):
            return False
        
    # if all yes, return true
    return True

# test program:
A = np.array([[4,9,2],
             [3,5,7],
             [8,1,6]])
B = np.array([[3,9,2],
              [4,5,7],
              [8,1,6]])

print(f"Is A magic? {is_magic(A)}")
print(f"Is B magic? {is_magic(B)}")