"""This module provides functions for testing purposes."""

# Implement quicksort for me: https://en.wikipedia.org/wiki/Quicksort
def quicksort(arr):
    """
    Sorts an array using the quicksort algorithm.
    arr: list of integers
    returns: list of integers
    """
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)
