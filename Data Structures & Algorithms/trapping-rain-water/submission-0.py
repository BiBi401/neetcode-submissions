class Solution:
    def trap(self, height: List[int]) -> int:
        
        if not height:
            return 0
        h=height
        l,r=0,len(h)-1
        lm,rm=h[l],h[r]
        res=0
        while l<r:
            if lm<rm:
                l+=1
                lm=max(lm,h[l])
                res+=lm-h[l]
            else:
                r-=1
                rm=max(rm,h[r])
                res+=rm-h[r]
        return res