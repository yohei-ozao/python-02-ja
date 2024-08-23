def mystery_function(lst):
    result = lst[:]  # オリジナルのリストをコピー
    for i in range(len(lst)):
        if lst[i] % 2 == 0:  # 要素が偶数かどうかをチェック
            result[i] = lst[i] ** 2
    return result