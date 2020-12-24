# coding=utf-8


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

if __name__ == '__main__':
    s = Solution()
    candies = [2, 3, 5, 1, 3]
    extraCandies = 3
    print(s.kidsWithCandies(candies, extraCandies))