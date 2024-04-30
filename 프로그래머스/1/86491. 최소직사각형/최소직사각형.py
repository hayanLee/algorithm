def solution(sizes):
    answer = 0
    maxs = []
    mins = []
    for card in sizes:
        maxs.append(max(card))
        mins.append(min(card))
    return max(maxs) * max(mins)