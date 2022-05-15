
def EuclidExtend(a, b):
    if b == 0: return 1, 0, a
    else:
        x, y, d = EuclidExtend(b, a%b)
        x, y = y, (x - (a//b)*y)
        return x, y, d

if __name__ == '__main__':
    print(EuclidExtend(55, 34))