def solution(board, h, w):
    answer = 0
    n = len(board)
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    
    for i in range(4):
        if 0<=h+dx[i]<n and 0<=w+dy[i]<n and board[h+dx[i]][w+dy[i]] == board[h][w]:
            answer+=1
    
    return answer