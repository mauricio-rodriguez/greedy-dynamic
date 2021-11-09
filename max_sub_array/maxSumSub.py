import math

def maxSubArraySumNaive(arr):
  max_sum = -math.inf
  for i in range(0, len(arr)):
    current_sum=0
    for j in range(i, len(arr)):
      current_sum += arr[j]
      max_sum = max(current_sum, max_sum) #compare the resulting sum with the existing max_sum value
  return max_sum    

def maxCrossingSum(arr, low, mid, high):
    sum = 0
    left_sum = -10000
 
    for i in range(mid, low-1, -1):
        sum = sum + arr[i]
 
        if (sum > left_sum):
            left_sum = sum
    sum = 0
    right_sum = -1000
    for i in range(mid + 1, high + 1):
        sum = sum + arr[i]
 
        if (sum > right_sum):
            right_sum = sum
    return max(left_sum + right_sum, left_sum, right_sum)
 
 
# Returns sum of maximum sum subarray in aa[l..h]
def maxSubArraySumDC(arr, low, high):
 
    if (low == high):
        return arr[low]

    mid = (low + high) // 2
    return max(maxSubArraySumDC(arr, low, mid),
               maxSubArraySumDC(arr, mid+1, high),
               maxCrossingSum(arr, low, mid, high))

def maxSubArraySumKadane(arr,size):
    max_sum = -math.inf
    current_sum = 0
     
    for i in range(0, size):
        if arr[i] > arr[i] + current_sum:
            current_sum = arr[i]
        else:
            current_sum += arr[i]
        if current_sum > max_sum:
            max_sum = current_sum
             
    return max_sum
 