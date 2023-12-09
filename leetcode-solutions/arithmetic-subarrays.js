var checkArithmeticSubarrays = function(nums, l, r) {
    let answer = []; 
    for(let i = 0 ; i < l.length; i++){
        let arithmetic = true;
        let sub1 = nums.slice(l[i],r[i]+1);
        sub1 = sub1.sort((a,b) => a-b);
        let target = sub1[0]-sub1[1];
        for(let i = 1; i < sub1.length ; i++){
            if(sub1[i-1] - sub1[i] === target) 
                continue;
            else{
                arithmetic = false;
                break;
            }
        }
        answer.push(arithmetic);
    }
    return answer;
};