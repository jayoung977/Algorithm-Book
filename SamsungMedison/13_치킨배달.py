from itertools import combinations
n, m = map(int, input().split())
chick_data = []
home_data = []
for i in range(n):
    li = list(map(int, input().split()))
    for j in range(n):
        if li[j] == 2:
            chick_data.append([i+1, j+1])
        elif li[j] == 1:
            home_data.append([i+1, j+1])

chick_selected = combinations(chick_data, m)


def city_chicken_distance(home_list, chicken_list):
    result = 0
    for x, y in home_list:
        min_dist = 1e9
        for cx, cy in chicken_list:
            dist = abs(x-cx) + abs(y-cy)
            min_dist = min(min_dist, dist)
        result += min_dist
    return result


min_city_result = 1e9
for c_data in chick_selected:
    city_dist = city_chicken_distance(home_data, c_data)
    min_city_result = min(min_city_result, city_dist)

print(min_city_result)
