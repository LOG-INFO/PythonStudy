# 집합
# 중복을 허용하지 않는다.
# 중복을 제거하기 위한 필터 역할로 종종 사용되기도 한다
# 순서가 없다. (Unordered)

# set 키워드를 사용하여 생성 가능
s1 = set([1, 2, 3])
print(s1)
print()

s2 = set("Hello")
print(s2)  # 순서는 그때그때 바뀜  {'e', 'o', 'H', 'l'}, {'H', 'o', 'e', 'l'}, {'H', 'e', 'o', 'l'}, {'l', 'o', 'H', 'e'}
print()

# 집합의 활용
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])
print("s1 : ", end='')
print(s1)
print("s2 : ", end='')
print(s2)

    # 교집합
print("[교집합] s1 & s2 ")
print(s1 & s2)
print("[교집합] s1.intersection(s2) ")
print(s1.intersection(s2))
print()

    # 합집합
print("[합집합] s1 | s2 ")
print(s1 | s2)
print("[합집합] s1.union(s2) ")
print(s1.union(s2))
print()

    # 차집합
print("[차집합] s1 - s2 ")
print(s1 - s2)
print("[차집합] s1.difference(s2) ")
print(s1.difference(s2))
print("[차집합] s2 - s1 ")
print(s2 - s1)
print("[차집합] s2.difference(s1) ")
print(s2.difference(s1))
print()


# 집합 자료형 주요 함수들
    # add
print("s1.add('a')")
s1.add('a')
print(s1)
print()

    # update
print("s1.update([4, 5, 'Heechan'])")
s1.update([4, 5, 'Heechan'])
print(s1)
print()

    # remove
print("s1.remove('a')")
s1.remove('a')
print(s1)
print()



