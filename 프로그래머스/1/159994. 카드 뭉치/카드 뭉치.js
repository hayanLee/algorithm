function solution(cards1, cards2, goal) {
   for(const ch of goal) {
       if(cards1[0] == ch) cards1.shift();
       else if(cards2[0] == ch) cards2.shift();
       else return "No"
    }
    return "Yes"

}