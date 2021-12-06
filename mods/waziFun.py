# A Function for get function name.
# 一个获取函数名的函数。
import inspect

def getFuncName():
    return inspect.stack()[1][3]
