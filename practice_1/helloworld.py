def helloworld(n):
    # try:
    #     n = int(input())
    # except TypeError:
    #     raise TypeError("Input should be int")

    HELLO = "hello"
    WORLD = "world"

    for i in range(1, n + 1):
        if i % 15 == 0:
            print(f"{HELLO} {WORLD}")
        elif i % 3 == 0:
            print(HELLO)
        elif i % 5 == 0:
            print(WORLD)
        else:
            print(i)


if __name__ == "__main__":
    helloworld(50)
