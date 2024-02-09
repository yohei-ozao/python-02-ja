def mystery_function(lst):
    result = lst
    for i in range(len(lst)):
        if i % 2 == 0:
            result[i] = i ** 2
    return result
