# coding=utf-8
# https://leetcode-cn.com/problemset/algorithms/

class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        """
        :param candies:
        :param extraCandies:
        :return:
        """
        result_list = []
        for candy in candies:
            candy += extraCandies
            if candy >= max(candies):
                result_list.append(True)
            else:
                result_list.append(False)
        return result_list

    def generate(self, numRows):
        """

        :param numRows:
        :return:
        """
        resultlist = []
        for i in range(numRows):
            resultlist.append([])
            for x in range(i + 1):
                if i <= 1:
                    resultlist[i].append(1)
                else:
                    resultlist[i].append('')
                    if x == 0 or x == i:
                        resultlist[i][x] = 1
                    else:
                        resultlist[i][x] = resultlist[i - 1][x - 1] + resultlist[i - 1][x]
        return resultlist

if __name__ == '__main__':
    s = Solution()
    numRows = 8
    print(s.generate(numRows))