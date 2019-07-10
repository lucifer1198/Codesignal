def removeDuplicateCharacters(inputStr):
    charCount = {}
    newInputStr = []
    for i in range(len(inputStr)):
        char = inputStr[i]
        if char in charCount:
            charCount[char] += 1
        else:
            charCount[char] = 0
    for i in range(len(inputStr)):
        if charCount[inputStr[i]] == 0:
            newInputStr.append(inputStr[i])
    return "".join(newInputStr)
