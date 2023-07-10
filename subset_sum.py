
# Subset Sum Problem

## Problem Statement:

### You are given an array and target. You have to find any
### subsets available that are equal to the target. 

## Solution:

### Create a 2D array 

def subSum(arr, target):
    
    # Instatiate Array
    arr_len = len(arr)
    new_arr = [[None]*(target + 1) for i in range (arr_len+1)]

    # If number of elements in new_arr are 0, target sum = 0 (impossible)
    for i in range(target + 1):
        new_arr[0][i] = False
    for j in range(arr_len + 1):
        new_arr[j][0] = True        

    # Nested for loop, an element can be chosen only if sum is less than arr[i]
    for i in range(1, arr_len + 1):
        for j in range(target + 1):
            if arr[i - 1] <= j:
                new_arr[i][j] = new_arr[i - 1][j] or new_arr[i - 1][j - arr[i - 1]]
            else:
                new_arr[i][j] = new_arr[i - 1][j]
    return new_arr[arr_len][target]

def main():
    arr = [0, 3, 7, 1]
    target = 6
    exists =  subSum(arr,target)
    print('Subset with Target sum exists : ', str(exists))

    arr = [0, 3, 2, 7, 1]
    target = 6
    exists =  subSum(arr,target)
    print('Subset with Target sum exists : ', str(exists))

if __name__ == '__main__':
    main()