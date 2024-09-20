function solution(new_id) {
    // 1단계
    const first = new_id.toLowerCase()
    
    // 2단계
    const second = first.replace(/[^a-z0-9\-_\.]/g, "");
   
    // 3단계
    const third = second.replace(/\.{2,}/g, ".");
    
    // 4단계
    const fourth = third.replace(/^\.|\.$/g, "");
    
    // 5단계
    const fifth = fourth.length === 0 ? "a" : fourth
    
    // 6단계
    const sixth = fifth.length >= 16 ? fifth.slice(0, 15).replace(/\.+$/g, "") : fifth;
    
    // 7번째
    const seventh = sixth.length <= 2 ? sixth.padEnd(3, sixth[sixth.length-1]) : sixth
    
    return seventh;
}