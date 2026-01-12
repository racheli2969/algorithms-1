
def partition(arr, left, right, key=lambda x: x):
    """
    Lomuto partition scheme with key function support.
    """
    pivot = key(arr[right])
    i = left - 1
    
    for j in range(left, right):
        if key(arr[j]) <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1


def quick_kth(arr, left, right, k, key=lambda x: x):
    """
    Quick select algorithm to find the k-th smallest element.
    
    Parameters:
    - arr: The array to search in
    - left: Left boundary index
    - right: Right boundary index
    - k: The k-th smallest element to find (0-indexed)
    - key: Function to extract comparison key from elements
    
    Returns:
    - The k-th smallest element
    """
    if left == right:
        return arr[left]
    
    # Partition the array and get the pivot index
    pivot_index = partition(arr, left, right, key)
    
    # The pivot is in its final sorted position
    if k == pivot_index:
        return arr[k]
    elif k < pivot_index:
        # k-th element is in the left partition
        return quick_kth(arr, left, pivot_index - 1, k, key)
    else:
        # k-th element is in the right partition
        return quick_kth(arr, pivot_index + 1, right, k, key)