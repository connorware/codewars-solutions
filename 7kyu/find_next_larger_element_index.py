"""
Least larger

Description:
Task
Given an array of numbers and an index, return either the index of the smallest number that is larger than the element at the given index, or -1 if there is no such index ( or, where applicable, Nothing or a similarly empty value ).

Notes
Multiple correct answers may be possible. In this case, return any one of them.
The given index will be inside the given array.
The given array will, therefore, never be empty.

Example
least_larger( [4, 1, 3, 5, 6], 0 )  ->  3
least_larger( [4, 1, 3, 5, 6], 4 )  -> -1
"""

def least_larger(a, i): 
    larger_no_list = [num for num in a if num > a[i]]

    if not larger_no_list:
        return -1
    
    larger_no_list.sort()
    larger_no = larger_no_list[0]
    larger_index = a.index(larger_no)
    return larger_index