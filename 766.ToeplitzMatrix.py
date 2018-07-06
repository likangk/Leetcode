class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        high = len(matrix)
        weight = len(matrix[0])
        for i in range(high-1):
            for j in range (weight-1):
                if matrix[i][j]!=matrix[i+1][j+1]:
                    return False
        return True