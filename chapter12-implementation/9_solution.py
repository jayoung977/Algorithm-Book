s = input()
answer = len(s)
# 1개 단위(step)부터 압축 단위를 늘려가며 확인
for step in range(1, len(s) // 2 + 1):
    print('='*50)
    print('step: ',step)
    compressed = ""
    prev = s[0:step] # 앞에서부터 step만큼의 문자열 추출
    print('prev, s[0:step]: ',prev)
    count = 1
    # 단위(step) 크기만큼 증가시키며 이전 문자열과 비교
    for j in range(step, len(s), step):
        # 이전 상태와 동일하다면 압축 횟수(count) 증가
        print(' j: ',j)
        print(' j + step: ',j + step)
        if prev == s[j:j + step]:
            count += 1
            print('count:',count)
            print(' prev == s[j:j + step]: ',prev)
        # 다른 문자열이 나왔다면(더 이상 압축하지 못하는 경우라면)
        else:
            print('--다른 문자열이 나왔다면(더 이상 압축하지 못하는 경우라면) --')
            compressed += str(count) + prev if count >= 2 else prev
            print('str(count) + prev: ',str(count) + prev)
            prev = s[j:j + step] # 다시 상태 초기화
            print('다시 상태 초기화 prev = s[j:j + step] ',prev)
            count = 1
    # 남아있는 문자열에 대해서 처리
    compressed += str(count) + prev if count >= 2 else prev
    print('남아있는 문자열 compressed ',compressed)
    # 만들어지는 압축 문자열이 가장 짧은 것이 정답
    answer = min(answer, len(compressed))
print(answer)