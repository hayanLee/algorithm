from collections import deque
dx = [-1,0,1,0]
dy = [0,1,0,-1]

def solution(n, computers):
    answer = 0
    ch = [False*n for _ in range(n)]

    for com in range(n): #컴퓨터 1개 탐색
        if not ch[com]: #방문 안했으면
                dfs(n, computers, ch, com)
                answer+=1
    return answer

def dfs(n,computers, ch, com):
    ch[com] = True #방문처리
    
    for connect in range(n): #해당 컴퓨터에 연결된 컴퓨터
        if connect != com and computers[com][connect]==1 and not ch[connect]: #자신이 아님 and com과 연결됨 and 방문 안함
            dfs(n, computers, ch, connect)
            
