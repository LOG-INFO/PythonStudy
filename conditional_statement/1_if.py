# if의 기본 구조
# 들여쓰기로 구분
# (※ 요즘 파이썬 커뮤니티에서는 들여쓰기를 할 때 공백(Spacebar) 4개를 사용하는 것을 권장한다.)
# if 조건문:
#     수행할 문장1
#     수행할 문장2
#     ...
# else:
#     수행할 문장A
#     수행할 문장B

money_a = 3100
money_b = 2900

if money_a >= 3000:
    print("a는 택시를 탄다")
else:
    print("a는 걸어간다")

if money_b > 3000:
    print("b는 택시를 탄다")
else:
    print("b는 걸어간다")
print()

# or, and, not
if money_a >= 3000 and money_b >= 3000:
    print("money_a >= 3000 and money_b >= 3000")
elif money_a >= 3000 or money_b < 3000:
    print("money_a >= 3000 or money_b < 3000")
elif not (money_a < 3000 and money_b >= 3000):
    print("not(money_a < 3000 and money_b >= 3000)")
else:
    print("else")
print()

# in
print("1 in [1, 2, 3] : ", end='')
print(1 in [1, 2, 3])
print("1 in [1, 2, 3] : ", end='')
print(1 not in [1, 2, 3])

# pass  (java의 continue)
if 1 in [1, 2, 3]:
    pass
else:
    print("not passed")
print()

# 조건부 표현식
# 조건문이_참인_경우 if 조건문 else 조건문이_거짓인_경우
score = 60
message = "success" if score >= 60 else "failure"
print("message = \"success\" if score >= 60 else \"failure\", message : " + message)
