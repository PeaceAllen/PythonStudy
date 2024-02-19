
import  sys


class Student():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 类型转字符串
    def __repr__(self):
        return f'Student: name = {self.name}, age = {self.age}'

    # 调用对象
    def __call__(self, *args, name, age):
        print(f"Student {id(self)} is called.")
        self.name = name
        self.age = age
        pass

    # 类方法：不需要实例化，就可以调用
    @classmethod
    def md5(self):
        print('md5 is class method.')
        pass


stu = Student('zhangsan', 18)
print(stu)

stu(name="wangwu", age=17)

print(sys.getsizeof(stu))

Student.md5()

# 一键查看类中的方法
print(dir(stu))

print(type(stu))

x = [ i for i in range(3)]

y = [ i for i in range(10, 20, 2)]

print(x, y)

z = list(zip(y, x))
print(z)


a = range(5)
b = list('abcde')

c = zip(b, a)

print(a)
print(b)

d = [str(x) + str(y) for x, y in c]
print(d)

print(int('5'))

