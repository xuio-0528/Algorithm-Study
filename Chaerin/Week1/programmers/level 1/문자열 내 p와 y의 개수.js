/*
#문제설명
 대문자와 소문자가 섞여있는 문자열 s가 주어집니다. 
 s에 'p'의 개수와 'y'의 개수를 비교해 같으면 True, 다르면 False를 return 하는 solution를 완성하세요.

#제한사항
 문자열 s의 길이 : 50 이하의 자연수
 문자열 s는 알파벳으로만 이루어져 있습니다.
*/

function solution(s) {
    var answer = true;
    s = [...s.toLowerCase()]
    let s1 = s.filter((val) => (val === 'p'))
    let s2 = s.filter((val) => (val === "y"))
    answer = s1.length === s2.length

    return answer;
}


// 한번만 돌려서 해결.. 연산처리횟수도 고려하면서 효율적으로

