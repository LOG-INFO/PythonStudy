# while문의 기본 구조
# while <조건문>:
#     <수행할 문장1>
#     <수행할 문장2>
#     ...

treeHit = 0
while treeHit < 10:
    treeHit = treeHit + 1
    print("나무를 %d번 찍었습니다." % treeHit)
    if treeHit == 10:
        print("나무 넘어갑니다.")


prompt = """
1. Add
2. Del
3. List
4. Quit

Enter number: """

number = 0
while True:
    print(prompt)
    number = int(input())
    if number == 1:
        print("Add")
    elif number == 2:
        print("Del")
    elif number == 3:
        print("List")
    elif number == 4:
        break


