def checkio(number):
    result = 1
    while number != 0:
        remain = number % 10
        number //= 10
        if remain == 0:
            continue
        result *= remain
    return result

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
