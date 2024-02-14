'''

Enter number of rows:5
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
'''
def pattern_1(n:int) -> str:
    result = ""
    #  method 1
    for i in range(n):
        if i == n - 1:
            result = result + ("* " * n)
        else:
            result = result + ("* " * n) + "\n"

    #  method 2
    for i in range(n):
        for j in range(n):
            result = result + "*" + " "
        if i != n - 1:
            result = result + "\n"

    return result

def pattern_2(n:int) -> None:
    for i in range(1,n+1):
        print("* " * i, end="\n")



if __name__ == "__main__":
    print(pattern_1(n=5))
