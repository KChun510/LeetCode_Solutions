function topKFrequent(nums: number[], k: number): number[] {
    let bucket: number[][] = [];
    let freq_rec: Record<number, number> = {};
    let ret_arr: number[] = [];

    // Init bucket
    for (let i = 0; i < nums.length + 1; i++) {
        bucket.push([]);
    }
    
    // Init freq map
    for (const num of nums) {
        freq_rec[num] = freq_rec[num] === undefined ? 1 : freq_rec[num] + 1;
    }

    // Fill bucket
    Object.keys(freq_rec).forEach((val) => {
        bucket[freq_rec[val]].push(Number(val));
    });

    for (let i = nums.length; i >= 0 && ret_arr.length < k; i--) {
        while (bucket[i].length > 0 && ret_arr.length < k) {
            ret_arr.push(bucket[i].pop());
        }
    }

    return ret_arr;
}


