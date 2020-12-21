# 实现一个 @timer 装饰器，记录函数的运行时间
import time

def timer(func):
    t1 = time.time()
    def funY(*args,**kwargs):
        result=func(*args,**kwargs)
        t2 = time.time()
        print(f'共经历了{t2-t1}秒')
        return result
    return funY

@timer
def square(x,y=2):
    time.sleep(0.2)
    return x*y

print(square(5,6))
