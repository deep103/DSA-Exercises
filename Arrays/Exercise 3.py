'''
Create a list of all odd numbers between 1 and a max number. 
Max number is something you need to take from a user using input() function
'''

class Solution():
    def marvel(self,n):
        oddNumList = []
        for i in range(1,n+1):
            if i%2==1:
               oddNumList.append(i) 
        print(oddNumList)
n = int(input("Enter a number greater than 1: "))
obj = Solution()
obj.marvel(n)