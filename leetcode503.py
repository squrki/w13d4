class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        rtn = []                        # instantiate return list
        for i, v1 in enumerate(nums):   # interate over list
            for v2 in nums[i:]:         # interate over slice of list to end
                if v2 > v1:             # if condition met
                    rtn.append(v2)      # append to return list
                    break               # begin next iteration
            if i == len(rtn):           # if condition not found in slice
                for v2 in nums[:i]:     # interate over slice of list from beginning
                    if v2 > v1:         # if condition met
                        rtn.append(v2)  # append to return list
                        break           # begin next iteration
            if i == len(rtn):           # if condition not met (since return list wasn't appended)
                rtn.append(-1)          # append return list with notifier (-1)
        return rtn
