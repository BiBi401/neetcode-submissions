class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r=0,len(heights)-1
        res=0
        h=heights
        while l<r:
            area=min(h[l],h[r])*(r-l)
            res=max(res,area)
            if h[l]<=h[r]:
                l+=1
            else:
                r-=1
        return res