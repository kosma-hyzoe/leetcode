

class Solution:
    def threeSum(self, nums):
        def _third(li, ri):
            return 0 - (nums[li] + nums[ri])

        triplets = []
        visited = []
        nums = sorted(nums)

        li = 0
        ri = len(nums) - 1

        while True:
            third = _third(li, ri)
            if third in nums[li + 1:ri]:
                triplet_rep = f"{nums[li]}{third}{nums[ri]}"
                if triplet_rep not in visited:
                    triplets.append([nums[li], third, nums[ri]])
                    visited.append(triplet_rep)

            li += 1
            if li == ri:
                return triplets

            if nums[li] >= 0:
                ri -= 1
                li = 0
                if nums[ri] <= 0:
                    if nums[ri] == 0 and nums[ri - 2] == 0 \
                            and "000" not in visited:
                        triplets.append([0, 0, 0])
                    return triplets
