+ [Diagonal summa](#diagonal-summa)

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