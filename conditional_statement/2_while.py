# while문의 기본 구조
# while <조건문>:
#     <수행할 문장1>
#     <수행할 문장2>
#     ...

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
