# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

def coding(str_: str):
    count = 1
    res = []
    m = len(list(str_))
    for i in range(m):
        if i < m - 1:
            if str_[i] == str_[i + 1] and count < 9:
                count += 1
                continue
            else:
                res.append(f"{count}{str_[i]}")
                count = 1
                continue
        else:
            res.append(f"{count}{str_[i]}")
            break
    return "".join(res)


def decoding(str_: str):
    res = []
    a = len(str_)
    for i in range(1, a, 2):
        res.append(str_[i] * int(str_[i - 1]))
    return "".join(res)


s = input("Введите текст для кодировки: ")
print(f"Текст после кодировки: {coding(s)}")
print(f"Текст после декодировки: {decoding(coding(s))}")


