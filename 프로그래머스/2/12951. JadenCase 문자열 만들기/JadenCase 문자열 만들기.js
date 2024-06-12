function solution(s) {
    const answer = ' ';
    let result = s.split(' ')
                .map((item) => item.charAt(0).toUpperCase() + item.slice(1).toLowerCase());
    return result.join(' ');
}