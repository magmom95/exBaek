num = int(input())
for i in range(num):
    sco = list(map(int, input().split()))
    avg = sum(sco[1:]) / sco[0]
    cnt = 0
    for j in sco[1:]:
        if j > avg:
            cnt += 1
    print("%.3f%%" % round(cnt/sco[0]*100, 3))
