# Don’t Reinvent The Wheel
# Python의 다양한 내장함수들

# abs(n) : 숫자 n의 절대값 반환
print("abs(-11.32) : " + str(abs(-11.32)))
print()

# all(i) : 반복 가능한 자료형 i(리스트, 튜플, 문자열, 딕셔너리, 집합 등)가 전부 True이면 True 반환, 하나라도 False이면 False 반환
if all([True, 1, {1, 2}, [], (1, 2)]):
    print("all(i) : True")
else:
    print("all(i) : False")
print()

# any(i) : 반복 가능한 자료형 i(리스트, 튜플, 문자열, 딕셔너리, 집합 등)가 하나라도 True이면 True 반환, 전부 False이면 False 반환
if any([True, 1, {1, 2}, [], (1, 2)]):
    print("any(i) : True")
else:
    print("any(i) : False")
print()

# chr(c) : ASKII 코드값 chr을 입력받아 해당 문자를 리턴
# ord(c) : 해당 문자의 ASKII 코드값을 리턴
print("chr(65) : " + chr(65))
print("chr(135) : " + chr(135))
print("chr(136) : " + chr(136))
print("ord(A) : " + str(ord('A')))
print()

# dir(o) : 객체가 자체적으로 가지고 있는 변수, 메서드를 반환
print("dir(list) : " + str(dir([1, 2, 3, 4])))
print("dir(dictionary) : " + str(dir({1: 3, 'a': 'A'})))
print("dir(string) : " + str(dir("string")))
print("dir(int) : " + str(dir(123)))
print()

# divmod(a, b) : a를 b로 나눈 몫, 나머지를 반환
print("divmod(8, 3) : " + str(divmod(8, 3)))
print("divmod(1.3, 0.3) : " + str(divmod(1.3, 0.3)))
print()

# enumerate(i) : 순서가 있는 자료형(리스트, 튜플, 문자열, 딕셔너리)을 입력으로 받아 인덱스 값을 포함하는 enumerate 객체를 리턴
    # for문과 함께 쓰면 유용함
for i, name in enumerate(['body', 'foo', 'bar']):
    print(i, name)
print()

dic = {'name': 'Heechan', 'age': 25, 'major': 'Computer Engineering'}
for i, name in enumerate(dic):
    print(i, name, dic[name])
print()

for i, name in enumerate('strses'):
    print(i, name)
print()

    # set은 안되나?         ->      TypeError: 'type' object is not subscriptable
# for i, name in enumerate(set[1, 2, 3, 4]):
#     print(i, name)
# print()

# eval(source, globals, locals) : 입력받은 문자열로 파이썬 함수나 클래스를 동적으로 실행하고 싶은 경우에 사용
    # 잘못쓰면 보안 망할 듯
    # globals, locals는 뭐지?
eval('print("eval(\'print(divmod(4,3))\') : " + str(divmod(4,3)))')
eval('print()')


# filter(func, iter) :
def positive(n):
    return n > 0


my_list = [1, 3, 5, -1, 7, -2, 0]
print("raw : " + str(my_list))
print("filtered : " + str(filter(positive, my_list)))
# lambda 표기법
print("filtered : " + str(filter(lambda n: n > 0, my_list)))
print()

# hex(n) : 정수값 n을 입력받아 16진수로 변환
print("hex(255) : " + str(hex(2555)))
print()

# id(o) : 객체를 입력받아 '고유 주소값'을 반환
a = 3
print("id(3) : " + str(id(3)))
print("id(4) : " + str(id(4)))  # + 16
print("id(6) : " + str(id(6)))  # + 16          word크기는 2byte이고 연속적으로 저장되어 있는 것을 알 수 있음
print("id(a) : " + str(id(a)))  # a = 3에서 a와 3의 주소값은 같다. (동일 객체이다)
print("id('My name is Heechan Yang') : " + str(id('My name is Heechan Yang')))
print()

# input([prompt]) : 사용자 입력을 받는 함수
    # Python 2.7의 경우 raw_input() 사용
# print(input("Input : "))

# int() : 문자열 or 실수를 입력받아 정수형태로 반환
    # '실수를 표현한 문자열'은 변환되지 않음
print("int(\'15124\') : " + str(int('15124')))
print("int(151.24) : " + str(int(151.24)))
# print("int('ㅎㅎ') : " + str(int('ㅎㅎ')))                # ValueError: invalid literal for int() with base 10: 'ㅎㅎ'
# print("int('151.24') : " + str(int('151.24')))            # ValueError: invalid literal for int() with base 10: '151.24'
print()


# isinstance(o, class)
class Person:
    pass


a = Person()
print("isinstance(a, Person) : " + str(isinstance(a, Person)))
print("isinstance(a, int) : " + str(isinstance(a, int)))
print()

# lambda : 함수를 생성할 때 사용하는 예약어로, def와 동일한 역할을 한다.
    # 보통 함수를 한줄로 간결하게 만들 때 사용하거나,
    # def를 사용할 수 없는 곳에 쓰인다
    # lambda 인수1, 인수2, ... : 인수를 이용한 표현식
lambda_sum = lambda n1, n2: n1+n2
print(lambda_sum(3, 4))
print()

# len(s) :  s의 길이(요소의 전체 개수)를 리턴
print(len("My name is Heechan Yang"))
print(len([1, 2, 3, 7, 8, 9]))
print()

# list(i) :
# map(i) :
# max(i) :
# min(i) :
# oct(n) : 정수 형태의 숫자 n을 8진수 문자열로 바꾸어 리턴
# open() : 파일을 여는 함수
# pow(x, y) : x^y를 리턴
# range
# sorted() : 입력값을 정렬한 후 그 결과를 리스트로 리턴
    # 리스트 자료형에도 sort라는 함수가 있다. 하지만 리스트 자료형의 sort 함수는 리스트 객체 그 자체를 정렬만 할 뿐 정렬된 결과를 리턴하지는 않는다.
# str(object) :
# tuple(i) : 반복 가능한 자료형을 입력받아 튜플 형태로 바꾸어 리턴
# type(o) : o의 자료형을 리턴
# zip(i*) : 동일한 개수로 이루어진 자료형을 묶어 줌
list(zip([1, 2, 3], [4, 5, 6]))
list(zip([1, 2, 3], [4, 5, 6], [7, 8, 9]))
list(zip("abc", "def"))