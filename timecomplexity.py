import time


def sumOfN(n):

    start = time.time()

    theSum = 0
    for i in range(1, n+1):
        theSum += i

    end = time.time()

    return theSum, end-start


if __name__ == "__main__":

    print(sumOfN(100000))
