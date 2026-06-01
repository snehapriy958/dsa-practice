class Solution:
    def name(self,name,N,count=0):
        if count==N:
            return
        print(name)
        self.name(name,N,count+1)
        
obj=Solution()
obj.name("Sneha",7)