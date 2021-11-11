## https://stackoverflow.com/questions/6392739/what-does-the-at-symbol-do-in-python
import numpy as np

I = np.identity(3)
v = np.arange(3)

print(I @ v)
print(np.dot(I, v))
print(np.dot(v, I))

## PendingDeprecationWarning: the matrix subclass is not the recommended way to represent matrices or deal with linear algebra
## (see https://docs.scipy.org/doc/numpy/user/numpy-for-matlab-users.html).
## Please adjust your code to use regular ndarray.

a = np.matrix([1,2,3])
print("a =", a)
print("(a.T @ a) =", (a.T @ a))
print("(a @ a.T) =", (a @ a.T))

v = np.array([1,2,3])
print("v =", v)
print("(v.T @ v) =", (v.T @ v))
print("(v @ v.T) =", (v @ v.T))


## mimic
class Mat(list):
    def __matmul__(self, B):
        A = self
        return np.array(A) @ np.array(B)

    def __imatmul__(self, B):
        self += np.array(B)
        return self

    def __mul__(self, B):
        A = self
        return np.array(A) @ np.array(B)


A = Mat([1,2,3])

print(A @ v)
print(v @ A)
A @= v
print("A =", A)
print(type(A))
