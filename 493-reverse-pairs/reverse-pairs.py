class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        # merge sort like solution
        def mergeSort(left, right):
            if left >= right: return 0
            mid = (left + right) // 2
            count = mergeSort(left, mid) + mergeSort(mid + 1, right)

            j = mid + 1
            for i in range(left, mid+1):
                while j <= right and nums[i] > 2 * nums[j]:
                    j += 1
                count += j - mid - 1

            nums[left:right+1] = sorted(nums[left:right+1])
            return count

        return mergeSort(0, len(nums) - 1)