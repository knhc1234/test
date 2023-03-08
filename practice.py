row, col = map(int, input().split())
matrix = []
for i in range(row):
    matrix.append(list(input()))
for i in range(row):
    for j in range(col):
        total = 0
        if matrix[i][j] == '.':
            for y in range(i-1,i+2):
                for x in range(j-1, j+2):
                    if not (y < 0 or y >= row or x < 0 or x >= col):
                        if matrix[y][x] == '*':
                            total += 1  
            matrix[i][j] = total              
            print(matrix[i][j], end ='')
        else:
            print(matrix[i][j],end='')
    print()        