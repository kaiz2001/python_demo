# 字符串操作
# 简单拼接
str1 = "Hello"
str2 = "World"
info = str1 + ", " + str2
# 输出：Hello, World


# 字符串重复
str3 = "python " * 3
# 输出：python python python


# 字符串切片
str4 = "01234567ABCabc"
print(str4[:4])  # 0123


# 字符串方法
str5 = "  ABC,abcOp  "
print(str5.upper())  # 转换为大写
print(str5.lower())  # 转换为小写
print(str5.strip())  # 去除头尾空白字符
str_list = str5.strip().split(",")  # 分割为列表
print(str_list)


# 字符替换 (实际开发中，更多的是使用正则表达式)
str6 = "Hello! Python!"
new_str6 = str6.replace("Hello", "Hi")
print(new_str6)


# 查找字符串索引
str7 = "fjihaisdfba"
index = str7.find("fb")
if index != -1:
    print("index: {}".format(index))
else:
    print("字符串未找到")
