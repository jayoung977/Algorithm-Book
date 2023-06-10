from itertools import permutations
n = int(input())
li = list(map(int, input().split()))
op = list(map(int, input().split()))
op_idx = []
for i in range(len(op)):
    for _ in range(op[i]):
        op_idx.append(i)


perm_li = permutations(op_idx, n-1)
max_sum = 0
min_sum = 1e9
for p in perm_li:
    sum = li[0]
    for i in range(1, n):
        num = li[i]
        op = p[i-1]
        print(num, op)
        if op == 0:
            sum = sum + num
        elif op == 1:
            sum = sum - num
        elif op == 2:
            sum = sum * num
        elif op == 3:
            sum = int(sum / num)
    max_sum = max(max_sum, sum)
    min_sum = min(min_sum, sum)

print(max_sum)
print(min_sum)
