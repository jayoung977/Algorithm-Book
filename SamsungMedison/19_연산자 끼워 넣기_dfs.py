
n = int(input())
li = list(map(int, input().split()))
plus, minus, multiple, divide = map(int, input().split())


max_result = 0
min_result = 1e9


def dfs(cnt, now):
    global max_result, min_result, plus, minus, multiple, divide
    if cnt == n:
        max_result = max(max_result, now)
        min_result = min(min_result, now)
        return

    else:
        if plus > 0:
            plus -= 1
            dfs(cnt+1, now + li[cnt+1])
            plus += 1
        if minus > 0:
            minus -= 1
            dfs(cnt+1, now - li[cnt+1])
            minus += 1
        if multiple > 0:
            multiple -= 1
            dfs(cnt+1, now * li[cnt+1])
            multiple += 1
        if divide > 0:
            divide -= 1
            dfs(cnt+1, int(now / li[cnt+1]))
            divide += 1


dfs(1, li[0])
