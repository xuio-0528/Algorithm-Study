function solution(numbers) {
    var answer = [];
    const arr = getCombinations(numbers, 2)
    arr.forEach((c, i)=>{
        var sum=c[0]+c[1]
        if(!answer.includes(sum))
        answer.push(sum)
    }) 
    answer.sort(function(a, b) {
  return a - b;
});
    return answer;
}

const getCombinations = function (arr, selectNumber) {
    const results=[];
    if (selectNumber === 1 ) return arr.map((value=>[value]))
    arr.forEach((fixed, i, origin)=>{
        const rest = origin.slice(i +1);
        const combinations = getCombinations(rest, selectNumber - 1);
        const attached = combinations.map((combination)=>[fixed,...combination]);
        results.push(...attached);
    })
    return results;
}