"""
Heap Sort Implementation Module
This module implements heap sort algorithm and related heap operations for Python lists.
Note: Python arrays are 0-indexed.
"""


# Question 1
def parent(i: int) -> int:
    """
    Returns the index of the parent node for a given index i in a heap.
    
    In a heap represented as a 0-indexed array:
    - The parent of node at index i is at index floor((i-1)/2)
    
    Args:
        i: Index of the current node
        
    Returns:
        Index of the parent node
        
    Example:
        >>> parent(1)  # Left child of root
        0
        >>> parent(2)  # Right child of root
        0
        >>> parent(3)  # Left child of node 1
        1
    """
    return (i - 1) // 2


# Question 2
def left(i: int) -> int:
    """
    Returns the index of the left child node for a given index i in a heap.
    
    In a heap represented as a 0-indexed array:
    - The left child of node at index i is at index 2*i + 1
    
    Args:
        i: Index of the current node
        
    Returns:
        Index of the left child node
        
    Example:
        >>> left(0)  # Left child of root
        1
        >>> left(1)  # Left child of node 1
        3
        >>> left(2)  # Left child of node 2
        5
    """
    return 2 * i + 1


# Question 3
def right(i: int) -> int:
    """
    Returns the index of the right child node for a given index i in a heap.
    
    In a heap represented as a 0-indexed array:
    - The right child of node at index i is at index 2*i + 2
    
    Args:
        i: Index of the current node
        
    Returns:
        Index of the right child node
        
    Example:
        >>> right(0)  # Right child of root
        2
        >>> right(1)  # Right child of node 1
        4
        >>> right(2)  # Right child of node 2
        6
    """
    return 2 * i + 2


# Question 4
def is_max_heap(arr: list, i: int = 0, key: callable = lambda x: x) -> bool:
    """
    Checks if a list satisfies the max-heap property starting from a given index.
    
    A max-heap property states that for every node i (except the root),
    the value of the parent node is greater than or equal to the value of node i.
    
    Args:
        arr: The list to check
        i: Starting index to begin checking from (default: 0)
        key: Function that returns the comparison key for each item (default: identity function)
        
    Returns:
        True if the array is a max-heap from index i onwards, False otherwise
        
    Example:
        >>> is_max_heap([10, 8, 5, 3, 2, 1])
        True
        >>> is_max_heap([10, 8, 12, 3, 2, 1])  # 12 > 8, violates max-heap property
        False
    """
    n = len(arr)
    
    # Check every node starting from i+1
    for j in range(i + 1, n):
        parent_idx = parent(j)
        # If parent is smaller than child, it's not a max-heap
        if key(arr[parent_idx]) < key(arr[j]):
            return False
    
    return True


# Question 5
def max_heapify(arr: list, i: int, heap_size: int, key: callable = lambda x: x) -> None:
    """
    Maintains the max-heap property for a subtree rooted at index i.
    
    This function assumes that the subtrees rooted at left(i) and right(i) are already
    max-heaps, but node i might violate the max-heap property with respect to its children.
    It "floats down" the value at index i to restore the max-heap property.
    
    Args:
        arr: The list representing the heap
        i: Index of the root of the subtree to heapify
        heap_size: Size of the heap (elements from heap_size onwards are excluded)
        key: Function that returns the comparison key for each item
        
    Returns:
        None (modifies arr in-place)
        
    Time Complexity: O(log n) where n is heap_size
    
    Example:
        If arr = [4, 10, 8, 3, 2, 1] and we call max_heapify(arr, 0, 6),
        it will swap 4 with 10, resulting in [10, 4, 8, 3, 2, 1],
        then swap 4 with 3 if needed, and so on.
    """
    l = left(i)
    r = right(i)
    largest = i
    
    # Check if left child exists and is larger than current largest
    if l < heap_size and key(arr[l]) > key(arr[largest]):
        largest = l
    
    # Check if right child exists and is larger than current largest
    if r < heap_size and key(arr[r]) > key(arr[largest]):
        largest = r
    
    # If the largest is not the current node, swap and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        # Recursively heapify the affected subtree
        max_heapify(arr, largest, heap_size, key)


