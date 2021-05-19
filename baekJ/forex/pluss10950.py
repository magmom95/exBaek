n = int(input("몇번 할까여? "))

for i in range(n):
    a, b = map(int, input("두 수를 입력하세요 ").split())
    print(a+b)
