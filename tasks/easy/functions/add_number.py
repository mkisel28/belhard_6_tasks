def add_numb(x):
    def sname(y):
        return x + y
    return sname


foo = add_numb(2)

print(foo(3))
