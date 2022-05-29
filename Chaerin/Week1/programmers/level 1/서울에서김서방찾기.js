/*
 # 문제설명
  String형 배열 seoul의 element중 Kim의 위치 x를 찾아, 김서방은 x에 있다는 String을 반환하는 함수, solution을 완성하세요.
  seoul에 Kim은 오직 한 번만 나타나며 잘못된 값이 입력되는 경우는 없습니다.

 # 제한사항
  seoul은 길이 1 이상, 1000 이하인 배열입니다.
  seoul의 원소는 길이 1 이상, 20 이하인 문자열입니다.
  Kim은 반드시 seoul 안에 포함되어 있습니다.
*/


// 내 코드
function solution(seoul) {
    var answer = '';
    for(var i=0; i<seoul.length; i++) {
        if(seoul[i] ==="Kim") {
            answer="김서방은 "+i+"에 있다"
        }
    }
    return answer;
} // 런타임 오류,  왜? => 바보는 상수의 뜻을 모른다... var, const 생각하면서 쓰기


// 더 나은 코드
`김서방은 ${seoul.findIndex((e)=>(e))}` // 한줄코드 찾아보기..
