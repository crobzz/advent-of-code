## AOC Day 3 Puzzle 1

example = \
"""467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""

import re

def getSymLocations(row):
    symbols = "@#$%^&*-=+/"
    symbolLocations = [ index for index, ltr in enumerate(row) if ltr in symbols ]
    withAdjacentValues = []
    for location in symbolLocations:
        if (location > 0):
            withAdjacentValues.append(location - 1)
        withAdjacentValues.append(location)
        withAdjacentValues.append(location + 1)
    return withAdjacentValues
    
def getNumbers(row):
    list_nums = []
    digit = None
    digit_locs = []
    for i in range(len(row)):
        if row[i].isdigit():
            if not digit:
                digit = row[i]
            else:
                digit += row[i]
            digit_locs.append(i)    
        else:
            if digit:
                list_nums.append((int(digit),digit_locs))
                digit = None
                digit_locs = []
    if digit:
        list_nums.append((int(digit),digit_locs))
    return list_nums
            
#rows = example.split('\n')
rows = open("input.txt","r").readlines()
numRows = len(rows)
print(numRows)

sum = 0
for i in range(len(rows)):
    partNumberLocations = []
    partNumberLocations += getSymLocations(rows[i])
    if i > 0:
        partNumberLocations += getSymLocations(rows[i-1])
    if i < numRows - 1:
        partNumberLocations += getSymLocations(rows[i + 1])
    numbers = getNumbers(rows[i])
    for num, locations in numbers:
        if len(list(set(locations) & set(partNumberLocations))) > 0:
            sum += num
            
print(f"Part1: {sum}")

def getGears(row):
    symbols = "*"
    return [ index for index, ltr in enumerate(row) if ltr in symbols ]
    
sum = 0
for i in range(len(rows)):
    partNumberLocations = []
    partNumberLocations += getNumbers(rows[i])
    if i > 0:
        partNumberLocations += getNumbers(rows[i-1])
    if i < numRows - 1:
        partNumberLocations += getNumbers(rows[i + 1])
    gears = getGears(rows[i])
    for gear in gears:
        gearings = [gear - 1, gear, gear + 1]
        attachments = []
        for number, locations in partNumberLocations:
            if len(list(set(locations) & set(gearings))) > 0:
                attachments.append(number)
        if len(attachments) > 1:
            product = 1
            for attachment in attachments:
                product *= attachment
            sum += product
            
print(f"Part 2: {sum}")
