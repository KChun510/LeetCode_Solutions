class Solution:
    def compress(self, chars: List[str]) -> int:
        def splitStr(number: str):
            arr = []
            for c in str(number):
                arr += [c]

            return arr

        count = 1
        currC = chars[0]
        i = 1
        lenC = len(chars) 

        if len(chars) == 1:
            return len(chars)
            

        while i < lenC:
            if chars[i] != currC:
                currC = chars[i]
                if count > 1:
                    right = chars[i: lenC + 1]
                    chars[i - count + 1:] = splitStr(count) + right
                    # Back Track, for the amount of Chars compressed
                    i -= count + 1
                    lenC = len(chars)
                    # Update to account for the len of the count we append
                    i += len(str(count)) + 2
        
                count = 1
                
            elif chars[i] == currC:
                count += 1
            
            i += 1
            
        if i == lenC and count > 1:
            chars[i - count + 1:] = splitStr(count)
            
                

        return len(chars)

"""
- Intuition
Loop through Char array, with a single pointer "i".
Create a count for each repeating Char.
Encounter a diff Char from Curr.
Append Count to (first Occurance) + 1 of Char.
Continue/ Repeat.

- Complexity
Time complexity:
O(n), single loop over our char Array.

- Space complexity:
O(Log(n)), besides the OG declared Var. We also use a var called "right",
that will be of size len(chars) - 'i', going down to 1.

"""
