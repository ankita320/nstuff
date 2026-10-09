class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        days = [0] * len(temperatures)

        for i in range(len(temperatures) - 2, -1, -1):
            count = i + 1
            while count < len(temperatures) and temperatures[i] >= temperatures[count]:
                if days[count] == 0:   # nothing warmer ever comes after count
                    count = len(temperatures)
                    break
                count += days[count]   # jump straight to count's next warmer day

            if count < len(temperatures):
                days[i] = count - i

        return days