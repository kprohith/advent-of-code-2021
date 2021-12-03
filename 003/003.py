import csv
import sys
import itertools


def main():
    split_data = get_data()


def get_data():
    with open('./data.txt', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
    for i in range(len(data)):
        data[i] = [x for x in data[i]]
        data.append(data[i])
    # print(data)
    split_data = []
    for i in range(len(data)):
        num = data[i][0]
       # print(num)
        num = [(a) for a in str(num)]
        split_data.append(num)
    # print(split_data)
    # print(len(split_data))
    # print(split_data[990][11])

    
    most = []
    least = []
    for j in range(12):
        zeroCount = 0
        oneCount = 0
        for i in range(len(split_data)):
            if int(split_data[i][j]) == 0:
                zeroCount += 1
            else:
                oneCount += 1
        if zeroCount > oneCount:
            most.append(0)
            least.append(1)
        else:
            most.append(1)
            least.append(0)
    print(most, least)
    return split_data


__init__ = main()
