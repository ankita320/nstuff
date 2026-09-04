class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #sort array
        #hash each elements
        #[0]*k
        #for i in range(len(dict)-3): parse through 
        d = {}
        arr = []
        m = 0

        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i]+=1


        buckets = [[] for _ in range(len(nums) + 1)] 

        buckets = [[] for _ in range(len(nums) + 1)]
        for key, val in d.items():
            buckets[val].append(key)
            

        count = len(nums)
        for i in range(len(buckets) - 1, 0, -1):  # Start from highest frequency down to 1
            for num in buckets[i]:
                arr.append(num)
                if len(arr) == k:  # Stop exactly when we have k elements
                    return arr


        
        return arr




        