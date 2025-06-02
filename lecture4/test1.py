def bubble_sort(lst):
    n = len(lst)
    for i in range(n-1):
        for j in range(0, n-i-1): 
            if lst[j] > lst[j+1] :
                lst[j], lst[j+1] = lst[j+1], lst[j] 
    return lst

numbers = [5, 3, 8, 4, 2]
bubble_sort(numbers)
