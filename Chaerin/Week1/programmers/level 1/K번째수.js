/*
# 문제설명
 배열 array의 i번째 숫자부터 j번째 숫자까지 자르고 정렬했을 때, k번째에 있는 수를 구해라.

#제한사항
 array의 길이는 1 이상 100 이하입니다.
 array의 각 원소는 1 이상 100 이하입니다.
 commands의 길이는 1 이상 50 이하입니다.
 commands의 각 원소는 길이가 3입니다.
*/

function solution(array, commands) {
    var answer = [];
    commands.forEach((el,i)=>{
    let sa = array.slice(el[0]-1,el[1]).sort((a,b)=>a-b)
    answer.push(sa[el[2]-1])
    })
    return answer;
}

// 질문
const [sPosition, ePosition, position] = command