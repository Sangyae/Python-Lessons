def decodeString(encodedList):
    decodeStr = ''
    for item in encodedList:
        decodeStr = decodeStr + item[0] * item[1]
        return decodeStr

print(decodeString('abc'))