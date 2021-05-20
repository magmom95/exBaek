inp1 = int(input())
inp2 = int(input())

out1 = inp1*((inp2 % 100) % 10)
out2 = inp1*((inp2 % 100)//10)
out3 = inp1*(inp2//100)
r = inp1*inp2

print(out1)
print(out2)
print(out3)
print(r)
