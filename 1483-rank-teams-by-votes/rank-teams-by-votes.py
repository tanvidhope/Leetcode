class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        countMap = {}
        for vote in votes:
            for rank,candidate in enumerate(vote):
                if candidate not in countMap:
                    countMap[candidate] = [0]*len(vote) # votes for each rank for the candidate
                countMap[candidate][rank]+=1
        votedNames = sorted(countMap.keys())
        return "".join(sorted(votedNames, key = lambda x:countMap[x], reverse = True))
