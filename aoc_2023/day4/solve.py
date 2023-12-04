## AOC 2023 Day 4 Puzzles 1 and 2

example = \
"""Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""

#cards = example.split('\n')
cards = open("input.txt","r").readlines()

def getWinningSet(card):
    winningNumbers = card.split(':')[1].split('|')[0].split(' ')
    return set([ int(i) for i in winningNumbers if i != ''])

def getCardNumbers(card):
    cardNumbers = card.split(':')[1].split('|')[1].split(' ')
    return set([ int(i) for i in cardNumbers if i != ''])

sum = 0
for card in cards:
    winningSet = getWinningSet(card)
    cardSet = getCardNumbers(card)
    commonSet = winningSet & cardSet
    if len(commonSet) > 0:
        pointValue = 2 ** (len(commonSet) - 1)
        sum += pointValue

print(f"Solution 1: {sum}")
