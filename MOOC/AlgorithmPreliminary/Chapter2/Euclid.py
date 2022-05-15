
def Euclid(x, y) -> int:
    if y == 0: return x
    else:
        return Euclid(y, x%y)

if __name__ == '__main__':
    print(Euclid(6, 3))