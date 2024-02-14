def pattern_1(n:int) -> None:
    #  method 1
    for i in range(n):
        print("*" * n, end="\n")
    #  method 2
    for i in range(n):
        for j in range(n):
            print("*", end=" ")
        print("")


if __name__ == "__main__":
    print(pattern_1(n=5))
