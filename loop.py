row, col = [int(i) for i in input().split()]
matrix = [[None] * col for j in range(row)]
dx, dy = 0, 1
x, y = 0, 0


for i in range(1, row * col + 1):
    matrix[x][y] = str(i).ljust(3)
    nx, ny = x + dx, y + dy
    if 0 <= nx < row and 0 <= ny < col and not matrix[nx][ny]:
        x, y = x + dx, y + dy
    else:
        dx, dy = dy, -dx
        x, y = x + dx, y + dy

for i in matrix:
    print(*i)