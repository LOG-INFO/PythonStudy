def plus_multiples_of_3_and_5(limit):
    result = 0
    i = 1
    while i <= limit:
        if (i % 3) or (i % 5):
            result += i
        i += 1
    return result


print(plus_multiples_of_3_and_5(1000))
