# -----------------------------------------------------------------------------
# sheng: exception.py
#
# Copyright (c) 2021
# luojiahai
# All rights reserved.
#
# Latest version: https://github.com/luojiahai/sheng
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# BEGIN exception.py
# -----------------------------------------------------------------------------

class ShengException(BaseException):

    def __init__(self, *args):
        super().__init__(*args)


class SyntaxException(ShengException):

    def __init__(self, message=''):
        super().__init__(f'「报错」【语法错误】{message}')


class RuntimeException(ShengException):
    
    def __init__(self, message=''):
        super().__init__(f'「报错」【运行时错误】{message}')
        

class AssertionException(ShengException):

    def __init__(self, message=''):
        super().__init__(f'「报错」【断言错误】{message}')


# -----------------------------------------------------------------------------
# END exception.py
# -----------------------------------------------------------------------------
