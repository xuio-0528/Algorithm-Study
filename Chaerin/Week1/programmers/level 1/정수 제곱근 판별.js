/*
문제 설명
임의의 양의 정수 n에 대해, n이 어떤 양의 정수 x의 제곱인지 아닌지 판단하려 합니다.
n이 양의 정수 x의 제곱이라면 x+1의 제곱을 리턴하고, n이 양의 정수 x의 제곱이 아니라면 -1을 리턴하는 함수를 완성하세요.

제한 사항
n은 1이상, 50000000000000 이하인 양의 정수입니다.

질문
x대신 Math.sqrt(n)으로 쓰면 런타임에러 왜?
*/

function solution(n) {
    let x = Math.sqrt(n)
    var answer = Number.isInteger(x)? (x+1) * (x+1) : -1
    return answer;
}
