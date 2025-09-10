def solution(mats, park):
    h = len(park) # 공원 세로
    w = len(park[0]) # 공원 가로
    
    mats.sort(reverse = True) # 내림차순 정렬
    
    for mat in mats:
        for i in range(h-mat+1):
            for j in range(w-mat+1):
                if park[i][j] != '-1': #자리가 없으면 다음으로
                    continue
                can_place_here = True
                for x in range(mat):
                    for y in range(mat):
                        if park[i+x][j+y] != '-1': # 빈칸이 아니면 탈출
                            can_place_here = False
                            break
                    if not can_place_here: # x문 탈출
                        break
                if can_place_here: # x,y 모두 탈출 후 검사
                    return mat
    return -1