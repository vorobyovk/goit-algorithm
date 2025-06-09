#bubble sort implementation
# def bubble_sort(lst):
#     n = len(lst)
#     for i in range(n-1):
#         for j in range(0, n-i-1): 
#             if lst[j] > lst[j+1] :
#                 lst[j], lst[j+1] = lst[j+1], lst[j] 
#     return lst

# numbers = [5, 3, 8, 4, 2]
# print("Before sorting:", numbers)
# bubble_sort(numbers)
# print("After sorting:", numbers)

#insertion sort implementation
# def insertion_sort(lst):
#     for i in range(1, len(lst)):
#         key = lst[i]
#         j = i-1
#         while j >=0 and key < lst[j] :
#                 lst[j+1] = lst[j]
#                 j -= 1
#         lst[j+1] = key 
#     return lst

# numbers = [5, 3, 8, 4, 2]
# print("Before insertion sort:", numbers)
# insertion_sort(numbers)
# print("After insertion sort:", numbers)

#selection sort implementation
# def selection_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         min_idx = i
#         for j in range(i+1, n):
#             if arr[j] < arr[min_idx]:
#                 min_idx = j
#         arr[i], arr[min_idx] = arr[min_idx], arr[i]
#     return arr

# numbers = [5, 3, 8, 4, 2]
# print("Before selection sort:", numbers)
# print(selection_sort(numbers))

# Quick sort implementation
# def quicksort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[len(arr) // 2]
#     left = [x for x in arr if x < pivot]
#     middle = [x for x in arr if x == pivot]
#     right = [x for x in arr if x > pivot]
#     return quicksort(left) + middle + quicksort(right)

# print(quicksort([5, 3, 8, 4, 2]))
# # Виведе: [2, 3, 4, 5, 8]

# Merge sort implementation
# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     mid = len(arr) // 2
#     left_half = arr[:mid]
#     right_half = arr[mid:]
#     return merge(merge_sort(left_half), merge_sort(right_half))

# def merge(left, right):
#     merged = []
#     left_index = 0
#     right_index = 0
#     # Спочатку об'єднайте менші елементи
#     while left_index < len(left) and right_index < len(right):
#         if left[left_index] <= right[right_index]:
#             merged.append(left[left_index])
#             left_index += 1
#         else:
#             merged.append(right[right_index])
#             right_index += 1
#     # Якщо в лівій або правій половині залишилися елементи, 
# 		# додайте їх до результату
#     while left_index < len(left):
#         merged.append(left[left_index])
#         left_index += 1
#     while right_index < len(right):
#         merged.append(right[right_index])
#         right_index += 1
#     return merged

# # Example usage
# numbers = [5, 3, 8, 4, 2]
# print("Before merge sort:", numbers)
# print(merge_sort(numbers))

# Shell sort implementation
def shell_sort(arr):
    n = len(arr)
    gap = n // 2    
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr

numbers = [5, 3, 8, 4, 2]
shell_sort(numbers)
print("After shell sort:", numbers)