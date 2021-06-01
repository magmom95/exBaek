max = 0
n = 0
for i in range(1, 10):
    a = int(input())
    if a > max:
        max = a
        n = i
print(f'{max},{n}')
