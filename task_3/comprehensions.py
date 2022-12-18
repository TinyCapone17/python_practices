# 1
numbers = [x for x in range(1, 1001) if x % 17 == 0]

# 2
numbers_2 = [x for x in range(1, 1001) if "2" in str(x)]

# 3
palindromes = [x for x in range(1, 10001) if str(x) == str(x)[::-1]]

# 4
def num_whitespaces(s):
    return sum(1 if c == " " else 0 for c in s)

# 5
def remove_vowels(s):
    return "".join(c if c.lower() not in ("a", "e", "i", "o", "u") else "" for c in s)

# 6
def word_length(s):
    return [word for word in s.split() if len(word) <= 5]

# 7
# теоретически могут повторяться слова, и тогда непонятно, какую длину слова писать
def map_word_to_length(s):
    return {word: len(word) for word in s.split()}

# 8
def count_chars(s):
    return {c: s.count(c) for c in s.lower() if c != " "}

# 9
def map_to_squares(ls):
    return list(map(lambda x: x**2, ls))

# 10
def points_on_line(ls):
    return {(x, y): (x**2 + y**2)**0.5 for (x, y) in ls if y == 5 * x - 2}

# 11
def squares_of_even():
    return [x ** 2 for x in range(2, 27 + 1) if x % 2 == 0]

# 12
def largest_distance(ls):
    return max((x ** 2 + y ** 2) ** 0.5 for (x, y) in ls if x >= 0 and y >= 0)

# 13
def sums_and_diffs(nums_first, nums_second):
    return [(x+y, x-y) for x, y in zip(nums_first, nums_second)]

# 14
def even_squares(ls):
    # если число четное, то его квадрат четный
    # если число нечетное, то его квадрат нечетный
    return [str(int(x)**2) for x in ls if int(x) % 2 == 0]

# 15
def string_to_json(s):
    return [
        {
            line.split(",", 1)[0]: line.split(",", 1)[1].split(",")[i]
            for line in s.split("\n")
        }
        for i in range(len(s.split("\n")[0].split(",")) - 1)
    ]

# 16
def columns_sum(ls):
    return [sum(col) for col in zip(*ls)]
