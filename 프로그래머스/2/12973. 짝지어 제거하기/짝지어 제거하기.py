def solution(s):
    st = []
    
    for x in s:
        if not st or st[-1] != x:
            st.append(x)
        else:
            st.pop()
    
    return int(not st)