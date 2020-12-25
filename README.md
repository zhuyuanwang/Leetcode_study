时间：2020年12月24日17:05:20

#### 1431. 拥有最多糖果的孩子

原题链接：https://leetcode-cn.com/problems/kids-with-the-greatest-number-of-candies

```python
def kidsWithCandies(self, candies, extraCandies):
    """
    思路:将数组里的每一项与extraCandies相加，再与max(candies)比较大小即可
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
```

时间：2020年12月25日15:45:22

#### 118. 拥有最多糖果的孩子

原题链接：https://leetcode-cn.com/problems/pascals-triangle/

```python3
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
```

