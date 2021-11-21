Table = [["ABCE"], ["SFCS"], ["ADEE"]]


def isExistChars(rIdx, cIdx, word):
    if word == '': return True

    isExist = False
    if rIdx - 1 > 0 and word[0] == Table[rIdx - 1][0][cIdx]:
        isExist = isExistChars(rIdx - 1, cIdx, word[1:])
    if rIdx + 1 < len(Table) and word[0] == Table[rIdx + 1][0][cIdx] and not isExist:
        isExist = isExistChars(rIdx + 1, cIdx, word[1:])
    if cIdx - 1 > 0 and word[0] == Table[rIdx][0][cIdx - 1] and not isExist:
        isExist = isExistChars(rIdx, cIdx - 1, word[1:])
    if cIdx + 1 < len(Table[0][0]) and word[0] == Table[rIdx][0][cIdx + 1] and not isExist:
        isExist = isExistChars(rIdx, cIdx + 1, word[1:])
    return isExist


def isCreatable(word):
    if word == '': return False

    rIdx = 0
    isFind = False
    for row in Table:
        cIdx = 0
        for char in row[0]:
            if char == word[0]:
                isFind = isExistChars(rIdx, cIdx, word[1:])
            if isFind: break
            cIdx += 1
        if isFind: break
        rIdx += 1

    return isFind


print('ABCCED', isCreatable('ABCCED'))
print('SEE', isCreatable('SEE'))
print('ABCB', isCreatable('ABCD'))