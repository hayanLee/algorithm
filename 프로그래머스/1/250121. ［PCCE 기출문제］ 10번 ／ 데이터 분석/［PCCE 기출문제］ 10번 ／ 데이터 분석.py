def solution(data, ext, val_ext, sort_by): #뽑아낼 기준 문자열, 기준값, 정렬할 기준 문자열
    dict = {
        'code' : 0,
        'date': 1,
        'maximum': 2,
        'remain': 3
    }
    
    filtered = [data[i] for i in range(len(data)) if data[i][dict.get(ext)] < val_ext]
    filtered.sort(key = lambda x : x[dict[sort_by]])    
        
    return filtered