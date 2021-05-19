n = int(input("몇번 수행 하시겠습니까? "))
for i in range(n):
    a, b = map(int, input("두수를 입력해주세요 : ").split())
    print(f'Case #{i+1}: {a+b}')
