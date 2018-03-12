# 리스트는 그 값의 생성, 삭제, 수정이 가능하지만 튜플은 그 값을 바꿀 수 없다.  (final?)
# 프로그램 끝까지 값을 바꾸지 않을 때 사용한다고 함. 난 잘 안 쓸 것 같은데....?
# 리스트는 [과 ]으로 둘러싸지만 튜플은 (과 )으로 둘러싼다.

t1 = ()
t2 = (1,)                           # 단일 값일 경우 뒤에 ','
t3 = (1, 2, 3)
t4 = 1, 2, 3
t5 = ('a', 'b', ('ab', 'cd'))

# 삭제 시 오류
t1 = (1, 2, 'a', 'b')
# del t1[0]                           # TypeError: 'tuple' object doesn't support item deletion
print()

# 인덱싱
print("t1[1]")
print(t1[1])
print()

# 슬라이싱
t1 = (1, 2, 'a', 'b')
print(t1)
print("t1[1:]")
print(t1[1:])
print()

# 튜플 더하기, 곱하기
print("t1 + t1")
print(t1 + t1)
print("t1 * 3")
print(t1 * 3)
print()