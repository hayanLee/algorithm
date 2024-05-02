def solution(s):
    answer = []
    cnt = 0 # 시도 횟수
    zerocnt = 0 # 제거한 0의 개수
    
    while s!='1':
        zerocnt += s.count("0") #제거할 0의 개수
        s = s.replace("0",'') #0제거
        
        s = str(bin(len(s))[2:]) #0제거 길이만큼 이진변환
        cnt+=1
    
    return [cnt, zerocnt]
