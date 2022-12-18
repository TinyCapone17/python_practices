+ [Diagonal summa](#diagonal-summa)
+ [Merge and sort 2 sorted arrays with O(n)](#merge-and-sort-2-sorted-arrays-with-o(n))
+ [Squares numbers in list](#squares-numbers-in-list)
+ [Compress chars](#compress-chars)


## Diagonal summa

считает сумму диагональных элементов матрицы

```python
def diagonal_sum(matrix):
    # Get the number of rows and columns in the matrix
    rows = len(matrix)
    cols = len(matrix[0])

    # Initialize a variable to store the sum
    sum = 0

    # Iterate over the diagonal elements of the matrix
    for i in range(rows):
        for j in range(cols):
            if i == j:
                # If the current element is on the diagonal, add it to the sum
                sum += matrix[i][j]

    return sum

```


## Merge and sort 2 sorted arrays with O(n)

соединяет 2 сортированных массива с заданной сложностью

```python
def merge_sorted_arrays(arr1, arr2):
    merged = []
    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1
    while i < len(arr1):
        merged.append(arr1[i])
        i += 1
    while j < len(arr2):
        merged.append(arr2[j])
        j += 1
    return merged

```


## Squares numbers in list

возводит в квадрат все элементы списка и сортирует их

```python
def squares(lst):
    return sorted([elem**2 for elem in lst])

```


## Compress chars

объединяет одинаковые элементы

```python
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


```
