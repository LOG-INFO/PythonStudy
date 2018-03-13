# 파일 생성하기
# open('name','mode')           mode : ['w', 'w+', 'r', 'r+', 'a', 'a+']
# file.write('str')
# 기존에 파일이 있다면 덮어쓰니 주의!!
print("#" * 50)
print("file.write(data)")
print("#" * 50)

f = open("새파일.txt", 'w')
for i in range(1, 11):
    data = "%d ) \n" % i
    f.write(data)
print()
f.close()

# file.readline()
# 파일의 내용 중 현재 커서의 위치 한 줄을 문자열로 리턴
print("#" * 50)
print("file.readline()")
print("#" * 50)

f = open("example_file.txt", 'r')
while True:
    line = f.readline()
    if not line:
        break
    print(line, end='')
print()
f.close()

# file.readlines()
# 파일의 내용 전체를 '한 줄 단위'로 문자열'리스트'로 리턴
print("#" * 50)
print("file.readlines()")
print("#" * 50)

f = open("example_file.txt", 'r')
lines = f.readlines()
print(lines)
for line in lines:
    print(line, end='')
print()
f.close()

# file.read()
# 파일의 내용 전체를 문자열로 리턴
print("#" * 50)
print("file.read()")
print("#" * 50)

f = open("example_file.txt", 'r')
data = f.read()
print(data)
print()
f.close()

# 'a'모드에서의 file.write()
# 파일의 뒤쪽에 이어서 입력
print("#" * 50)
print("file.write() in mode 'a'")
print("#" * 50)

f = open("example_file.txt", 'a+')                  # a+
data = "// This is example file for Python study.\n"
f.write(data)
# 파일을 읽기 위해 파일의 맨 처음으로 이동
f.seek(0)
print(f.read())
print()
f.close()


