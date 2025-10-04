def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i -1
        while j >=0 and arr[j]> arr[j+1]:
            # Swap
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp
            j -= 1
    return arr
            
numbers = [5, 2, 4, 6, 1]
sorted_numbers = insertion_sort(numbers)
print(sorted_numbers)