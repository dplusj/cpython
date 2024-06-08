def f():
    x = 1
    a = locals()
    x = 2
    b = locals()
    print(id(a), id(b))
    print(a, b)

f()