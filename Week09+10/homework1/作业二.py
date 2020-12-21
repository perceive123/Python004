# 作业二：自定义一个 python 函数，实现 map() 函数的功能。
def likemap(func,iterable):
    for iter in iterable:
        yield func(iter)

def square(x):
    return x**2

m=likemap(square,[1,2,3])
print(next(m))
print(next(m))
print(next(m))