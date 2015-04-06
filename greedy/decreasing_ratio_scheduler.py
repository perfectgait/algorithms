#!/usr/bin/env python
"""
Schedule jobs in decreasing order of the ratio (weight / length) and report the sum of weighted completion times of
the resulting schedule
"""

from __future__ import division
from math import ceil

__author__ = "Matt Rathbun"
__version__ = "1.0.0"
__license__ = "GPL"


def find_sum_of_weighted_completion_times(schedule):
    weighted_completion_time = 0
    completion_time = 0

    for job in schedule:
        completion_time += int(job[1])
        weighted_completion_time += completion_time * int(job[0])

    return weighted_completion_time


def create_schedule(jobs):
    """Use merge sort to create a schedule"""
    length = len(jobs)

    if len(jobs) > 1:
        half = int(ceil(length/2))
        left = create_schedule(jobs[:half])
        right = create_schedule(jobs[half:])
        merged = merge_schedule(left, right)

        return merged

    # base case
    return jobs


def merge_schedule(list1, list2):
    """Merge two schedules"""
    merged = []
    i, j = 0, 0
    left_len = len(list1)

    while i < left_len and j < len(list2):
        left_ratio = int(list1[i][0]) / int(list1[i][1])
        right_ratio = int(list2[j][0]) / int(list2[j][1])

        if left_ratio > right_ratio:
            merged.append(list1[i])
            i += 1
        elif right_ratio > left_ratio:
            merged.append(list2[j])
            j += 1
        # tie breaker
        else:
            if int(list1[i][0]) > int(list2[j][0]):
                merged.append(list1[i])
                i += 1
            else:
                merged.append(list2[j])
                j += 1

    # Append the remainder of each list to the merged list
    merged += list1[i:]
    merged += list2[j:]

    return merged


print "Reading input file..."
inputs = [line.strip().rstrip('\r\n').split() for line in open('jobs.txt')]
# Remove the number of jobs as we don't need it
del inputs[0]
print "Creating schedule..."
schedule = create_schedule(inputs)
print "Weighted completion time: %d" % find_sum_of_weighted_completion_times(schedule)