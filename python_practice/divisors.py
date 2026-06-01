import math
class Solution:
    def divisor(self,num:int)->int:
        list1=[]
        
        for i in range(1,int(math.sqrt(num))+1):
            if num%i==0:
                list1.append(i)
                list1.append(int(num/i))
        return sorted(set(list1))
num=36
obj=Solution()
print(f"Divisors of {num} are ",obj.divisor(num))