#!/usr/bin/env python3
Copyright 2021 Jonathan Lee Komar

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
import inspect
class mycallable:
    def __init__(self, fun, nargs=None):
        '''make a callable out of fun, record number of args'''
        if nargs == None:
            if isinstance(fun, mycallable): self.nargs = fun.nargs
            else: self.nargs = len(inspect.getfullargspec(fun).args)
        else: self.nargs = nargs
        print("__init__: {}".format(nargs))
        self.fun = fun
    def __add__(self, fun):
        '''compose self and fun'''
        f = (mycallable(fun) if not isinstance(fun, mycallable) else fun)
        return mycallable(lambda *args: self(f(*args)), f.nargs)
    def __or__(self, fun):
        '''compose self and fun'''
        f = (mycallable(fun) if not isinstance(fun, mycallable) else fun)
        return mycallable(lambda *args: self(f(*args)), f.nargs)
    def __call__(self, *args):
        '''do the currying'''
        print("currying: {}".format(len(args)))
        if len(args) == self.nargs: # straight call
            return self.fun(*args)
        if len(args) == 0: # f() == f when arity of f is not 0
            return self
        if len(args) < self.nargs: # too few args
            print("args < self.nargs")
            return mycallable(lambda *ars: self.fun(*(args + ars)),
                              self.nargs-len(args))
        if len(args) > self.nargs: # if l x,y:x+y defined as l x:(l y:x+y)
            print("args > self.nargs")
            rargs = args[self.nargs:]
            res = self.fun(*(args[:self.nargs]))
            return (res(*rargs) if isinstance(res, mycallable) else res)

f = mycallable(lambda x,y : x + y) #init without any args
h = mycallable(lambda x: x**2)
q = mycallable(lambda x,y,z: x**2)
print((h + f)(1)(2))  # h(f(1)(2)) == 9 
#print((h + f)(1,2))   # h(f(1,2))  == 9
print((h | f)(1)(2))  # h(f(1)(2)) == 9 
fold = mycallable(lambda f,i,s: (f(s[0],fold(f,i,s[1:])) if s else i))
cons = mycallable(lambda a,l : [a] + l)
map  = mycallable(lambda f: fold(cons + f, []))
