# Implementation of the Merge sort with a huge array adding a timer to see how long it takes to sort all data.
import time

start = time.time()

def mergeSort(array):

    if len(array) <= 1:
        return array

    mid = len(array) // 2

    left_side = array[:mid]
    right_side = array[mid:]
    
    sortedLeft  = mergeSort(left_side)
    sortedRight = mergeSort(right_side)

    return merge(sortedLeft, sortedRight)

def merge(left,right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if right[j] > left[i]:
            result.append(right[j])
            j += 1
        else:
            result.append(left[i])
            i += 1

    result.extend(right[j:])
    result.extend(left[i:])

    return result    
        
array = [64, 25, 12, 22, 11, 1, 37, 98, 87, 54, 32, 19, 8, 45, 67, 91, 83, 3, 72, 56, 29, 38, 78, 46, 99, 69, 15, 63, 71, 82, 27, 41, 93, 7, 61, 16, 68, 34, 94, 39, 73, 43, 84, 2, 79, 53, 6, 89, 88, 26, 47, 31, 42, 59, 13, 51, 97, 17, 85, 81, 95, 49, 74, 9, 76, 62, 23, 86, 28, 77, 14, 33, 18, 52, 36, 58, 24, 66, 4, 57, 96, 21, 48, 92, 75, 5, 65, 35, 44, 55, 83, 94, 39, 73, 43, 84, 2, 79, 53, 6, 89, 88, 26, 47, 31, 42, 59, 13, 51, 97, 17, 85, 81, 95, 49, 74, 9, 76, 62, 23, 86, 28, 77, 14, 33, 18, 52, 36, 58, 24, 66, 4, 57, 96, 21, 48, 92, 75, 5, 65, 35, 44, 55]

sortedArr = mergeSort(array)
print("Sorted array:", sortedArr)

end = time.time()
print("Time taken:", end - start, "seconds")




