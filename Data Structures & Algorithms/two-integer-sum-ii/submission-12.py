class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        idx1=0
        idx2 = len(numbers)-1
        arr = []
        while idx1!=idx2:
            if (numbers[idx1] + numbers[idx2] < target):
                idx1+=1
            elif (numbers[idx1] + numbers[idx2] > target):
                idx2-=1
            elif numbers[idx1] + numbers[idx2] == target:
                arr.append(idx1+1)
                arr.append(idx2+1)
                break
        return arr

        