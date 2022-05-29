/*
#문제설명
 배열 arr의 각 원소는 숫자 0부터 9까지로 이루어져 있습니다. 
 배열 arr에서 연속적으로 나타나는 숫자는 제거하고 남은 수들을 return 하는 solution 함수를 완성해 주세요

#제한사항
 배열 arr의 크기 : 1,000,000 이하의 자연수
 배열 arr의 원소의 크기 : 0보다 크거나 같고 9보다 작거나 같은 정수

*/

function solution(arr) {
    var answer = [];
    answer.push(arr[0])
    for (let i = 0; i < arr.length - 1; i++) {
        if (arr[i] !== arr[i + 1]) {
            answer.push(arr[i + 1])
        }
    }
    return answer;
}


// 다른코드
answer = arr.filter((val, i) => (val !== arr[i + 1]))

// new set