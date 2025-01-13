class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        # tree problem
        countMap = defaultdict(int)
        for cpdomain in cpdomains:
            count, domain= cpdomain.split()
            arr = domain.split(".")
            for element in arr:
                countMap[domain]+=int(count)
                if '.' in domain:
                    domain = domain[domain.index('.')+1:]
        ans = []
        for domain in countMap:
            ans.append(str(countMap[domain])+" "+domain)
        return ans


        
