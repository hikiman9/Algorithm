# 문제 설명
# N × M 크기의 얼음틀이 있다.
# 구멍이 뚫려있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시된다. 
# 구멍이 뚫려 있는 부분끼리 상, 하, 좌, 우로 붙어 있는 경우 서로 연결되어 있는 것으로 간주한다. 
# 이때 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램을 작성하시오. 
# 다음의 4 × 5 얼음 틀 예시에서는 아이스크림이 총 3개 생성된다.

# 입력 조건
# 1. 첫 번째 줄에 얼음 틀의 세로 길이 N과 가로 길이 M이 주어진다. (1 <= N, M <= 1000)
# 2. 두 번째 줄부터 N+1번째 줄까지 얼음 틀의 형태가 주어진다.
# 3. 이때 구멍이 뚫려있는 부분은 0, 그렇지 않은 부분은 1이다.

# 출력 조건
# 한 번에 만들 수 있는 아이스크림의 개수를 출력한다.

def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if graph[x][y] == 0:
        
        graph[x][y] = 1
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)

        return True
    return False

n, m = map(int, input().split())

graph=[]
for i in range(n):
    graph.append(list(map(int,input())))

answer = 0

for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            answer += 1

print(answer)