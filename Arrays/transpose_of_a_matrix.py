#https://leetcode.com/problems/transpose-matrix/

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix:
            return []
        m=len(matrix)
        n=len(matrix[0])
        mat=[[0 for _ in range(0,m)]for _ in range(0,n)]
        for i in range(0,len(matrix[0])):
            for j in range(0,len(matrix)):
                mat[i][j]=matrix[j][i]

        return mat
