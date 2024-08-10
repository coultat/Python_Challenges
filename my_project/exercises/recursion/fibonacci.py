async def fibonacci(n):
    if n in (0, 1):
        return n
    else:
        return await fibonacci(n - 1) + await fibonacci(n - 2)
