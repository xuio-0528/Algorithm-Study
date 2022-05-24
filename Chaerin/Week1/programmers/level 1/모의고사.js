/*
#문제설명
 1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때,  
 가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성해주세요.

-찍는방식-
 1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
 2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
 3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...

#제한 조건
 시험은 최대 10,000 문제로 구성되어있습니다. 
 문제의 정답은 1, 2, 3, 4, 5중 하나입니다.
 가장 높은 점수를 받은 사람이 여럿일 경우, return하는 값을 오름차순 정렬해주세요.
*/

function solution(answers) {
    var answer = [];
    const a = [1, 2, 3, 4, 5]
    const b = [2, 1, 2, 3, 2, 4, 2, 5]
    const c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    let ca = answers.filter((el, i)=>el===a[i%5]).length  // {}없으면 그 값이 반환. filter는 반환이 필요 ,{}=함수본문, ()=값을묶음
    let cb = answers.filter((el, i)=>el===b[i%8]).length
    let cc = answers.filter((el, i)=>el===c[i%10]).length
    const count = [ca,cb,cc]
    const max = Math.max(...count)
    count.forEach((el,i)=>{
        if(el===max){
            answer.push(i+1)
        }
    })
        
    return answer;
}



// 다른 방식
function solution(answers) {
    var answer = [];
    const a = [1, 2, 3, 4, 5]
    const b = [2, 1, 2, 3, 2, 4, 2, 5]
    const c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    let ca = 0
    let cb = 0
    let cc = 0
    
    answers.forEach((el, index)=>{
        if(el === a[index%5]) {
            ca += 1
        }
        if(el === b[index%8]) {
            cb += 1
        }
        if(el === c[index%10]) {
            cc += 1
        }
    })  // 시간복잡도 (자료구조, 알고리즘)
    const count = [ca,cb,cc]
    const max = Math.max(...count)
    count.forEach((el,i)=>{
        if(el===max){
        answer.push(i+1)
        }
    })
    
    return answer;
}