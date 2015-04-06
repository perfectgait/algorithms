# Greedy algorithms for minimizing the weighted sum of completion times for jobs

## Problems
### Question 1
This file describes a set of jobs with positive and integral weights and lengths. It has the format

number_of_jobs

job_1_weight job_1_length

job_2_weight job_2_length

...

For example, the third line of the file is "74 59", indicating that the second job has weight 74 and length 59. You
should NOT assume that edge weights or lengths are distinct.

Your task in this problem is to run the greedy algorithm that schedules jobs in decreasing order of the difference
(weight - length).