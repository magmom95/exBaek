n, x = map(int, input("횟수 숫자 입력 하세여 ").split())
Arr = list(map(int, input("입력하세여 ").split()))
for i in range(n):
    if Arr[i] < x:
        print(Arr[i], end=' ')
