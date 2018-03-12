# 에러
# print() print()print()
print("a"); print("b")
print()

# 문자열 출력
head = "Python"
print(head)
print()

# 문자열 표현 " "
print("Python\'s favorite food is perl")
print("\"My name is Heechan, Yang\", I said.")
print()

# 문자열 표현 ' '
print('Python\'s favorite food is perl')
print('"My name is Heechan, Yang", I said.')
print()

# 문자열 표현 """ """
str = """My name is Heechan, Yang.
I'm 25 years old.
I like programming."""
print(str)
print()
# 문자열 표현 ''' '''
str2 = '''My name is Heechan, Yang.
I'm 25 years old.
I like programming.'''
print(str2)
print()

# 문자열 더하기(연결)
name = "Heechaan, Yang."
print("My name is " + name + ' Nice to meet you.')
print()

# 문자열 곱하기(반복)
print("##00@@"*10)
print("loopString")
print("##00@@"*10)
print()

# 문자열 슬라이싱
str3 = "My life for Ire."
print("str3 : " + str3 + "\n")
print("str3[4] : " + str3[4])               # 5번째 문자
print("str3[-3] : " + str3[-3])             # 뒤에서 3번째 문자
print("str3[0] : " + str3[0])               # 0번째 문자
print("str3[-0] : " + str3[-0])             # = 0번째 문자
print("str3[0:6] : " + str3[0:6])           # 0~6번째 문자들
print("str3[6:] : " + str3[6:])             # 7~번째 문자들
print("str3[:8] : " + str3[:8])             # ~9번째 문자들
print("str3[10:10] : " + str3[10:10])       # [a:b]  ==> a 이상, b 미만
print("str3[10:9] : " + str3[10:9])         #
print("str3[-5:20] : " + str3[-5:20])       #
print("str3[-5:10] : " + str3[-5:10])       #
print("str3[0:20] : " + str3[0:20])         #
print()

# 문자열 슬라이싱 응용
typo = "Pithon"
#   ypo[1] = "y"  # 바뀌지 않고 에러 발생 ( TypeError: 'str' object does not support item assignment )
print(typo)
print(typo[:1] + "y" + typo[2:])
print()

# 문자열 포매팅
current_temp = "It's %d degree celcius now." % 7
print(current_temp)
introduce_myself = "My name is %s." % "Heechan, Yang"
print(introduce_myself)
print()

my_name = "Heechan, Yang"
my_age = 25
introduce_myself_2 = "My name is %s. I'm %d years old." % (my_name, my_age)
print(introduce_myself_2)
print()

print("My score is %8.2f" % 3.78986698)     # 반올림은 뽀너스~
print()

