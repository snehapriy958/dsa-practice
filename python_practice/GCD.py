class Solution:
    def gcd(self,num:int)->int:
        while num>0:
            if n1>n2:
                n1%=n2
            else:
                n2%=n1
        if n1==0:
            return n2
        else:
            return n1
n1,n2=9,12
obj=Solution()
print(f"GCD of {n1} and {n2} is ",obj.gcd(n1,n2))