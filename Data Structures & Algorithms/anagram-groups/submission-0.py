class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)
        for s in strs:
            result=''.join(sorted(s))
            res[result].append(s)
        return list(res.values())