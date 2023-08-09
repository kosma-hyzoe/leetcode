
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = sorted(list(Counter(nums).items()), key=lambda x: x[1])
        return [freqs.pop()[0] for i in range(0, k)]

        product_of_array_except_self
