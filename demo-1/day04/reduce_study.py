
from functools import reduce

# 0, 1, 1, 2, 3, 5, 8....

init_value = [0, 1]


def reduce_fun(a, b):
    return a + b




# 递归实现斐波那契，性能极低
def fib_fun(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n > 1:
        return fib_fun(n-1) + fib_fun(n-2)


# 循环实现斐波那契，性极最高
def fib_fun2(n):
    a,b = 0, 0
    fib_num = 0
    for i in range(n):

        if i == 0:
            a = 0
        elif i == 1:
            b = 1
        else:
            x = a + b
            a = b
            b = x

        fib_num = a + b

    return fib_num


def fib_reduce_f(a, b):
    return [a[1], a[0] + a[1]]

# reduce函数实现斐波那契，性极高
def fib_fun3(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        sum = reduce(fib_reduce_f, range(n), [0, 1])
        return sum[0]

fib_max = 10
fib_arr2 = []
for i in range(fib_max):
    fib_arr2.append(fib_fun2(i))
print(fib_arr2)

# fib_arr = []
# for i in range(10):
#     fib_arr.append(fib_fun(i))
# print(fib_arr)

fib_arr3 = []
for i in range(fib_max):
    fib_arr3.append(fib_fun3(i))
print(fib_arr3)


