function solution(s){
    var answer = true;
    const splitedP = s.toLowerCase().split('p');
    const splitedY = s.toLowerCase().split('y');
    
    return splitedP.length === splitedY.length;
}