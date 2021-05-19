n = int(input("몇번수행할까여? "))
for i in range(n):
    a, b = map(int, input("두 수를 입력하세요").split())
    print(f'Case #{i+1}: {a+b}')
