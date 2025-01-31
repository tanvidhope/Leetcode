class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        wordLen = len(words[0])
        word_count = Counter(words)
        indexes = []

        for i in range(wordLen):
            start = i
            window = defaultdict(int)
            words_used = 0

            for j in range(i, len(s) - wordLen + 1, wordLen):
                word = s[j:j + wordLen]

                if word not in word_count:
                    start = j + wordLen
                    window = defaultdict(int)
                    words_used = 0
                    continue

                words_used += 1
                window[word] += 1

                while window[word] > word_count[word]:
                    window[s[start:start + wordLen]] -= 1
                    start += wordLen
                    words_used -= 1

                if words_used == len(words):
                    indexes.append(start)

        return indexes