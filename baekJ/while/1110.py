x = int(input())
i = 0
x1 = x
while True:
    ten = x // 10
    one = x % 10
    i = i + 1
    x = ((ten+one) % 10)+one*10
    if x1 == x:
        break
print(i)
