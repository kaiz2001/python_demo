""" python中的基本数据类型 """

# 整型 Int
i1 = 123
i2 = -345
print("-------- int -------")
print(type(i1))
# 浮点型 Float （实际是双精度浮点型）
d1 = 3.14
d2 = -1.25
print("-------- float -------")
print(type(d1))

# 字符型 String
s1 = "Hello Python !"
s2 = "你好，Python！"
print("-------- string -------")
print(type(s1))

# 布尔型 Boolean
b1 = True
b2 = False
print("-------- boolean -------")
print(type(b1))

# ********  复数 Complex  ************
z1 = 1 + 2j
z2 = 2 - 3j
z3 = z1 - z2
z4 = z3 * 3
print("-------- complex -------")
print(z3)
print(type(z1))


""" python中的一些结构语法格式 """

# if  elif  else
i, j = 1, 2
if i == j:
    print("相等")
elif i > j:
    print("i大于j")
else:
    print("其他")

# for
for i in range(0, 10):
    print(i, end=" ")

# while
while False:
    print("不会被执行")
