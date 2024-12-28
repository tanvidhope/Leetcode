class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        # move the largest element to the end at each iteration and shrink the space
        def flip(sublist, k):
            i=0
            while i<k/2:
                sublist[i], sublist[k-i-1]=  sublist[k-i-1], sublist[i]
                i+=1
        
        ans = []
        valueToSort = len(arr)
        while valueToSort > 0:
            index = arr.index(valueToSort)
            if index!= valueToSort-1:
                if index!=0:
                    ans.append(index+1)
                    flip(arr, index+1)
                ans.append(valueToSort)
                flip(arr, valueToSort)
            valueToSort-=1
        return ans