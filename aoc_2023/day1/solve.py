# AOC Day 1 Puzzles 1 and 2
def getDigits1(token):
    firstDigit = None
    lastDigit = None
    for i in token:
        if i.isdigit():
            if firstDigit is None:
                firstDigit = int(i)
            lastDigit = int(i)
    return firstDigit * 10 + lastDigit

stringToNum = {
    'one':      1,
    'two':      2,
    'three':    3,
    'four':     4,
    'five':     5,
    'six':      6,
    'seven':    7,
    'eight':    8,
    'nine':     9
}

def getDigits2(token):
    firstDigit = None
    firstDigitLocation = None
    lastDigit = None
    lastDigitLocation = None
    for i in range(len(token)):
        if token[i].isdigit():
            if firstDigit is None:
                firstDigit = int(token[i])
                firstDigitLocation = i
            lastDigit = int(token[i])
            lastDigitLocation = i
    for stringNum in stringToNum.keys():
        if stringNum in token:
            location = token.find(stringNum)
            if not firstDigit or (location < firstDigitLocation):
                firstDigitLocation = location
                firstDigit = stringToNum[stringNum]
            location = token.rfind(stringNum)
            if not lastDigit or (location > lastDigitLocation):
                lastDigitLocation = location
                lastDigit = stringToNum[stringNum]
    return firstDigit * 10 + lastDigit
            
inputFile = "input.txt"
tokens = open(inputFile,"r").readlines()
sum1 = 0
sum2 = 0
sum3 = 0
for token in tokens:
    sum1 += getDigits1(token.strip())
    sum2 += getDigits2(token.strip())

print(f"Solution 1: {sum1}")
print(f"Solution 2: {sum2}")
