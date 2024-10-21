class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merge_str = ""
        if len(word1) >= len(word2):
            for i in range(len(word2)):
                merge_str += word1[i]
                merge_str += word2[i]
            merge_str += word1[len(word2) : ]

        elif len(word2) >= len(word1):
            for i in range(len(word1)):
                merge_str += word1[i]
                merge_str += word2[i]
            merge_str += word2[len(word1) : ]


        return merge_str

          
        
