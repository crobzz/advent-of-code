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
    '''
    Gets locations of symbols from a given row of text. Adds the adjacent indeces
    into the return list because adjacent numbers are valid.
    '''
    symbols = "@#$%^&*-=+/"
    ## List comprehension
    # # The following for loop is an equivalent statement
    # symbolLocations = []
    # for i in range(len(row)):
    #     letter = row[i]
    #     if letter in symbols:
    #         symbolLocations.append(i)
    symbolLocations = [ index for index, ltr in enumerate(row) if ltr in symbols ]
    withAdjacentValues = []
    for location in symbolLocations:
        if (location > 0):
            withAdjacentValues.append(location - 1)
        withAdjacentValues.append(location)
        withAdjacentValues.append(location + 1)
    return withAdjacentValues
    
def getNumbers(row):
    '''
    Retrieves all numbers from a row with a list of their index(es)
    Returns a list of tuples<int, list[int]> (full number, indexes on the row)
    '''
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
# Step 1. Separate input into rows (on the newline character '\n')
rows = open("input.txt","r").readlines()
numRows = len(rows)
print(numRows)

## Approach for Part 1
## Each row of text has adjacent rows which may contain symbols that make
## numbers on the current row a valid part number.
## For a given row, we can get a list of all the numbers and their locations.
## We can also combine the valid locations on a row where a part number might be
## according to the symbols in the adjacent rows. For example:
## prev_row -> .....*....#....
## curr_row -> ..@...........+
## next_row -> .......&.......
## Produces a valid location mapping for the current row:
## curr_row -> .VVVVVVVVVVV.VV
## Where 'V' is a valid location for a number.
## We can use set theory to check if a valid location mapping (partNumberLocations)
## overlaps with a particular number's location.
## If so, we add the number to our running sum.
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
    '''
    Returns the index for any * symbols on a given row of text.
    '''
    symbols = "*"
    return [ index for index, ltr in enumerate(row) if ltr in symbols ]

## Approach for part 2.
## For part 2, we only have to care about '*' gears.
## So we need to make the gears our focus. So this time, instead of 
## looping over the number locations, we will loop over the gears
## first. Then, for any numbers in a row that a gear might affect,
## we check again with set theory for an overlap with the gear.
##
## The real trick to this puzzle is understanding the scope of each 
## symbol, which can only affect its direct neighbors.

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
