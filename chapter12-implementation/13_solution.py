from itertools import combinations

n, m = map(int, input().split())
chicken, house =[],[]

for r in range(n):
    data = list(map(int, input().split()))
    for c in range(n):
        if data[c] == 1:
            house.append((r,c))
        elif data[c] == 2:
            chicken.append((r,c))

candidates = list(combinations(chicken,m))
# print('candidates >>',candidates) #candidates >> [((1, 2), (2, 2), (4, 4))]
def get_sum(candidate):
    result = 0
    for hx, hy in house:
        temp = 1e9
        for cx, cy in candidate:
            temp = min(temp, abs(hx-cx)+abs(hy-cy)) 
        result += temp
        print('get_sum candidate result',result)
    return result

result = 1e9
for candidate in candidates:  #candidate (1, 2), (2, 2), (4, 4)
    result = min(result, get_sum(candidate))
    print('candidate result',candidate,result)

print(result)