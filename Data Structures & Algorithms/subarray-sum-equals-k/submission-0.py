class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt=0
        prefixSum=0
        seen={0:1}
        for num in nums:
            prefixSum+=num
            cnt+=seen.get(prefixSum-k,0)
            seen[prefixSum]=seen.get(prefixSum,0)+1
        return cnt