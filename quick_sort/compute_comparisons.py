#!/usr/bin/env python
"""This will compute the number of comparisons used to sort an input using quick sort."""

from __future__ import division
from math import ceil, floor

__author__ = "Matt Rathbun"
__version__ = "1.0.0"
__license__ = "GPL"


def quicksort(input, start, end):
    """Quick sort an input"""
    if end - start <= 0:
        return 0

    pivot = choose_pivot("median", input, start, end)
    # swap the pivot with the first element so that partition never has to change
    input[start], input[pivot] = input[pivot], input[start]

    split = partition(input, start, end)
    comparisons = end - start
    comparisons += quicksort(input, start, split-1)
    comparisons += quicksort(input, split+1, end)

    return comparisons


def partition(input, l, r):
    """Partition an input into two halves using the first element as the pivot"""
    pivot_element = input[l]
    i = l + 1

    for j in range(l + 1, r + 1):
        if input[j] < pivot_element:
            input[i], input[j] = input[j], input[i]
            i += 1

    input[i-1], input[l] = pivot_element, input[i-1]

    return i-1


def choose_pivot(strategy, input, start, end):
    """Chose a pivot point from an input based on a strategy"""
    if strategy == 'right':
        return end
    elif strategy == 'median':
        first, last = input[start], input[end]
        length = end - start

        # this is actually the odd case because arrays are 0 based
        if length % 2 == 0:
            middle_index = start + int(ceil(length / 2))
        else:
            middle_index = start + int(floor(length / 2))

        middle = input[middle_index]

        if first <= middle <= last or last <= middle <= first:
            return middle_index
        elif middle <= first <= last or last <= first <= middle:
            return start
        else:
            return end
    else:
        return start


ten_inputs = [int(line.rstrip('\n\r')) for line in open('10.txt')]
hundred_inputs = [int(line.rstrip('\n\r')) for line in open('100.txt')]
thousand_inputs = [int(line.rstrip('\n\r')) for line in open('1000.txt')]
quicksort_inputs = [int(line.rstrip('\n\r')) for line in open('QuickSort.txt')]

print "Number of comparisons (10): %d, (100): %d, (1000): %d, (quicksort): %d"\
      % (quicksort(ten_inputs, 0, 9),
         quicksort(hundred_inputs, 0, 99),
         quicksort(thousand_inputs, 0, 999),
         quicksort(quicksort_inputs, 0, len(quicksort_inputs) - 1))