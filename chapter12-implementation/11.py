from collections import deque

N = int(input())
board = [[0]*N for i in range(N)]  #[[0]*N]*M 사용하지 말것, 모든 행 값 반복됨


apple_num = int(input())
for i in range(apple_num):
    row, col = map(int, input().split())
    board[row-1][col-1] = 2 #리스트는 0부터
# for li in board:
#     print(li)



dx = [0, 1, 0, -1]  # 하우상좌
dy = [1, 0, -1, 0]
directDict = dict()
queue = deque()
queue.append((0, 0))


change_num = int(input())
for i in range(change_num):
    X, C = map(int, input().split())
    directDict[(X)] = C  #{X1:C1, X2:C2 ...}



x, y = 0, 0
board[x][y] = 1  #초기값 board[0][0] =1 
cnt = 0
direction = 0

# ?
def turn(alpha):
    global direction
    if alpha == 'L':
        direction = (direction - 1) % 4
    else:  #D-오른쪽
        direction = (direction + 1) % 4


while True:
    cnt += 1
    x += dx[direction]
    y += dy[direction]

    if x < 0 or x >= N or y < 0 or y >= N: #벽에 부딫히면 게임끝
        break

    if board[x][y] == 2:
        board[x][y] = 1
        queue.append((x, y))
        if cnt in directDict:
            turn(directDict[cnt])

    elif board[x][y] == 0:
        board[x][y] = 1
        queue.append((x, y))
        tx, ty = queue.popleft()
        board[tx][ty] = 0
        if cnt in directDict:
            turn(directDict[cnt])

    else:
        break

print(cnt)



        





