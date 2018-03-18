import sys

option = sys.argv[1]
memo = sys.argv[2]

if option == '-a':
    f = open('memo.txt', 'a')
    f.write(memo)
    f.write('\n')
    f.close()
elif option == '-r':
    f = open('memo.txt', 'r')
    for line in f.readlines():
        print(line, end='')
    f.close()
elif option == 'w':
    f = open('memo.txt', 'w')
    f.write(memo)
    f.write('\n')
    f.close()
else:
    print('잘못된 옵션입니다. 옵션 목록 : [-a, -r, -w]')


