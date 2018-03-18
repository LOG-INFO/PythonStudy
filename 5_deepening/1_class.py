# class
class Calculator:
    def __init__(self):
        self.result = 0

    def adder(self, num):
        self.result += num
        return self.result

    def sub(self, num):
        self.result -= num
        return self.result


cal1 = Calculator()
cal2 = Calculator()

print(cal1.adder(3))
print(cal1.adder(4))
print(cal1.adder(5))
print(cal2.adder(3))
print(cal2.adder(7))

print("type of \'cal1\' : " + str(type(cal1)))
print()


class Person:
    def __init__(self, name, age):
        print("### Contructor_Person_Start ###")
        self.name = name
        self.age = age
        print("#### Contructor_Person_End ####")

    def set_data(self, name, age):
        self.name = name
        self.age = age

    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    def print_info(self):
        print("My name is \'%s\'. I'm \'%d\' years old." % (self.name, self.age))


me = Person("Heechan Yang", 25)
me.print_info()
me.set_data("Yongjin Ahn", 26)
me.print_info()
print()


# class 상속
class Student(Person):
    def __init__(self, name, age, major):
        print("### Contructor_Student_Start ###")
        Person.__init__(self, name, age)
        self.major = major
        print("#### Contructor_Student_End ####")

    def set_major(self, major):
        self.major = major

    def print_info(self):
        Person.print_info(self)
        print("And my major is \'%s\'" % self.major)


student = Student("Heechan Yang", 25, "Computer Engineering")
student.print_info()
print()

# super() 함수


# 다중상속 시 부모생성자 여러 번 호출될 시 해결법
# http://bluese05.tistory.com/5

