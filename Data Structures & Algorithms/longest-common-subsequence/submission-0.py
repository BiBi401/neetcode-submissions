class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        t1,t2=text1,text2
        if len(t1)<len(t2):
            t1,t2=t2,t1

        prev=[0]*(len(t1)+1)
        curr=[0]*(len(t2)+1)

        for i in range(len(t1)-1,-1,-1):
            for j in range(len(t2)-1,-1,-1):
                if t1[i]==t2[j]:
                    curr[j]=1+prev[j+1]
                else:
                    curr[j]=max(prev[j],curr[j+1])
            prev,curr=curr,prev
        return prev[0]
        