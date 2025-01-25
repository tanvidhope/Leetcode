class TrieNode:
    def __init__(self, val):
        self.val = val
        self.children = defaultdict(set)
        self.isWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode('*')

    def addWord(self, word: str) -> None:
        temp = self.root
        for letter in word:
            if letter not in temp.children:
                temp.children[letter] = TrieNode(letter)
            temp = temp.children[letter]
        temp.isWord = True

    def search(self, word: str) -> bool:

        def rsearch(word, root):
            if not word:
                return root.isWord
            if word[0] != '.' :
                if word[0] not in root.children:
                    return False
                return rsearch(word[1:], root.children[word[0]])
            for letter in root.children:
                if rsearch(word[1:], root.children[letter]):
                    return True
            return False

        temp = self.root
        return rsearch(word, temp)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)