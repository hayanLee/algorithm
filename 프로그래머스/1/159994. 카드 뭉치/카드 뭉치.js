function solution(cards1, cards2, goal) {    
    let aIdx = 0;
    let bIdx = 0;
    
    for(const target of goal){
        if(aIdx < cards1.length && cards1[aIdx] === target) aIdx++;
        else if(bIdx < cards2.length && cards2[bIdx] === target) bIdx++;
        else return "No"
    }
    
    return "Yes";
}