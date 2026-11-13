class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        length_of_pre = 0
        ln = []
        for i in strs:
            ln.append(len(i))

        shortest = min(ln)

        for j in range(shortest):
            curr_str_length = 0
            for i in range(len(strs)-1):
                if strs[i+1][j] == strs[i][j]:
                    curr_str_length += 1
                else:
                    break

            if curr_str_length == len(strs)-1:
                length_of_pre +=1
            else:
                break

        return strs[0][:length_of_pre]