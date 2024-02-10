class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        summ=[]
        m=len(accounts)
        n=len(accounts[0])
        for i in range(m):
            maximum=0
            for j in range(n):
                maximum+=accounts[i][j]
            summ.append(maximum)
        return max(summ)
      
class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        max_wealth = 0
        for customer_wealth in accounts:
            total_wealth = sum(customer_wealth)
            max_wealth = max(max_wealth, total_wealth)
        return max_wealth



# Time Complexity: O(m * n)
# Space Complexity: O(m)
