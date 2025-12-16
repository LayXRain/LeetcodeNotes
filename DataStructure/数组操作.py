from typing import List
nums = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

def Print(nums):
    n= len(nums)
    for i in range(n):
        print(nums[i])

def zhuanzhi(nums):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            nums[i][j], nums[j][i] = nums[j][i], nums[i][j]
    return nums
#将数组顺时针转90
Print(nums)
print()
Print(zhuanzhi(nums))
print()
def T1(nums):
    n = len(nums)
    for i in range(n):
        for j in range(i+1,n):
             nums[i][j],nums[j][i]=nums[j][i],nums[i][j]
    for i in range(n):
        nums[i]=nums[i][::-1]
    return nums

Print(T1(nums))
print()
#将数组顺时针180度
def T2(nums):
    reversed = [row[::-1]for row in nums]
    rotate = reversed[::-1]
    return rotate

Print(T2(nums))
print()
#270
def T3(nums):
    n = len(nums)
    for i in range(n):
        for j in range(i+1,n):
             nums[i][j],nums[j][i]=nums[j][i],nums[i][j]
    # rotate = nums.reverse()
    rotate = nums[::-1]
    return rotate

Print(T3(nums))
print()
#以中央铅锤线反射

def T4(nums):
    n=len(nums)
    for i in range(n):
        nums[i]=nums[i][::-1]
    return nums
Print(T4(nums))
print()