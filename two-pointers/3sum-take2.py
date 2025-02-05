class Solution:
    def threeSum(self, nums):

        def helper(nums):
            pass

        triplets = []
        nums.sort()

        if nums[0] == 0:
            return [0, 0, 0] if nums[:3] == [0, 0, 0] else []

        i = 0
        while nums[i] < 0:
            j = i + 1
            while j < len(nums) and nums[i] + nums[j] <= 0:
                k = -1
                while nums[k] >= 0:
                    if nums[i] + nums[j] + nums[k] == 0:
                        triplets.append([nums[i], nums[j], nums[k]])

                    k -= 1

                j += 1

            i += 1

        return triplets
