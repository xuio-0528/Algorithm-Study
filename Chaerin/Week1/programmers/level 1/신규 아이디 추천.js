/*
#문제설명
 신규 유저가 입력한 아이디를 나타내는 new_id가 매개변수로 주어질 때, 
 네오가 설계한 7단계의 처리 과정을 거친 후의 추천 아이디를 return 하도록 solution 함수를 완성해 주세요.

- 7단계 처리과정 -
 1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
 2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
 3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
 4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
 5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
 6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
     만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
 7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.


#제한사항
 new_id는 길이 1 이상 1,000 이하인 문자열입니다.
 new_id는 알파벳 대문자, 알파벳 소문자, 숫자, 특수문자로 구성되어 있습니다.
 new_id에 나타날 수 있는 특수문자는 -_.~!@#$%^&*()=+[{]}:?,<>/ 로 한정됩니다.
*/

function solution(new_id) {

    //1단계
    new_id = new_id.toLowerCase();

    //2단계
    var nouse = ['~','!','@','#','$','%','^','&','*','(',')','=','+','[','{',']','}',':','?',',','<','>','/'];
    var newid0 = [...new_id]; //배열이 편해서...
    var newid1 = newid0.filter(i => !nouse.includes(i));//특수문자제거
    newid1.push("z");

    //3단계
    var newid2 = [];
    for(let i = 0; i < newid1.length; i++) {
        if(newid1[i] === "." && newid1[i+1] === ".") {
            continue;
        } else{ newid2.push(newid1[i])}
    };

    newid2.pop();


    //4단계
    if(newid2[0] === ".") {
        newid2.shift();
    };
    if(newid2[newid2.length-1] === ".") {
        newid2.pop();
    };

    //5단계
    if(newid2.length === 0) {
        newid2.push("a");
    }

    //6단계
    if(newid2.length > 15) {
        newid2.splice(15,1000)
    };

    if(newid2[newid2.length-1] === ".") {
        newid2.pop();
    };

    //7단계
    if(newid2.length === 1 && newid2[0] === "a") {
        newid2.push("a");
        newid2.push("a");
    };

    if(newid2.length === 1) {
        newid2.push(newid2[0]);
        newid2.push(newid2[1]);
    }


    if(newid2.length === 2) {
        newid2.push(newid2[1]);
    }

    var answer = newid2.join('');

    return answer;
}