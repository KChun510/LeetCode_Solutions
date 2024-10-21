class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        word1_dic = {}
        word2_dic = {}

        for i in range(len(word1)):
            if word1[i] not in word1_dic:
                word1_dic[word1[i]] = 1
            else:
                word1_dic[word1[i]] += 1

        for i in range(len(word2)):
            if word2[i] not in word2_dic: 
                word2_dic[word2[i]] = 1
            else:
                word2_dic[word2[i]] += 1

        freq1_arr = []
        freq2_arr = []
        for key in word1_dic:
            if key not in word2_dic:
                return False
            else:
                freq1_arr.append(word1_dic[key])
                freq2_arr.append(word2_dic[key])
        
        freq1_arr.sort() 
        freq2_arr.sort()
        if freq1_arr != freq2_arr:
            return False
        
        return True
                
        
        
