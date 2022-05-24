/* 
#문제설명
 마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때,
 완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.

#제한사항
 마라톤 경기에 참여한 선수의 수는 1명 이상 100,000명 이하입니다.
 completion의 길이는 participant의 길이보다 1 작습니다. 
 참가자의 이름은 1개 이상 20개 이하의 알파벳 소문자로 이루어져 있습니다.
 참가자 중에는 동명이인이 있을 수 있습니다.
*/


function solution(participant, completion) {

    for (var i = participant.length; i >= 0; i--) {
        for (var j = completion.length; j >= 0; j--) {
            if (participant[i] == completion[j]) {
                participant.splice(i, 1);
                completion.splice(j, 1);
                break;
            }
        }
    }
    return participant[0];
}


// 실패코드 => 시간초과 (n^2 이상 돌면 비효율.)
function solution(participant, completion) {

    let answer = participant.filter(e => {
        if (completion.includes(e)) {
            completion.splice(completion.indexOf(e), 1)
            return false
        }
        return true
    })
    return answer[0];
}