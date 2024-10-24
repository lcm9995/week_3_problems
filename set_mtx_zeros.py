def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        zero_cols = set()
        zero_rows = set()
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[i])):
                if matrix[i][j] == 0:
                    zero_rows.add(i)
                    zero_cols.add(j)

        for i in range(len(matrix)):
            for num in zero_cols:
                matrix[i][num] = 0
        for num in zero_rows:
            for i in range(len(matrix[num])):
                matrix[num][i] = 0