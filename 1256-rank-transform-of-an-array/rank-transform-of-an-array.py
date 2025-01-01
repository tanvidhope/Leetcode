class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        temp = sorted(arr)
        map = {}
        rank = 1
        for i in range(len(temp)):
            if temp[i] not in map:
                map[temp[i]] = rank
                rank+=1
        ans =[]
        for i in range(len(arr)):
            ans.append(map[arr[i]])
        return ans
            