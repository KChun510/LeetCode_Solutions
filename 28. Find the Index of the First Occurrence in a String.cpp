#include <cstring>
class Solution {
public:
    int strStr(string haystack, string needle) {
        int hay_index = 0;
        int needle_index = 0;
        int save = 0;

        while(hay_index <= haystack.length() - 1){
            if(haystack[hay_index] == needle[needle_index]){
                int needle_len = needle.length();
                save = hay_index;
                while(hay_index <= haystack.length()){
                    if(haystack[hay_index] == needle[needle_index]){
                        hay_index += 1;
                        needle_index += 1;
                        needle_len -= 1;
                        if(needle_len == 0){
                            return save;
                        }
                    }
                    else if(haystack[hay_index] != needle[needle_index]){
                        needle_index = 0;
                        hay_index = save + 1;
                        break;
                    }
                }
            }
            else{
                hay_index++;
            }
        }
        return -1;
    }
};
