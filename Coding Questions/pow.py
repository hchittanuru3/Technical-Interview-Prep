def pow(x, n):
    if n == 0:
        return 1
    if n == 1:
        return x
    if n % 2 == 0:
        return pow(x, n/2) * pow(x, n/2)
    else:
        return pow(x, n/2) * pow(x, n/2) * x

