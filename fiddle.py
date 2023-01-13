class Solution:
    def isPossible(self, nums) -> bool:
        i = 1
        prev = nums[0]
        taken_count = 1
        curr_len = 1
        first_not_taken = None
        
        while i < len(nums):
            if curr_len == 3:
                prev=nums[i]
                curr_len =1
                i+=1
                continue
            if nums[i] == prev:
                if first_not_taken is None:
                    first_not_taken= i
                i+=1
                continue
            elif nums[i] - prev == 1:
                prev = nums[i]
                taken_count+=1
                curr_len+=1
                i+=1
            else:
                if curr_len < 3:
                    return False
                elif curr_len == len(nums):
                    return True
                i = i if first_not_taken is None else first_not_taken
                prev=nums[i]
                curr_len =1
                i+=1
        
        return taken_count == len(nums)
    
sol = Solution()
print(sol.isPossible([1,2,3,3,4,5]))