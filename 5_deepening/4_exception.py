#
try:
    a = [1, 2, 3, 4, 0]
    print(a[3] / a[2])

except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
except IndexError:
    print("인덱싱 할 수 없습니다.")
else:
    print("Exception이 발생하지 않았을 때 실행되는 \'else\'구문")
finally:
    print("try문의 마지막에 실행되는 \'finally\' 구문")


# Bird 클래스를 상속한 클래스에서 fly를 오버라이딩하지 않으면 NotImplementedError 발생
# (Java의 interface에 포함된 method처럼)
class Bird:
    def fly(self):
        raise NotImplementedError


class Chicken(Bird):
    def fly(self):
        print("Chicken can't fly")


class Duck(Bird):
    pass


chicken = Chicken()
chicken.fly()

duck = Duck()
# duck.fly()                # raise NotImplementedError


class MyError(Exception):
    def __str__(self):
        return "허용되지 않는 별명입니다"


def say_nick(nick):
    if nick == '바보':
        raise MyError()
    elif nick == '멍청이':
        raise MyError("허용되지 않는 별명입니다 : \'" + nick + "\'")  # 허용되지 않는 별명입니다 : '멍청이'      가 예상됐지만 그렇지 않음
    print(nick)


try:
    say_nick("천사")
    say_nick("바보")
except MyError as e:
    print(e)        # 실행되지 않음
    e.__str__()


try:
    say_nick("멍청이")
except MyError as e:
    print(e)


