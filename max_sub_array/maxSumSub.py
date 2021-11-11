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
            print("Current sum: ",current_sum)
        else:
            current_sum += arr[i]
            print("Current sum: ",current_sum)
        if current_sum > max_sum:
            max_sum = current_sum
            print("Current sum: ",current_sum)
             
    return max_sum
 
# arr = [-1,-3,-4,-2,-5]
# print("MaxSum: ",maxSubArraySumKadane(arr,5))

def maxSubArraySumKadaneIndex(arr,size):
    max_sum = -math.inf
    current_sum = 0
    start = end = _start = 0
    for i in range(0, size):
        if arr[i] > arr[i] + current_sum:
            current_sum = arr[i]
            _start = i + 1
            # print("Current sum: ",current_sum)
        else:
            current_sum += arr[i]
            # print("Current sum: ",current_sum)
        if current_sum > max_sum:
            max_sum = current_sum
            start = _start
            end = i
            # print("Current sum: ",current_sum)
             
    return max_sum, start - 1, end
