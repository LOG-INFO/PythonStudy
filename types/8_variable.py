import sys  # import mudle named 'sys'

# 파이썬의 모든 자료형은 객체이다
# ex) 3 은 '정수형 객체'

print("type(3)", end='')
print(type(3))
print()

a = 3
b = 3
print("a is b", end='')
print(a is b)

# 참조 개수(Reference Count : sys.getrefcount() )
# 레퍼런스 카운트가 0이 되는 순간 그 객체( 이 예시에서는 '정수형 객체(3)')는 자동으로 사라진다
# 가비지 콜렉션(Garbage collection, 쓰레기 수집)
print("sys.getrefcount(3) : ", end='')
print(sys.getrefcount(3))
c = 3
d = 3
print("c = 3, d = 3")
print("sys.getrefcount(3) : ", end='')
print(sys.getrefcount(3))
print("결과적으로 a, b, c는 같은 '정수형 객체(3)'을 가리킨다는 것을 알 수 있다")

# 변수를 만드는 여러 가지 방법
a, b = ('python', 'life')
print("a, b = ('python', 'life')")
print("a : " + a)
print("b : " + b)
print()

(a, b) = 'python', 'life'
print("(a, b) = 'python', 'life'")
print("a : " + a)
print("b : " + b)
print()

[a, b] = ['python', 'life']
print("[a, b] = ['python', 'life']")
print("a : " + a)
print("b : " + b)
print()

a, b = b, a  # 간단히 swap할 수 있다
print("a, b = b, a")
print("a : " + a)
print("b : " + b)
print()

a = b = 'python'
print("a = b = 'python'")
print("a : " + a)
print("b : " + b)
print()

# 특정 객체를 가리키는 변수를 없애는 예
a = b = 'python__'
print("sys.getrefcount('python__') : " + str(sys.getrefcount('python__')))
del a
del b
print("del a, del b")
print("sys.getrefcount('python__') : " + str(sys.getrefcount('python__')))  # 왜 3이 남지??

