baz = set([1, 2, 3])


def foo():
    baz.add(4)


foo()
print(baz)
