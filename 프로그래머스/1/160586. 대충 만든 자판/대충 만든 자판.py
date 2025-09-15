def solution(keymap, targets):
    answer = []
    alpha_dict = {}
    
    # 최소값만 담은 딕셔너리 생성
    for i in range(len(keymap)):
        s = keymap[i]
        for idx, ch in enumerate(s):
            alpha_dict[ch] = min(alpha_dict.get(ch, idx+1), idx+1)
    
    print(alpha_dict)
    
    for i in range(len(targets)):
        cnt = 0
        for ch in targets[i]:    
            if ch not in alpha_dict:
                cnt = -1
                break
            else:
                cnt += alpha_dict[ch]
        answer.append(cnt)
    return answer