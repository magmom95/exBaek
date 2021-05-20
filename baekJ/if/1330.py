A, B = map(int, input("두수를 입력하세요 ").split())

if A > B:
    print('>')
elif A < B:
    print('<')
else:
    print('==')
