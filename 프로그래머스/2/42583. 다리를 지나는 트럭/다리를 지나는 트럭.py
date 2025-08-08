# 다 건너기 위한 최소 시간
# 올라갈 때, 내려갈 때 각각 1초

# 조건
# 1. len(dq) <= bright_length and full_weight <= bright_length (+시간, +무게)
# 2. 1 조건이 안되면 다리에서 내려와야 가능 (+시간, -무게)

from collections import deque
def solution(bridge_length, weight, truck_weights): # 다리 길이 = 올라갈 수 있는 트럭 개수, 다리에 올라갈 수 있는 총 무게, 트럭 무게
    time = 0 # 걸린 시간 
    total_weight = 0 # 다리에 올라간 트럭 총 무게
    on_the_bridge = deque([0] * bridge_length) # 트럭 위 상황
    dq = deque(truck_weights) # 올라가지 않은 트럭들
        
    while dq or total_weight>0: # 올라가지 않은게 있거나, 다리 위에 트럭이 있을때
        time += 1
        exited_truck = on_the_bridge.popleft()
        total_weight -= exited_truck  # 다리에서 빠진 트럭 무게 빼기
        
        if dq:
            if total_weight + dq[0] <= weight: # 새로운 트럭 올라가기 
                truck = dq.popleft()
                on_the_bridge.append(truck)
                total_weight+=truck
            else: # 빈 공간 올리기
                on_the_bridge.append(0) 
        
        
    return time