from esponenziazioneVeloce import expVeloce


def rabinTest(x, n):
    if n % 2 == 0:
        return True if n != 2 else False
    m = n - 1
    r = 0
    while m % 2 == 0:
        m //= 2
        r += 1
    xr = pow(x, m, n)
    if xr == 1:
        return False
    # print 'x0 ', xr
    for i in range(r):
        xr = pow(xr, 2, n)
        # print 'x' + str(i + 1), '', xr
        if xr == n - 1:
            return False
    return True

# print rabinTest(1, 3)
