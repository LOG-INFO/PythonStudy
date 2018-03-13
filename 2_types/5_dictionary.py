# key - value 구조
# 연관배열(Associate Array) or 해시(Hash)
# 비순차적 (순서를 따지지 않음)
# 형식 {Key1:Value1, Key2:Value2, Key3:Value3 ...}
dic = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
dic2 = {1: 'hi', 'a': 'my name is', 'b': 'Heechan'}
dic3 = {'a': [1, 2, 3]}

# 삭제하기  del dic[key]
print(dic)
# del dic[1]                                        # 에러 - ( KeyError: 1 )
# print(dic)
del dic['name']
print(dic)
print()

# Key를 사용해 Value 얻기
# 인덱싱이나 슬라이싱 안됨. 오직 key를 이용해야함
print("dic['phone']")
print(dic['phone'])
print()

# Dictionary 주요 함수들
    # Dictionary.keys() : 해당 Dictionary에 있는 key 값들을 나열
print("dic.keys()")
print(dic.keys())
print("dic2.keys()")
print(dic2.keys())
print()

    # 'key' in Dictionary : 해당 key가 Dictionary 안에 있는지 조사
print("'a' in dic2")
print('a' in dic2)
print("'c' in dic2")
print('c' in dic2)
print()