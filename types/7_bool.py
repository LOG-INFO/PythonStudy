# bool 자료형 [True, False]

#
a = True
b = False

print("1+1 == 2 : ", end='')
print(1 + 1 == 2)
print()

print("1+2 == 2 : ", end='')
print(1 + 2 == 2)
print()

# 자료형의 True or False
# 문자열, 리스트, 튜플, 딕셔너리 등의 값이 비어 있으면(" ", [ ], ( ), { }) False.
# 당연히 비어있지 않으면 True
# 숫자에서는 그 값이 0일 땐 False. 0이 아닐 땐 True.

print("Python : ", end='')
if ["Python"]:
    print("True")
else:
    print("False")

print("\"\" : ", end='')
if "":
    print("True")
else:
    print("False")

print("['a'] : ", end='')
if ['a']:
    print("True")
else:
    print("False")

print("[] : ", end='')
if []:
    print("True")
else:
    print("False")

print("() : ", end='')
if ():
    print("True")
else:
    print("False")

print("{} : ", end='')
if {}:
    print("True")
else:
    print("False")

print("1 : ", end='')
if 1:
    print("True")
else:
    print("False")

print("0 : ", end='')
if 0:
    print("True")
else:
    print("False")

print("-1 : ", end='')
if -1:
    print("True")
else:
    print("False")

print("None : ", end='')
if None:
    print("True")
else:
    print("False")

i = 5
while i > 0:
    i -= 1
    print(i)
print()

# bool(value) 함수
print("bool('Python') : ", end='')
print(bool('Python'))
print("bool(\"\") : ", end='')
print(bool(""))
print("bool([1,2,3]) : ", end='')
print(bool([1, 2, 3]))
print("bool([]) : ", end='')
print(bool([]))
print("bool({}) : ", end='')
print(bool({}))
print("bool(()) : ", end='')
print(bool(()))
print("bool(1) : ", end='')
print(bool(1))
print("bool(0) : ", end='')
print(bool(0))
print("bool(-1) : ", end='')
print(bool(-1))
