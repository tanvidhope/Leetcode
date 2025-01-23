class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = defaultdict(list)
        for s in strs:
            tmp = s
            hmap[''.join(sorted(s))].append(tmp)
        ans = []
        for key in hmap:
            ans.append(hmap[key])
        return ans