# Question 6
def build_max_heap(arr: list, key: callable = lambda x: x) -> None:
    """
    Builds a max-heap from an arbitrary array.
    
    This function converts an unsorted array into a max-heap by calling max_heapify
    on all non-leaf nodes, starting from the last non-leaf node and moving up to the root.
    
    The last non-leaf node is at index floor(n/2) - 1, where n is the length of the array.
    We work backwards because max_heapify assumes that the children are already max-heaps.
    
    Args:
        arr: The list to convert into a max-heap
        key: Function that returns the comparison key for each item
        
    Returns:
        None (modifies arr in-place)
        
    Time Complexity: O(n) - although max_heapify is O(log n), the overall complexity
                     is O(n) due to the specific structure of the heap.
    
    Example:
        >>> arr = [3, 1, 4, 1, 5, 9, 2, 6]
        >>> build_max_heap(arr)
        >>> arr
        [9, 6, 4, 3, 5, 1, 2, 1]  # Now a max-heap
    """
    n = len(arr)
    
    # Start from the last non-leaf node and move upwards to the root
    # The last non-leaf node is at index (n // 2) - 1
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(arr, i, n, key)


# Question 7
def heap_sort(arr: list, key: callable = lambda x: x) -> None:
    """
    Sorts an array in-place using the heap sort algorithm.
    
    Algorithm:
    1. Build a max-heap from the input array
    2. Repeatedly extract the maximum element (root of heap) and place it at the end
    3. Reduce the heap size and restore the max-heap property
    
    The algorithm works because:
    - After building a max-heap, the largest element is at the root (index 0)
    - We swap it with the last element and reduce the heap size
    - We then heapify the root to restore the max-heap property
    - We repeat until the heap size is 1
    
    Args:
        arr: The list to sort
        key: Function that returns the comparison key for each item
        
    Returns:
        None (modifies arr in-place, sorting it in ascending order)
        
    Time Complexity: O(n log n) in all cases (best, average, and worst)
    Space Complexity: O(1) - sorts in-place
    
    Example:
        >>> arr = [3, 1, 4, 1, 5, 9, 2, 6]
        >>> heap_sort(arr)
        >>> arr
        [1, 1, 2, 3, 4, 5, 6, 9]  # Sorted in ascending order
    """
    n = len(arr)
    
    # Step 1: Build a max-heap from the array
    build_max_heap(arr, key)
    
    # Step 2: Extract elements one by one from the heap
    for i in range(n - 1, 0, -1):
        # Move current root (maximum) to the end
        arr[0], arr[i] = arr[i], arr[0]
        
        # Call max_heapify on the reduced heap
        # The heap size is now i (excluding the sorted elements at the end)
        max_heapify(arr, 0, i, key)


# Example usage and test code
if __name__ == "__main__":
    # Test basic functionality
    print("Testing heap sort implementation:\n")
    
    # Test 1: Simple array
    arr1 = [3, 1, 4, 1, 5, 9, 2, 6]
    print(f"Original array: {arr1}")
    heap_sort(arr1)
    print(f"Sorted array:   {arr1}")
    print()
    
    # Test 2: Already sorted array
    arr2 = [1, 2, 3, 4, 5]
    print(f"Already sorted: {arr2}")
    heap_sort(arr2)
    print(f"After sorting:  {arr2}")
    print()
    
    # Test 3: Reverse sorted array
    arr3 = [5, 4, 3, 2, 1]
    print(f"Reverse sorted: {arr3}")
    heap_sort(arr3)
    print(f"After sorting:  {arr3}")
    print()
    
    # Test 4: Array with duplicates
    arr4 = [3, 3, 3, 1, 1, 2, 2]
    print(f"With duplicates: {arr4}")
    heap_sort(arr4)
    print(f"After sorting:   {arr4}")
    print()
    
    # Test 5: Sorting with custom key function (by absolute value)
    arr5 = [-5, 3, -8, 1, -2, 7]
    print(f"Original array: {arr5}")
    heap_sort(arr5, key=abs)
    print(f"Sorted by abs:  {arr5}")
    print()
    
    # Test 6: Verify is_max_heap function
    arr6 = [10, 8, 5, 3, 2, 1]
    print(f"Array: {arr6}")
    print(f"Is max-heap? {is_max_heap(arr6)}")
    
    arr7 = [10, 8, 12, 3, 2, 1]
    print(f"Array: {arr7}")
    print(f"Is max-heap? {is_max_heap(arr7)}")
    print()
    
    # Test 7: Demonstrate build_max_heap
    arr8 = [3, 1, 4, 1, 5, 9, 2, 6]
    print(f"Before build_max_heap: {arr8}")
    build_max_heap(arr8)
    print(f"After build_max_heap:  {arr8}")
    print(f"Is max-heap? {is_max_heap(arr8)}")
