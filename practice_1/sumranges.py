def sumranges(l):
    seq = []
    if len(l) == 0:
        return seq
    left = l[0]
    right = l[0]
    for i in range(1, len(l)):
        if l[i] - 1 != l[i-1]:
            if left == right:
                seq.append(str(left))
            else:
                seq.append(str(left) + '->' + str(right))
            left = right = l[i]
        right = l[i]
    if left == right:
        seq.append(str(left))
    else:
        seq.append(str(left) + '->' + str(right))
    return seq

if __name__ == "__main__":
    print(sumranges([0,1, 2, 3, 4, 5, 6, 7]))
