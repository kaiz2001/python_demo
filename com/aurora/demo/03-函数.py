"""
    函数定义：
        def 函数名(参数1: 参数1类型, 参数2: 参数2类型) -> 返回类型:
            函数体
    1.参数类型可自动推断
    2.返回值类型可自动推断
    3.python函数类似kotlin中的lambda表达式
"""


# 1.需指定参数
def my_sum(num1: int, num2: int) -> int:
    # 函数体
    result = num1 + num2
    return result


i, j = 3.2, 3.4
result = my_sum(i, j)
print(f"{i}+{j}={result}")


# 2.设置默认参数
def show_info(addr, name="无名之辈", age=18) -> None:
    print("name = {}, age = {}, addr = {}".format(name, age, addr))
    # 无返回值，返回None (null)


show_info(name="张三", addr="广西桂林")
show_info(age=23, addr="四川成都")


# 3.可变参数（参数数量不定）
def me_sum(*nums) -> int:
    return sum(nums)


print(me_sum(1, 2, 3, 4))
print(me_sum(1, 2, 3, 4, 5, 6))


# 4.返回多个值
def person_info() -> any:
    name = "李四"
    age = 24
    addr = "广西桂林"
    return name, age, addr


name, age, addr = person_info()
show_info(name, age, addr)


# 5.匿名函数
# x乘y
def mult(x, y): return x * y


print(mult(2, 3))


# 6.高阶函数
def apply(func, x, y):
    return func(x, y)


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


result1 = apply(add, 5, 2)
result2 = apply(subtract, 5, 2)
print("result1: %d, result2: %d" % (result1, result2))

# 7.空实现函数


def empty_func():
    pass
