s = input() #aabbcc

li = []
for i in range(1,len(s)+1): 
    last_n = len(s)//i
    # print("="*50)
    # print('i:',i)
    # print('last_n:',last_n)
    li_per_num = []
    for j in range(last_n):
        print(i*j,i*(j+1))
        li_per_num.append(s[i*j:i*(j+1)])
    if i*(j+1) != len(s):
        li_per_num.append(s[i*(j+1):])
    # print(li_per_num)
    cnt = 0
    new_s = li_per_num[0]
    new_s_2 = ''
    for k in range(len(li_per_num)):
        if li_per_num[k] == new_s:
            cnt +=1
        else:
            new_s_2 += str(cnt)+new_s
            cnt = 1
            new_s = li_per_num[k]
    new_s_2 += str(cnt)+new_s
    new_s_2 = new_s_2.replace('1','')
    # print('new_s_2: ',new_s_2)
    li.append(len(new_s_2))
print(min(li))
    


   