# Implement Bubble Sort:
#    - Write a Python function `bubble_sort(arr)` that takes a list `arr` as input and returns the sorted list using the Bubble Sort algorithm.
def bubble_sort(arr):
    count = 0
    for i in range(len(arr)):
        for j in range(1, len(arr)-i):
            if arr[j] < arr[j-1]:
                temp = arr[j]
                arr[j] = arr[j-1]
                arr[j-1] = temp
            count += 1
    print(count)
    return arr

#    - Test your implementation with sample input lists and verify the correctness of the output.

#    - Count the number of comparisons and swaps performed by Bubble Sort for each test case.

 

# Implement Selection Sort:
#    - Write a Python function `selection_sort(arr)` that takes a list `arr` as input and returns the sorted list using the Selection Sort algorithm.
def selection_sort(arr):
    count = 0
    for i in range(len(arr)):
        for j in range(len(arr)-i):
            if arr[i] < arr[len(arr)-1-j]:
                count += 1
                continue
            else:
                count += 1
                temp = arr[i]
                arr[i] = arr[len(arr)-1-j]
                arr[len(arr)-1-j] = temp
    print(count)
    return arr

#    - Test your implementation with sample input lists and verify the correctness of the output.

#    - Count the number of comparisons and swaps performed by Selection Sort for each test case.

 

# Implement Insertion Sort:
#    - Write a Python function `insertion_sort(arr)` that takes a list `arr` as input and returns the sorted list using the Insertion Sort algorithm.
def insertion_sort(arr):
    count = 0
    for i in range(len(arr)):
        temp = arr[i]
        index = i
        for j in range(i, len(arr)):
            if arr[index] < arr[j]:
                count += 1
                continue
            else:
                count += 1
                temp = arr[j]
                index = j
        arr[index] = arr[i]
        arr[i] = temp
    print(count)
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
size = 1000
sample = 100
randm=random.sample(range(size),sample)
sorted = []
reverse = []
for i in range(sample):
    sorted.append(i)
    reverse.append(sample-i)
print("sorted :",sorted)
print("reverse:",reverse)
print("random :",randm)

print("bubble_sort")
print("sorted")
bubble_sort(sorted)
print("reverse")
bubble_sort(reverse)
print("random")
bubble_sort(randm)

print("selection_sort")
print("sorted")
selection_sort(sorted)
print("reverse")
selection_sort(reverse)
print("random")
selection_sort(randm)

print("insertion_sort")
print("sorted")
insertion_sort(sorted)
print("reverse")
insertion_sort(reverse)
print("random")
insertion_sort(randm)

# bubble sort has less iterations than selection or insertion. Selection and insertion has the same number of iterations.
