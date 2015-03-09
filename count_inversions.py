#!/usr/bin/env python
"""This module determines how many inversions exist in a given input using the merge sort algorithm"""

from __future__ import division
from math import ceil

__author__ = "Matt Rathbun"
__version__ = "1.0.0"
__license__ = "GPL"


def merge_sort_inversions(list):
    """Merge sort and count the number of inversions"""
    length = len(list)

    if len(list) > 1:
        half = int(ceil(length/2))
        left, inversions_left = merge_sort_inversions(list[:half])
        right, inversions_right = merge_sort_inversions(list[half:])
        merged, inversions = merge_inversions(left, right)

        return merged, (inversions_left + inversions_right + inversions)

    # base case
    return list, 0


def merge_inversions(list1, list2):
    """Merge two lists and count the number of inversions"""
    merged = []
    i, j = 0, 0
    inversions = 0
    left_len = len(list1)

    while i < left_len and j < len(list2):
        if list1[i] <= list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1
            inversions += left_len - i

    # Append the remainder of each list to the merged list
    merged += list1[i:]
    merged += list2[j:]

    return merged, inversions



inputs = [int(line.rstrip('\n\r')) for line in open('IntegerArray.txt')]

print "Number of inversions: %d" % merge_sort_inversions(inputs)[1]
