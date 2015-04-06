#!/usr/bin/env python
"""This will compute the sum of the medians for some input using the Median Maintenance algorithm"""

from heapq import heappush, heappop

__author__ = "Matt Rathbun"
__version__ = "1.0.0"
__license__ = "GPL"


def median_maintenance(inputs):
    """
    Determine the sum of the medians in the input, treating input as a series of cards being looked at one at a time
    """
    heap_low, heap_high = [], []
    median_sum = 0

    for i in inputs:
        if len(heap_low) == 0 or i < heap_low[0] * -1:
            heappush(heap_low, i * -1)
        else:
            heappush(heap_high, i)

        # Fix imbalances
        if len(heap_low) - len(heap_high) > 1:
            heappush(heap_high, heappop(heap_low) * -1)
        elif len(heap_high) - len(heap_low) > 1:
            heappush(heap_low, heappop(heap_high) * -1)

        # Find the median
        low_length, high_length = len(heap_low), len(heap_high)

        if low_length == high_length or low_length > high_length:
            median_sum += heap_low[0] * -1
        else:
            median_sum += heap_high[0]

    return median_sum


print "Reading input file..."
inputs = [int(line.rstrip('\n\r')) for line in open('Median.txt')]
print "Computing median sum..."
median_sum = median_maintenance(inputs) % 10000
print "Median sum: %d" % median_sum