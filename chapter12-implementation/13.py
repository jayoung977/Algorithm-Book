N, M = map(int, input().split())
# city = [[]*N for i in range(N)]
house_li = []
chicken_li = []
for i in range(1,N+1):
    each_row = list(map(int, input().split()))
    for j in range(len(each_row)):
        if each_row[j] == 0:
            pass
        elif each_row[j] == 1:
            house_li.append([i,j+1])
        else:
            chicken_li.append([i,j+1])
# print('house_li',house_li) #[[1, 3], [2, 5], [3, 2], [4, 3]]
# print('chicken_li',chicken_li) #chicken_li [[2, 3], [3, 3], [5, 5]]
distance_li = []
same_M_dist = 0
for house in house_li:
    house_per_distance = []
    for chicken in chicken_li:
        distance = abs(house[0] - chicken[0]) + abs(house[1] - chicken[1]) 
        house_per_distance.append(distance)
    same_M_dist += min(house_per_distance)
    distance_li.append(house_per_distance)
# print('distance_li>>',distance_li)


def comb(arr, n):
    result = []
    if n > len(arr):
        return result

    if n == 1:
        for i in arr:
            result.append([i])
            
    elif n > 1:
        for i in range(len(arr) - n + 1):
            for j in comb(arr[i + 1:], n - 1):
                result.append([arr[i]] + j)

    return result
    
    

# [[1, 2, 6], [2, 3, 3], [2, 1, 5], [2, 1, 3]]
distance_li_reverse = list(map(list,zip(*distance_li)))
# print('distance_li_reverse>> ',distance_li_reverse)
# [[1, 2, 2, 2], [2, 3, 1, 1], [6, 3, 5, 3]]
if M == len(chicken_li):
    print(same_M_dist)
else:
    min_distances = []
    for c in comb(list(range(0,len(chicken_li))), M):
        # not_c = set(list(range(len(chicken_li)))) - set(c)
        # print(not_c)
        # for idx in not_c:
            # distance_li_reverse.remove(distance_li_reverse[idx])
        distance_li_reverse_filtered = list(filter(lambda x:x if distance_li_reverse.index(x) in c else None, distance_li_reverse))
        distance_li = list(map(list,zip(*distance_li_reverse_filtered)))

        # print(distance_li)
        min_dis = 0
        for house in distance_li:
            min_dis+=min(house)
        min_distances.append(min_dis)
    print(min(min_distances))

distance_li_reverse =   [[1, 2, 2, 2], [2, 3, 1, 1], [6, 3, 5, 3]]
c = [0,1]
distance_li_reverse = list(filter(lambda x:x if distance_li_reverse.index(x) not in c else None, distance_li_reverse))

print(distance_li_reverse)







        
        

    

