# title Compress chars
# description объединяет одинаковые элементы
# ---end----


def compress(chars):
    compressed = []
    count = 1
    for i in range(1, len(chars)):
        if chars[i] == chars[i - 1]:
            count += 1
        else:
            if count == 1:
                compressed.append(chars[i - 1])
            else:
                compressed.append(chars[i - 1] + str(count))
            count = 1
    if count == 1:
        compressed.append(chars[- 1])
    else:
        compressed.append(chars[- 1] + str(count))
    return ''.join(compressed)

