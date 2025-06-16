def merge_sort(arr):
   # Base case - if array has 1 or 0 elements, it's already sorted
   if len(arr) <= 1:
       return arr
   
   # Find the middle point to divide the array into two halves
   mid = len(arr) // 2
   
   # Recursively sort both halves
   left_half = merge_sort(arr[:mid])
   right_half = merge_sort(arr[mid:])
   
   # Merge the sorted halves back together
   return merge(left_half, right_half)

def merge(left, right):
   result = []
   i = j = 0  # pointers for left and right arrays
   
   # Compare elements from both arrays and add smaller one to result
   while i < len(left) and j < len(right):
       if left[i] <= right[j]:
           result.append(left[i])
           i += 1
       else:
           result.append(right[j])
           j += 1
   
   # Add any remaining elements from left array (if any)
   while i < len(left):
       result.append(left[i])
       i += 1
   
   # Add any remaining elements from right array (if any)
   while j < len(right):
       result.append(right[j])
       j += 1
   
   return result

# Test it out
if __name__ == "__main__":
   # Example usage
   numbers = [64, 34, 25, 12, 22, 11, 90]
   print(f"Original array: {numbers}")
   
   sorted_numbers = merge_sort(numbers)
   print(f"Sorted array: {sorted_numbers}")
