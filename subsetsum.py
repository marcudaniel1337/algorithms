def subset_sum(nums, target):
    """
    Find all subsets of nums that sum up exactly to the target value.

    Args:
        nums (list of int): The list of numbers to consider.
        target (int): The target sum we want subsets to match.

    Returns:
        list of lists: A list containing all subsets that sum to target.
    """

    results = []  # To store all valid subsets

    def backtrack(start, current_subset, current_sum):
        """
        Recursive backtracking function to explore subsets.

        Args:
            start (int): The index in nums to start from.
            current_subset (list): The current subset being built.
            current_sum (int): The sum of elements in current_subset.
        """
        # If current sum matches target, we found a valid subset
        if current_sum == target:
            # Append a copy of the current subset to results
            results.append(current_subset[:])
            return

        # If current sum exceeds target, no need to continue this path
        if current_sum > target:
            return

        # Explore further elements starting from 'start'
        for i in range(start, len(nums)):
            # Include nums[i] in the current subset
            current_subset.append(nums[i])
            # Recurse with updated sum and next start index (i + 1)
            backtrack(i + 1, current_subset, current_sum + nums[i])
            # Backtrack: remove last element and try next possibility
            current_subset.pop()

    # Start backtracking with empty subset and sum 0
    backtrack(0, [], 0)

    return results


if __name__ == "__main__":
    numbers = [2, 3, 6, 7]
    target_sum = 7

    print(f"Finding subsets of {numbers} that sum to {target_sum}...\n")
    subsets = subset_sum(numbers, target_sum)

    print(f"Total subsets found: {len(subsets)}\n")
    for idx, subset in enumerate(subsets, start=1):
        print(f"Subset #{idx}: {subset}")
