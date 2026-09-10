class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair=[(p,s) for p,s in zip(position,speed)]
        pair.sort(reverse=True)
        stck=[]
        for p,s in pair:
            stck.append((target-p)/s)
            if len(stck)>=2 and stck[-1]<=stck[-2]:
                stck.pop()
        return len(stck)        