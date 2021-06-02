a = int(input()) , b = int(input()) ,c = int(input())

result = str(a*b*c)

for i in range(10):
    c = result.count(str(i))
    print(c)
