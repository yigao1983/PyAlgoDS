def gcd(m, n):

    while m % n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm % oldn

    return n


class Fraction(object):

    def __init__(self, top, bottom):

        if bottom == 0:
            raise ValueError("Denominator cannot be 0.")

        self.num = top
        self.den = bottom

        common = gcd(self.num, self.den)

        self.num /= common
        self.den /= common

    def __str__(self):

        return str(self.num) + "/" + str(self.den)

    def __add__(self, otherfraction):

        newnum = self.num * otherfraction.den + self.den * otherfraction.num
        newden = self.den * otherfraction.den

        return Fraction(newnum, newden)

    def __eq__(self, other):

        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum == secondnum

    def __mul__(self, other):

        newnum = self.num * other.num
        newden = self.den * other.den

        return Fraction(newnum, newden)

    def __div__(self, other):

        newnum = self.num * other.den
        newden = self.den * other.num

        return Fraction(newnum, newden)


if __name__ == "__main__":

    myfraction = Fraction(3, 5)
    print(myfraction)

    f1 = Fraction(1, 4)
    f2 = Fraction(1, 2)

    print(f1 + f2)
    print(f1 * f2)
    print(f1 / f2)
    print(gcd(20, 10))
    print(f1 == f2)
