#普通做法
import math
#暴力判断
def IsPrime(n):
    #判断n是否是质数
    if n == 1:
        return False
    if n == 2:
        return True
    for i in range(3,int(math.sqrt(n))+1):
        if n%i ==0:
            return False
    return True

#做部分优化，去除大于2的偶数
def IsPrime2(n):
    # 1 不是质数
    if n == 1:
        return False
    # 2 是唯一的偶质数
    if n == 2:
        return True
    # 大于 2 的偶数都不是质数
    if n % 2 == 0:
        return False
    # 只检查奇数，步长设为 2，减少循环次数
    for i in range(3, math.isqrt(n) + 1, 2):
        if n % i == 0:
            return False
    return True

