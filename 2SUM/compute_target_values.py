#!/usr/bin/env python
"""
This will compute the number of target values t in a specified range such that there are distinct numbers in the
input that satisfy x + y = t.  This uses a hash table (dictionary) to achieve linear time.  This uses a variant of the
2-SUM algorithm.
"""

__author__ = "Matt Rathbun"
__version__ = "1.0.0"
__license__ = "GPL"


def create_hash_table():
    """Create the hash table from the input file"""
    hash_table = {}

    with open("algo1-programming_prob-2sum.txt") as f:
    # with open("test_inputs2.txt") as f:
        for line in f:
            hash_table[int(line)] = True

    return hash_table


def compute_distinct_targets(lower_bound, upper_bound, hash_table):
    """Compute the distinct targets for a range using the values in the hash table"""
    distinct_targets = 0

    for i in range(lower_bound, upper_bound):
        for key in hash_table:
            if i - key in hash_table:
                # Must be distinct pairs
                if (i - key) != key:
                    # print "%d + %d = %d" % (key, (i - key), i)

                    distinct_targets += 1

                    break

    return distinct_targets


lower_bound, upper_bound = -10000, 10000
print "Creating hash table..."
inputs = create_hash_table()
print "Counting distinct targets..."
number_of_distinct_targets = compute_distinct_targets(lower_bound, upper_bound, inputs)
print "Number of distinct targets: %d" % number_of_distinct_targets