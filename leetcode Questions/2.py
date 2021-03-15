def luckyNumbers (matrix):
    min_row, max_col, ans = [], [], []
    row = 0
    while row < len(matrix):
        min_row.append(min(matrix[row]))
        row+=1
    col = 0
    while col<len(matrix[0]):
        max_num, i = matrix[0][col], 1
        while i<len(matrix):
            if matrix[i][col] > max_num:
                max_num = matrix[i][col]
            i+=1
        max_col.append(max_num)
        col+=1
    for num in min_row:
        if num in set(max_col):
            ans.append(num)
            return ans

R=int(input("Enter Rows = "))
C=int(input("Enter colums = "))
matrix = [[int(input()) for x in range (C)] for y in range(R)] 
print(luckyNumbers(matrix))