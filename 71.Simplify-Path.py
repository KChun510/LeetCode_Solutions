class Solution:
    def simplifyPath(self, path: str) -> str:
        split_arr = path.split("/")
        split_arr = list(filter(lambda x: x != '', split_arr))
        split_arr = split_arr[::-1]
        res = []
        skip = 0
        
        if (len(split_arr) == 1 and split_arr[0] == ".." ) or (len(path) == 1 and path[0] == "/" ):
            return "/"

        for dir in split_arr:
            if dir == "..":
                skip += 1
            elif dir == ".":
                continue 
            elif skip != 0:
                skip -= 1
            elif dir != ".":
                res.append(dir)

        if len(res) == 0 and path[0] == "/":
            return "/"


        res = res[::-1]
        res = ["/" + dir for dir in res]
        return ''.join(res)
       
"""
General Idea: 
Read our directory string backwards. Doing this greatly simplifies the logic, eliminates the need to keep track of skips/backtrack when we see a '..' in our string. 

Also split the string up into an array by using the "/". Making the reading of each dir whole rather than letter by letter.

Again start from the back, when we see a dir name like "desktop" "home" "downloads" append to res.
If we see a skip "..", then we up our skip count. And don't append dir's until skip = 0 again.

The two other if statments account for side cases. 

Time O(n): Split, filter, reverse == (n + n + n). Looping through split Arr == (n). Reverse and append "/" == (n + n)
So O(n * 6) simplifys to O(n)

Beats 70-80% in speed depending on how leet code is feelig hehe.

"""
