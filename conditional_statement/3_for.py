# for문의 기본 구조
# for 변수 in 리스트(또는 튜플, 문자열):
#     수행할 문장1
#     수행할 문장2
#     ...


test_list = ['one', 'two', 'three']

i = 0
for val in test_list:
    print(str(i) + ") " + val)
    i += 1;
print()

# range(a, b)  : a 이상 b 미만
for i in range(0, 10):
    i = i + 1
    print("나무를 %d번 찍었습니다." % i)
    if i == 10:
        print("나무 넘어갑니다.")
print()

print("[구구단]")
for i in range(2, 10):
    for j in range(1, 10):
        print(i * j, end=" ")
    print()
print()

# for문 '리스트 내포'
a = [1, 2, 3, 4]
print("result = [num * 3 for num in a]")
result = [num * 3 for num in a]
print(result)
print()

prompt = ""
index_list = [1, 2, 3, 4]
option_list = [(index_list[0], 'Add'), (index_list[1], 'Del'), (index_list[2], 'List'), (index_list[3], 'Quit')]
for (key, val) in option_list:
    prompt += str(key) + ") " + val + "\n"
prompt += "input num : "
while True:
    print(prompt, end='')
    select = int(input())
    for (key, val) in option_list:
        if select == key:
            print(val)

    if select == 4:
        break
    elif select not in index_list:
        print("잘못된 입력입니다 다시 입력해주세요")

    # if select == 1:
    #     print("Add")
    # elif select == 2:
    #     print("Del")
    # elif select == 3:
    #     print("List")
    # elif select == 4:
    #     print("Quit")
    #     break
    # else:
    #     print("잘못된 입력입니다 다시 입력해주세요")
