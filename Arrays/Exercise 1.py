'''
Let us say your expense for every month are listed below,
January - 2200
February - 2350
March - 2600
April - 2130
May - 2190
Create a list to store these monthly expenses and using that find out,

1. In Feb, how many dollars you spent extra compare to January?
2. Find out your total expense in first quar
ter (first three months) of the year.
3. Find out if you spent exactly 2000 dollars in any month
4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
5. You returned an item that you bought in a month of April and
got a refund of 200$. Make a correction to your monthly expense list
based on this
'''

class Solution():
    def monthlyExp(self,expenses):
        #1st task:
        print(expenses[1]-expenses[0])
        #2nd task:
        for i in range(0,3):
            print(expenses[i])
        #3rd task:
        for i in range(len(expenses)):
            if expenses[i]==2000:
                print(expenses[i])
        print(False)
        #4th task:
        expenses.append(1980)
        print(expenses)
        #5th task:
        expenses[3] -= 200
        print(expenses)
expenses = [2200, 2350, 2600, 2130, 2190]
obj = Solution()
obj.monthlyExp(expenses)