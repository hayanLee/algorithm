def solution(s):
    answer = 0
    st = []
    
    for x in s:
        if not st or st[-1] != x:
            st.append(x)
        else:
            st.pop()
    
    if not st:
        answer = 1
    return answer