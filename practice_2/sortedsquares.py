# title Squares numbers in list
# description возводит в квадрат все элементы списка и сортирует их
# ---end----

def squares(lst):
    return sorted([elem**2 for elem in lst])
