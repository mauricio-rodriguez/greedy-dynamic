def coinChangeRecursive(arr, ind, n):
    if n == 0:
        return 1
    
    if n < 0:
        return 0
    
    if n > 0 and ind == len(arr):
        return 0
    
    return (coinChangeRecursive(arr, ind, n - arr[ind]) + coinChangeRecursive(arr, ind+1, n))

def coinChangeWaysDP(arr, ind, n):

    table = [[0 for x in range(ind)] for x in range(n+1)]
    
    for i in range(ind):
        table[0][i] = 1

    for i in range(1, n+1):
        for j in range(ind):
 
            x = table[i - arr[j]][j] if i-arr[j] >= 0 else 0
            y = table[i][j-1] if j >= 1 else 0
            table[i][j] = x + y
 
    return table[n][ind-1]