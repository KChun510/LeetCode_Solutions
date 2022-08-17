class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        Dcode = {"a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", "g": "--.", "h": "....", "i": "..",
             "j": ".---", "k": "-.-", "l": ".-..", "m": "--", "n": "-.", "o": "---", "p": ".--.", "q": "--.-",
             "r": ".-.", "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--", "x": "-..-", "y": "-.--", "z": "--.."}
        code = []
        save = []
        for word in words:
            for let in word:
                save += Dcode[let]
        
            a = ''.join(save)    
            if a not in code:
                code += [a]
                del save[:]
            else:
                del save[:]
                
        return len(code)
