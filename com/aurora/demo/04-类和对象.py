# python与java,javaScript,cpp,kotlin一样都属于OOP语言
# **************** 创建类 ****************
class Person:
    # 类的属性
    name = None
    age = None
    addr = None

    # 构造方法
    def __init__(self, name, age, addr):
        self.name = name
        self.age = age
        self.addr = addr

    # 类的方法
    def sayHello(self):
        print(f"Hi! I am {self.name}.")


# 创建类的实例
p1 = Person("zhangsan", 18, "guilin")
print("name={},age={},addr={}".format(p1.name, p1.age, p1.addr))
p1.sayHello()


# **************** 类的继承和方法重写 ****************
class Animal:
    name = None
    age = None

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # abstract method
    def sayHi(self):
        pass


class Cat(Animal):
    # 重写sayHi方法
    def sayHi(self):
        print(f"Hi！我是{self.name}，我{self.age}岁了")

    def todo(self):
        print("喵喵喵~~~")


class Dog(Animal):
    # 重写sayHi方法
    def sayHi(self):
        print(f"Hello！我是{self.name}，我{self.age}岁了")

    def todo(self):
        print("汪汪汪。。。")


cat = Cat("大橘", 2)
cat.sayHi()
cat.todo()

dog = Dog("三百万", 5)
dog.sayHi()
dog.todo()


# **************** 多态 ****************
class Car():
    def speak(self):
        pass


class BMW(Car):
    def speak(self):
        return "I am BMW."


class LAMB(Car):
    def speak(self):
        return "I am Lamborghini."


class WUL(Car):
    def speak(self):
        return "I am Wuling Hongguang."


def car_speak(car):
    return car.speak()


bmw = BMW()
lamb = LAMB()
wul = WUL()

print(car_speak(bmw))
print(car_speak(lamb))
print(car_speak(wul))


# **************** 类的魔术方法 ****************
# 魔术方法以双下划线开始，双下划线结束
class my_class:
    # init 构造
    def __init__(self) -> None:
        pass

    # toString  一般用于输出对象信息
    def __str__(self) -> str:
        # return f"Person:{name={self.name}, age={self.age}}"
        return " "

    # equals  对象比较 (cpp中可使用运算符重载实现)
    def __eq__(self, other: object) -> bool:
        # if isinstance(self, Cat):
        #    return self.name == other.name and self.age == other.age
        pass

    # .....
