def coinChangeRecursive(arr, ind, n):
    if n == 0:
        return 1
    
    if n < 0:
        return 0
    
    if n > 0 and ind == len(arr):
        return 0
    
    return (coinChangeRecursive(arr, ind, n - arr[ind]) + coinChangeRecursive(arr, ind+1, n))

def coinChangeWaysDP(arr, ind, n):

    table = [[0 for x in range(n+1)] for x in range(len(arr))]

    for i in range(len(arr)):
        table[i][0] = 1

    for i in range(n+1):
        if(i % arr[0] == 0):
            table[0][i] = 1

    for i in range(1,len(arr)):
        for j in range(1,n + 1):
            if arr[i] > j:
                table[i][j] = table[i - 1][j]
            else:
                table[i][j] = table[i - 1][j] + table[i][j - arr[i]]

    return table[len(arr)-1][n]