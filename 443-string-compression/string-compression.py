class Solution:
    def compress(self, chars: List[str]) -> int:
        i, j= 0, 0
        charCount = 0
        currChar = chars[0]
        while i<=len(chars):
            if i<len(chars) and chars[i] == currChar:
                charCount+=1
            else:
                chars[j] = currChar
                j+=1
                if charCount!=1:
                    lst = list(str(charCount))
                    for l in lst:
                        chars[j] = l
                        j+=1
                currChar = chars[i] if i<len(chars) else ""
                charCount = 1
            i+=1
        return j
