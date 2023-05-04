
# def main():
for i in range(1):
    building_length = int(input())
    building_list = list(map(int, input().split()))
    cnt = 0 
    answer = 0
    for j in range(2,building_length-2):
        current_building = building_list[j]
        diff_l1 = current_building - building_list[j-1]
        diff_r1 = current_building - building_list[j+1]
        if diff_l1 > 0 and diff_r1 > 0:
            buildings_l1 = list(range(building_list[j-1]+1,current_building+1))
            buildings_r1 = list(range(building_list[j+1]+1,current_building+1))
            diff_l2 = current_building - building_list[j-2]
            diff_r2 = current_building - building_list[j+2]
            if diff_l2 > 0 and diff_r2 > 0:
                buildings_l2 = list(range(building_list[j-2]+1,current_building+1))
                buildings_r2 = list(range(building_list[j+2]+1,current_building+1))
                l2 = set(buildings_l1) & set(buildings_l2)
                r2 = set(buildings_r1) & set(buildings_r2)
                answer += len(set(l2) & set(r2))
    print(answer)
                    # return answer
                # 14
                # 0 0 3 5 2 4 9 0 6 4 0 6 0 0 




        # if diff > 0:
        #     rest_blocks = [diff + building_list[j-1]
