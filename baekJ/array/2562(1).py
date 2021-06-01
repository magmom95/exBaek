max = 0
num = 0
for i in range(1, 10):
    a = int(input())
    if a > max:
        max = a
        num = i
print(f'{max},{num}')
