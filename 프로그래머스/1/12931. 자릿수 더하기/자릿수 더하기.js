function solution(n)
{
    var answer = 0;
    str = String(n)
    for(let i=0; i<str.length; i++){
        answer+=Number(str[i])
    }

    return answer;
}