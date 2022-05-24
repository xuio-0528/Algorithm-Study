/*
#문제 설명
 자연수 n이 매개변수로 주어집니다. 
 n을 3진법 상에서 앞뒤로 뒤집은 후, 
 이를 다시 10진법으로 표현한 수를 return 하도록 solution 함수를 완성해주세요.

#제한사항
 n은 1 이상 100,000,000 이하인 자연수입니다.

// reserve는 배열을 역순정렬, join('')은 배열을 문자열로 변환
// 3진법은 로직으로 해결하는것도 해보기...
*/

function solution(n) {
    var answer = 0;
    answer = parseInt([...n.toString(3)].reverse().join(''),3);
    return answer;
}