import types 

class Example():
    a = "AA"
    __a = "aa"
    def __init__(self):
        self.b = "BB"
        self.__b = "bb"

t = Example()

print(dir(t))
print(vars(t))

t = types.SimpleNamespace()
t.p = "XX"
t._p = "xx"

print(dir(t))
print(vars(t))


d = {k: v for k, v in vars(t).items() if not k.startswith('_')}
print(d)


a = None 
b = a or "x"
print(b)