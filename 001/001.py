import os
import csv
import itertools


def findLarger():
    count = 0
    with open('./data.txt', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
       # print(data)
        print(len(data))
        merged = list(itertools.chain.from_iterable(data))
        print(merged)

        merged = list(map(int, merged))

    for i in range(1, len(merged)):
        if merged[i] > merged[i-1]:
            count += 1
    print("Value:", count)
    return


def findLarger3():
    count = 0
    with open('./data.txt', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
       # print(data)
        print(len(data))
        merged = list(itertools.chain.from_iterable(data))
        print(merged)

        merged = list(map(int, merged))

    for i in range(len(merged)-3):
        firstThree = sum(merged[i:i+3])
        secondThree = sum(merged[i+1:i+4])
        if(firstThree < secondThree):
            count += 1
    print("Value:", count)


def flatten(t):
    return [item for sublist in t for item in sublist]


def main():
    findLarger3()


__init__ = main()

# Part 1

# file = open('p1_input.txt')
# data = [int(i) for i in file.readlines()]

# # track n of increases
# increased=0

# # loop through list indices
# for i in range(0,len(data)-1):
#     # read in number and next at each index
#     n1 = data[i]
#     n2 = data[i+1]
#     # compare, increment increased if increase
#     if n1<n2:
#         increased = increased+1
# print(increased)

# Part 2

# # track n of increases
# increased=0

# # loop through list indices
# for i in range(0,len(data)-3):
#     # calculate sums for series of 3 and next series
#     sum1 = sum(data[i:i+3])
#     sum2 = sum(data[i+1:i+4])
#     # compare, increment increased if increase
#     if sum1<sum2:
#         increased = increased+1
# print(increased)


# I'd say the main non-pythonic thing happening is range(0, len(data) - 1) (by the way, if you call range(0, n), it's the same as just range(n)). In python, you should almost always directly iterate over data structures, and use helpers such as zip, enumerate, and everything in the itertools module.

# Here's something you can do for part 1:

# increased = 0
# for n1, n2 in zip(data, data[1:]):
#     if n1 < n2:
#         increased += 1

# You can replace incrementing in an if statement by

# increased += n1 < n2

# You can make this all one line by doing

# print(sum(n1 < n2 for n1, n2 in zip(data, data[1:])))

# The data[1:] slice still copies data though, so you can do:

# from itertools import islice
# print(sum(n1 < n2 for n1, n2 in zip(data, islice(data, 1, None)))

# You can interpolate between the above options depending on how you want to trade off being concise vs simple

# For part 2, you can do something similar:

# increased = 0 prev_sum = sum(data[:3])

# for discard, add in zip(data, data[3:]):
#     new_sum = prev_sum - discard + add
#     increased += new_sum > prev_sum
#     prev_sum = new_sum

# This similarly makes use of zip, (and has the same issue of a copy, which you can remove by islice). My friend pointed out to me that you can just not even check the sums though, since the sum will only go up when add > discard, so:

# increased = sum(n2 > n1 for n1, n2 in zip(data, islice(data, 3, None)))

# does it, with no copies.
