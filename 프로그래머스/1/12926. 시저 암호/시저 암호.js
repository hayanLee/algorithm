function solution(s, n) {
    let answer = '';
    for (let i = 0; i < s.length; i++) {
        if (s[i] >= 'A' && s[i] <= 'Z') { // 대문자
            answer += String.fromCharCode((s.charCodeAt(i) - 'A'.charCodeAt(0) + n) % 26 + 'A'.charCodeAt(0));
        } else if (s[i] >= 'a' && s[i] <= 'z') { // 소문자
            answer += String.fromCharCode((s.charCodeAt(i) - 'a'.charCodeAt(0) + n) % 26 + 'a'.charCodeAt(0));
        } else { // 알파벳이 아닌 경우
            answer += s[i];
        }
    }
    return answer;
}
