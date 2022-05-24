/*
문제 설명
양의 정수 x가 하샤드 수이려면 x의 자릿수의 합으로 x가 나누어져야 합니다. 
자연수 x를 입력받아 x가 하샤드 수인지 아닌지 검사하는 함수, solution을 완성해주세요.

제한 조건
x는 1 이상, 10000 이하인 정수입니다.

// do while이랑 while 차이?
*/
function solution(x) {
    const origin = x
    let k = 0;
    while (x > 0) {
        k += (x % 10);
        x = Math.floor(x / 10);
    }
    return origin % k == 0;
}