a:1

def func(v:int) -> int:
    return 0

print(__annotations__)
print(func.__annotations__)


class A:
    def func(v:float) -> None:
        pass

a = A()
a.var = 1
## a.func.var = 1 # NG: method には変数を割り当てられない
A.func.var = 1 # OK: function には割り当てられる

print(A.func.__annotations__)

print(a.func.__annotations__)

print("A.func.var =", A.func.var)
print("a.func.var =", a.func.var)
