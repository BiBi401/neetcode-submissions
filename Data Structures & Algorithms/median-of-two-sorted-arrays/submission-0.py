class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l1,l2=len(nums1),len(nums2)
        merg=nums1+nums2
        merg.sort()
        total=len(merg)
        if total%2==0:
            return (merg[total//2-1]+merg[total//2])/2.0
        else:
            return merg[total//2]
