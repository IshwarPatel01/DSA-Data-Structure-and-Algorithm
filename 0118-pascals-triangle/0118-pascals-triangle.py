class Solution(object):
    def generate(self, numRows):
        res = []
        for i in range(numRows):
            temp = [1]
            if res:
                for j in range(len(res[-1])-1):
                    s = res[-1][j] + res[-1][j+1]
                    temp.append(s)
                temp.append(1)
                res.append(temp)
            else:
                res.append([1])
        return res