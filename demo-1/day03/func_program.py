
from functools import reduce

def add1(x):
    return x + 1


ages = [i for i in range(18, 30)]

# map(f, list)
new_ages = list(map(add1, ages))

print(ages)
print(new_ages)

new_ages2 = list(filter(lambda x: x % 2 == 0, new_ages))

print(new_ages2)

counter1 = [x for x in range(7)]

new_counter1 = reduce(lambda a, b: a+b, counter1)
print(new_counter1)



# decorator装饰器
def log(fun):
    def wrapper(*args, **kwargs):
        print(f'{fun.__name__} fun is called.')
        return fun(*args, **kwargs)
    return wrapper


@log
def test1():
    print("test1 is locally called.")
test1()


# 高阶装饰器
def log2(fun_txt):
    def wrapper1(fun):
        def wrapper2(*args, **kwargs):
            print(f'{fun_txt} is called.')
            return fun(*args, **kwargs)
        return wrapper2
    return wrapper1

@log2('test2 name is test2_function')
def test2(name, age):
    print(f'test2 is called: name = {name}, age = {age}')

test2('lisan', 18)







