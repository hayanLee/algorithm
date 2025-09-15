def solution(s, skip, index):
    answer = []
    all_alpha = 'abcdefghijklmnopqrstuvwxyz'
    filtered_alpha = ''.join([ch for ch in all_alpha if ch not in skip]) 
    
    alpha_dict = {}
    
    for idx, value in enumerate(filtered_alpha):
        alpha_dict[value]=idx
        
    for ch in s:
        new_idx = (alpha_dict[ch] + index) % len(alpha_dict)
        answer.append(filtered_alpha[new_idx])
    
    return ''.join(answer)