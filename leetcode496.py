class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        rtn = []
        for i, v1 in enumerate(nums1):
            for v2 in nums2[nums2.index(v1):]:
                if v2 > v1:
                    rtn.append(v2)
                    break
            if i == len(rtn):
                rtn.append(-1)
        return rtn
