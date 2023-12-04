## AOC Day 2 Puzzle 1

import re

max_red = 12
max_green = 13
max_blue = 14
regex_id = re.compile("([0-9]+):")
regex_blue = re.compile("([0-9]+)\sblue")
regex_red = re.compile("([0-9]+)\sred")
regex_green = re.compile("([0-9]+)\sgreen")

def parse_game1(game):
    id = int(regex_id.findall(game)[0])
    blues = max( [int(x) for x in regex_blue.findall(game)]  + [0] )
    reds =  max( [int(x) for x in regex_red.findall(game)]  + [0] )
    greens =  max( [int(x) for x in regex_green.findall(game)]  + [0] )
    if blues > max_blue:
        return 0
    if reds > max_red:
        return 0
    if greens > max_green:
        return 0
    return id

def parse_game2(game):
    id = int(regex_id.findall(game)[0])
    blues = max( [int(x) for x in regex_blue.findall(game)]  + [0] )
    reds =  max( [int(x) for x in regex_red.findall(game)]  + [0] )
    greens =  max( [int(x) for x in regex_green.findall(game)]  + [0] )
    power = reds * blues * greens
    return power

games = open('input.txt','r').readlines()

sum = 0
for game in games:
    sum += parse_game2(game)
    
print(sum)
