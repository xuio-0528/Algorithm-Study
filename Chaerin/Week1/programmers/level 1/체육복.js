/*
# 문제 설명
 점심시간에 도둑이 들어, 일부 학생이 체육복을 도난당했습니다. 다행히 여벌 체육복이 있는 학생이 이들에게 체육복을 빌려주려 합니다. 
 학생들의 번호는 체격 순으로 매겨져 있어, 바로 앞번호의 학생이나 바로 뒷번호의 학생에게만 체육복을 빌려줄 수 있습니다. 
 체육복이 없으면 수업을 들을 수 없기 때문에 체육복을 적절히 빌려 최대한 많은 학생이 체육수업을 들어야 합니다.(탐욕법 - 한번에 쭉 훑어보면서 가장 최선의 방법 선택)

 전체 학생의 수 n, 체육복을 도난당한 학생들의 번호가 담긴 배열 lost, 여벌의 체육복을 가져온 학생들의 번호가 담긴 배열 reserve가 매개변수로 주어질 때, 
 체육수업을 들을 수 있는 학생의 최댓값을 return 하도록 solution 함수를 작성해주세요.

# 제한사항
 전체 학생의 수는 2명 이상 30명 이하입니다. 
 체육복을 도난당한 학생의 수는 1명 이상 n명 이하이고 중복되는 번호는 없습니다. 
 여벌의 체육복을 가져온 학생의 수는 1명 이상 n명 이하이고 중복되는 번호는 없습니다.
 여벌 체육복이 있는 학생만 다른 학생에게 체육복을 빌려줄 수 있습니다.
 여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있습니다. 이때 이 학생은 체육복을 하나만 도난당했다고 가정하며, 남은 체육복이 하나이기에 다른 학생에게는 체육복을 빌려줄 수 없습니다.
*/

// 힌트
// 1로 채운 배열에 lost -1, reserve +1
// 앞에서부터 진행

// lost, reserve 중복 처리 필요

function solution(n, lost, reserve) {
    var answer = 0;
    let arr = new Array(n).fill(1).map((st, i) => {
        if (lost.includes(i + 1)) {
            st -= 1
        }
        if (reserve.includes(i + 1)) {
            st += 1
        }
        return st
    })
    arr.forEach((st, i) => {
        if (st === 0) {
            if (arr[i - 1] === 2) {
                arr[i] = 1
            }
            else if (arr[i + 1] === 2) {
                arr[i + 1] = 1
                arr[i] = 1
            }
        }
    })
    answer = arr.filter(e => e).length
    return answer;
}


// 질문
function solution() {
        var answer = 0;
        let arr = new Array(n).fill(1).map((st, i) => {
            if (lost.includes(i + 1)) {
                st -= 1
            }
            if (reserve.includes(i + 1)) {
                st += 1
            }
            return st
        })
        answer = arr.map((st, i) => { // 세번째인자로 원래배열 들어갈수있음
            if (st === 0) {
                if (arr[i - 1] === 2) {
                    return 1
                }
                else if (arr[i + 1] === 2) {
                    arr[i + 1] = 1
                    return 1
                }
            }
            return st
        }).filter(e => e).length
        return answer;
    }