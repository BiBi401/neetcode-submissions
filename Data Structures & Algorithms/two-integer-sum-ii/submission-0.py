class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r=0,len(numbers)-1
        n=numbers

        while l<r:
            sum=n[l]+n[r]

            if sum>target:
                r-=1
            elif sum<target:
                l+=1
            else:
                return [l+1,r+1]
        return []