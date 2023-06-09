//Sliding window question.
//Two pointers that start at 0, start & end.
//Increment end/push_back s[end] to end of 'save' vector.
//If dupe found erase from 'save'
//Max length gotten from end - start

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        vector<char> save;
        int start = 0;
        int end = 0;
        int maxLength = 0; 

        while (end < s.size()) {
        if (!count(save.begin(), save.end(), s[end])) { //If s[end] not found in 'save'
            save.push_back(s[end]); //Add element to que
            end++; //Increment window right side
            maxLength = max(maxLength, end - start); //Update max length
        } else {
            save.erase(save.begin()); //Erase Dupe
            start++; //Increment window left side
        }
    }

    return maxLength;
}

};  
