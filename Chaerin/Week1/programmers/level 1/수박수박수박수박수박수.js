/*
#문제 설명
 길이가 n이고, "수박수박수박수...."와 같은 패턴을 유지하는 문자열을 리턴하는 함수, solution을 완성하세요.
 예를들어 n이 4이면 "수박수박"을 리턴하고 3이라면 "수박수"를 리턴하면 됩니다.

#제한 조건
 n은 길이 10,000이하인 자연수입니다.
*/

function solution(n) {
    var answer = '';
    let i = 1
    while (i <= n) {
        if (i % 2 == 0) {
            answer += "박"
        } else {
            answer += "수"
        }
        i++
    }
    return answer;
}

// 다른풀이
return '수박'.repeat(n/2) + (n%2 === 1 ? '수' : '');

return "수박".repeat(n).slice(0,n);

for(var i=1; i<=n; i++) {
    i % 2 === 1 ? result += "수" : result += "박"
  }
  