class Solution:
    def name(self,N,count=1):
        if count==N+1:
            return
        print(count)
        self.name(N,count+1)
        
obj=Solution()
obj.name(7)