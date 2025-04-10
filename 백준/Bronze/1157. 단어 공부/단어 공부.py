from collections import Counter

str = input()
cnts = Counter(str.upper())
mostCommonCnt = cnts.most_common()[0][1]
mode = [item for item, value in cnts.most_common() if mostCommonCnt == value]
print('?' if len(mode)>1 else mode[0])
