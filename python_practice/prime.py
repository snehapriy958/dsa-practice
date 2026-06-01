import math
class Solution:
    def prime(self,num:int)->int:
        for i in range(2,int(math.sqrt(num))+1):
            if num%i==0:
                return False
        return True

num=33
obj=Solution()
if obj.prime(num):
    print("Prime ")
else:
    print("Not prime")