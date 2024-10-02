function solution(x, n) {
    const arr = Array(n).fill(x);
    return arr.map((num, i) => num*(i+1));
}