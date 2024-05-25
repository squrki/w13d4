# Implement Bubble Sort:
#    - Write a Python function `bubble_sort(arr)` that takes a list `arr` as input and returns the sorted list using the Bubble Sort algorithm.
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(1, len(arr)-i):
            if arr[j] < arr[j-1]:
                temp = arr[j]
                arr[j] = arr[j-1]
                arr[j-1] = temp
    return arr

#    - Test your implementation with sample input lists and verify the correctness of the output.

#    - Count the number of comparisons and swaps performed by Bubble Sort for each test case.

 

# Implement Selection Sort:
#    - Write a Python function `selection_sort(arr)` that takes a list `arr` as input and returns the sorted list using the Selection Sort algorithm.
def selection_sort(arr):
    # temp = 0
    for i in range(len(arr)):
        for j in range(len(arr)-i):
            if arr[i] < arr[len(arr)-1-j]:
                continue
            else:
                temp = arr[i]
                arr[i] = arr[len(arr)-1-j]
                arr[len(arr)-1-j] = temp

    return arr

#    - Test your implementation with sample input lists and verify the correctness of the output.

#    - Count the number of comparisons and swaps performed by Selection Sort for each test case.

 

# Implement Insertion Sort:
#    - Write a Python function `insertion_sort(arr)` that takes a list `arr` as input and returns the sorted list using the Insertion Sort algorithm.
def insertion_sort(arr):
    
    return arr

#    - Test your implementation with sample input lists and verify the correctness of the output.

#    - Count the number of comparisons and swaps performed by Insertion Sort for each test case.

 

# Time Complexity Analysis:
#    - Analyze the time complexity of each sorting algorithm in the best-case, average-case, and worst-case scenarios.

#    - Provide a brief explanation of your analysis and the reasoning behind the time complexity for each algorithm.

 

# Comparison of Sorting Algorithms:
#    - Create a table or chart comparing the time complexity, number of comparisons, and number of swaps for Bubble Sort, Selection Sort, and Insertion Sort.

#    - Discuss the observations and insights gained from the comparison.

#    - Identify scenarios where each sorting algorithm might be preferred based on their characteristics.

 

# Testing and Evaluation:
#    - Create a set of test cases with different input sizes and initial order of elements (e.g., already sorted, reverse sorted, random).

#    - Evaluate the performance of each sorting algorithm on the test cases and record the execution time, number of comparisons, and number of swaps.

#    - Analyze the results and discuss any discrepancies or interesting findings.

import random

arr=random.sample(range(100),30)
print(arr)
# sorted = bubble_sort(arr)
sorted = selection_sort(arr)
print(sorted)
