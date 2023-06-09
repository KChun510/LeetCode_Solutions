/**
 * @param {character[]} letters
 * @param {character} target
 * @return {character}
 */
var nextGreatestLetter = function(letters, target) {
    const dic = {a: 1, b: 2, c: 3,d: 4,e: 5,f: 6,g: 7,h: 8,i: 9,j: 10,k: 11,l: 12,m: 13,n: 14,
                 o: 15,p: 16,q: 17,r: 18,s: 19,t: 20,u: 21,v: 22,w: 23,x: 24,y: 25,z: 26};

    const dic_rever = {1: "a",2: "b",3: "c",4: "d",5: "e",6: "f",7: "g",8: "h",9: "i",10: "j",11: "k",12: "l",13: "m",14: 
                       "n",15: "o",16: "p",17: "q",18: "r",19: "s",20: "t",21: "u",22: "v",23: "w",24: "x",25: "y",26: "z"};

    if(target == "z"){
        return letters[0];
    }

    const target_val = dic[target] //Aquire numeric value for target letter
    const len = letters.length;
    for(let i = 0; i < len; i++){ //Loop through given letters
        var tmp_val = dic[letters[i]]; 
        if(tmp_val > target_val){ //Compare target and letter values
            return dic_rever[tmp_val] //Return first greatest value
        }
    }
    return letters[0] //Not found return first letter
};
