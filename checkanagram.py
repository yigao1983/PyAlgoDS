def anagramSolution1(s1, s2):

    alist = list(s2)

    pos1 = 0
    stillOK = True

    while pos1 < len(s1) and stillOK:
        pos2 = 0
        found = False
        while pos2 < len(alist) and not found:
            if s1[pos1] == alist[pos2]:
                found = True
            else:
                pos2 += 1

        if found:
            alist[pos2] = None
        else:
            stillOK = False

        pos1 += 1

    return stillOK


def anagramSolution2(s1, s2):
    alist1 = list(s1)
    alist2 = list(s2)

    alist1.sort()
    alist2.sort()

    pos = 0
    matches = True

    while pos < len(s1) and matches:
        if alist1[pos] == alist2[pos]:
            pos += 1
        else:
            matches = False

    return matches


def anagramSolution4(s1, s2):
    c1 = [0] * 26
    c2 = [0] * 26

    if len(s1) != len(s2):
        return False

    for i in range(len(s1)):
        pos1 = ord(s1[i]) - ord("a")
        pos2 = ord(s2[i]) - ord("a")
        c1[pos1] += 1
        c2[pos2] += 1

    j = 0
    stillOK = True
    while j < 26 and stillOK:
        if c1[j] == c2[j]:
            j += 1
        else:
            stillOK = False

    return stillOK


if __name__ == "__main__":

    print(anagramSolution1("abcd", "dcba"))
    print(anagramSolution2("abcd", "dcba"))
    print(anagramSolution4("abcd", "dcba"))
