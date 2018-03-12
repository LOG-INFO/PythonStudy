# 함수의 기본 구조
# def 함수명(입력 인수):
#     <수행할 문장1>
#     <수행할 문장2>
#     ...


def sum(n1, n2):  # warning : (Shadows built-in name 'sum')
    return n1 + n2


print("sum(1, 3) : " + str(sum(1, 3)))
print()


def print_hi():
    print("Hi")


print_hi()
print("return value of 'print_hi()' : " + str(print_hi()))
print()


# 입력 값이 몇 개인지 모를 때는?
def sum_many(*args):
    sum = 0
    for i in args:
        sum += i
    return sum


print("sum_many(1,2,3,4) : " + str(sum_many(1, 2, 3, 4)))
print()


# 키워드 파라미터 (kwargs : keyword_parameter)
# key=value 형식으로 주어지면 kwargs라는 Dictionary에 대입됨
def kwargs_func(**kwargs):
    print(kwargs)


kwargs_func(a=3)
kwargs_func(name="Heechan", age=25, lang=['C', 'Java', 'Python', 'PHP', 'JavaScript', 'MySQL', 'HTML'])
print()


# 함수의 결과값은 오직 하나뿐
def sum_and_mul(a, b):
    return a + b, a * b  # 결과적으로 (a + b, a * b)라는 튜플 값이 반환됨


print("sum_and_mul(3, 7) : " + str(sum_and_mul(3, 7)))
print()


# 초기값(Default값) 미리 설정하기
    # *주의* 초기값을 설정하는 매개변수는 항상 뒤쪽에 둔다
def say_myself(name, old, man=True):
    print("나의 이름은 %s 입니다." % name)
    print("나이는 %d살입니다." % old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")


print("say_myself('양희찬', 25) : ", end='')
say_myself('양희찬', 25)
print("say_myself('양희찬', 25, True) : ", end='')
say_myself('양희찬', 25, True)
print("say_myself('양희찬', 25, False) : ", end='')
say_myself('양희찬', 25, False)

