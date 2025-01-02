class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        # find internal patterns of each of the words
        def shiftLetter(letter, shift):
            return chr((ord(letter) - shift) %26 + ord('a'))

        def getHash(string):
            shift = ord(string[0])
            return "".join(shiftLetter(letter, shift) for letter in string)
        hmap =defaultdict(list)
        for string in strings:
            hashKey = getHash(string)
            hmap[hashKey].append(string)
        ans = []
        for key in hmap:
            ans.append(list(hmap[key]))
        return ans