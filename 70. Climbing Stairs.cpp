#include <map>
class Solution {
public:

    int climbStairs(int n) {
        map<int, int> map;
        return recursion(n, map );
        
    }

    int recursion(int n, map<int, int> &map){
        if(map.find(n) != map.end()){
            return map[n];
        }
        else if(n <= 1){
            return 1;
        }
        else if(n < 0){
            return 0;
        }
        map[n] = recursion(n - 1, map) + recursion(n - 2, map);
        return map[n];

    };



};
