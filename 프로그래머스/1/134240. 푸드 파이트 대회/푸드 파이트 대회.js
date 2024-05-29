function solution(food) {
    const foods = []
    for(let i=1; i<food.length; i++){
        let cnt = parseInt(food[i] / 2) // 한 사람이 먹을 양
        if(cnt) foods.push(String(i).repeat(cnt))
    }
    let answer = foods.join('') + '0' + foods.reverse().join('')
    return answer;
}