# author: Jack Farah
# Description: Binary search implementation in python. O(log N) time complexity


from os import *
from math import *


def binary_search(array1, value):

    start = 0
    end = len(array1)

    if end ==0:
        return False
    while start < end:
        midpoint = int((start + end)/2)

        if array[midpoint] == value:
            return True
        elif array[midpoint] < value:
            start = midpoint + 1
        elif array[midpoint] > value:
            end = midpoint
    return False


array = [-22, -5, 7, 15, 22, 30, 45, 88, 90, 100, 105]

print(binary_search(array, 50))













