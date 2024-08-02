def count_digits(n):
    if n == 1:
        return n
    return n + count_digits(n - 1)
