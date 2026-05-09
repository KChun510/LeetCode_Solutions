function twoSum(nums: number[], target: number): number[] {
    let ind_val : Record<number, number> = {};

    for(let i = 0; i < nums.length; i++){
        const curr_num = nums[i];
        const rem = target - curr_num;
        if (ind_val[rem] === undefined && ind_val[curr_num] === undefined) ind_val[curr_num] = i; 
        else if (ind_val[rem] === undefined) continue;
        else if(ind_val[rem] !== undefined) return [i, ind_val[rem]];
    }
    return [0, 0];
};


