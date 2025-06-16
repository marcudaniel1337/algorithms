def quick_sort(arr):
   # Base case - arrays with 0 or 1 element are already sorted
   if len(arr) <= 1:
       return arr
   
   # Choose pivot (I'm using the middle element, but you could use first/last too)
   pivot = arr[len(arr) // 2]
   
   # Partition the array into three parts
   left = [x for x in arr if x < pivot]      # elements smaller than pivot
   middle = [x for x in arr if x == pivot]   # elements equal to pivot
   right = [x for x in arr if x > pivot]     # elements greater than pivot
   
   # Recursively sort the left and right parts, then combine everything
   return quick_sort(left) + middle + quick_sort(right)

def quick_sort_inplace(arr, low=0, high=None):
   """In-place version that modifies the original array"""
   if high is None:
       high = len(arr) - 1
   
   if low < high:
       # Get the partition index
       pivot_index = partition(arr, low, high)
       
       # Recursively sort elements before and after partition
       quick_sort_inplace(arr, low, pivot_index - 1)
       quick_sort_inplace(arr, pivot_index + 1, high)

def partition(arr, low, high):
   # Choose the rightmost element as pivot
   pivot = arr[high]
   
   # Index of smaller element (indicates right position of pivot)
   i = low - 1
   
   for j in range(low, high):
       # If current element is smaller than or equal to pivot
       if arr[j] <= pivot:
           i += 1
           arr[i], arr[j] = arr[j], arr[i]  # swap elements
   
   # Place pivot in correct position
   arr[i + 1], arr[high] = arr[high], arr[i + 1]
   return i + 1

# Test both versions
if __name__ == "__main__":
   # Test the simple version (creates new arrays)
   numbers1 = [64, 34, 25, 12, 22, 11, 90]
   print(f"Original array: {numbers1}")
   sorted_numbers1 = quick_sort(numbers1)
   print(f"Sorted (new array): {sorted_numbers1}")
   
   # Test the in-place version (modifies original array)
   numbers2 = [64, 34, 25, 12, 22, 11, 90]
   print(f"\nOriginal array: {numbers2}")
   quick_sort_inplace(numbers2)
   print(f"Sorted (in-place): {numbers2}")
