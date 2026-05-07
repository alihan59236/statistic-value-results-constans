def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        return None
    return a / b

def greet(name):
    return f"Hello, {name}!"

def get_list(n):
    return list(range(n))

def is_even(n):
    return n % 2 == 0

def nothing():
    pass  # вернёт None

def repeat(text, times):
    return text * times

def stats(a, b, c):
    total = a + b + c
    avg = total / 3
    return {"sum": total, "avg": avg, "values": [a, b, c]}
