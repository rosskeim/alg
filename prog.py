class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        wealth = []

	for i in range(len(accounts)):
		wealth.append(sum(accounts[i]))

	return max(wealth)
