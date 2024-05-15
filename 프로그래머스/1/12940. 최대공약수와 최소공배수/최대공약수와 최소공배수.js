function gcd(a, b) {
    if(b==0) return a;
    else return gcd(b, a%b)
    
}

function solution(n, m) {
    const a = gcd(n,m)
    const b = (n * m) / a
    return [a, b];
}