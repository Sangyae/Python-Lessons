def encodeString(stringVal):
    encodeList = []
    prevChar = stringVal[0]
    count = 0
    for char in stringVal:
        if prevChar != stringVal:
            encodeList.append([prevChar, count])
            count = 0
        prevChar = char
        count = count +1
    encodeList.append([prevChar, count])
    return encodeList

    