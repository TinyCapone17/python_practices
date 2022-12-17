
def ones(lst):
    maximum, now = 0, 0
    for i in lst:
        if i == 1:
            now += 1
            if maximum < now:
                maximum = now
        else:
            now = 0
    return maximum


if __name__ == "__main__":
    print(ones([1, 1, 1, 1, 0, 1, 1, 1]))
