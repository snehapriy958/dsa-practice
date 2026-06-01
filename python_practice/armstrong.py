class Solution:
    def arm(self,num:int)->int:
        length=len(str(num))
        sum=0
        n=num
        while n>0:
            digit=n%10
            sum+=digit**length
            n//=10
        return sum==num
            
num=370
obj=Solution()
if obj.arm(num):
    print(f"{num} is an armstrong number.")
else:
    print(f"{num} is not an armstrong number.")