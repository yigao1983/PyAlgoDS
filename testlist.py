import timeit
import matplotlib.pyplot as plt


def test1():
    lst = []
    for i in range(1000):
        lst += [i]


def test2():
    lst = []
    for i in range(1000):
        lst.append(i)


def test3():
    lst = [i for i in range(1000)]


def test4():
    lst = range(1000)


if __name__ == "__main__":

    t1 = timeit.Timer("test1()", "from __main__ import test1")
    print(t1.timeit(number=1000))
    t2 = timeit.Timer("test2()", "from __main__ import test2")
    print(t2.timeit(number=1000))
    t3 = timeit.Timer("test3()", "from __main__ import test3")
    print(t3.timeit(number=1000))
    t4 = timeit.Timer("test4()", "from __main__ import test4")
    print(t4.timeit(number=1000))

    popzero = timeit.Timer("x.pop(0)", "from __main__ import x")
    popend = timeit.Timer("x.pop()", "from __main__ import x")

    runtime_popzero = []
    runtime_popend = []
    testrange = range(1000000, 100000001, 1000000)
    for n in testrange:
        x = range(n)
        runtime_popzero.append(popzero.timeit(number=1000))

        x = range(n)    
        runtime_popend.append(popend.timeit(number=1000))

    plt.plot(testrange, runtime_popzero)
    plt.plot(testrange, runtime_popzero)
    plt.savefig("testpop.pdf")
