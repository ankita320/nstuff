class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        maj = len(nums)//3+1
        d = {}
        fin = []
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i]+=1
        
        for i in d:
            if d[i] >= maj:
                fin.append(i)
        
        return fin

        