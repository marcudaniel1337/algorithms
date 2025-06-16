def insertion_sort(arr):
   # Start from the second element (index 1) since first element is considered sorted
   for i in range(1, len(arr)):
       key = arr[i]  # Current element to be inserted into sorted portion
       j = i - 1     # Index of the last element in sorted portion
       
       # Move elements that are greater than key one position ahead
       while j >= 0 and arr[j] > key:
           arr[j + 1] = arr[j]  # shift element to the right
           j -= 1
       
       # Insert the key at its correct position
       arr[j + 1] = key

def insertion_sort_return_new(arr):
   """Version that returns a new sorted array instead of modifying original"""
   new_arr = arr.copy()  # make a copy so we don't modify the original
   
   for i in range(1, len(new_arr)):
       key = new_arr[i]
       j = i - 1
       
       # Shift elements to make room for key
       while j >= 0 and new_arr[j] > key:
           new_arr[j + 1] = new_arr[j]
           j -= 1
       
       new_arr[j + 1] = key
   
   return new_arr

# Test both versions
if __name__ == "__main__":
   # Test in-place version
   numbers1 = [64, 34, 25, 12, 22, 11, 90]
   print(f"Original array: {numbers1}")
   insertion_sort(numbers1)
   print(f"Sorted in-place: {numbers1}")
   
   # Test version that returns new array
   numbers2 = [64, 34, 25, 12, 22, 11, 90]
   print(f"\nOriginal array: {numbers2}")
   sorted_numbers = insertion_sort_return_new(numbers2)
   print(f"Original unchanged: {numbers2}")
   print(f"New sorted array: {sorted_numbers}")
