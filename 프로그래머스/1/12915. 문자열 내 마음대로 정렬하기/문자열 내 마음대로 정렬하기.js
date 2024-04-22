function solution(strings, n) {
    return strings.sort((s1, s2) => s1[n] === s2[n] ? s1.localeCompare(s2) : s1[n].localeCompare(s2[n]));
}
// 같으면 s1 vs s2
// 다르면 s1[n] vs s2[n]