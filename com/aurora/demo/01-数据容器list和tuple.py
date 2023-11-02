""" list 列表   有序可变 """
print("************** list **************", end="\n")

print("----------- 创建 ----------")
num_list = [1, 2, 3, 4, 5, 6]  # 单一类型
complex_list = [1, 3.14, "Python", True]  # 复合类型
empty_list = []  # [] 或 list()构造方法
print(type(num_list))  # <class 'list'>
# python中的常用格式化输出方式
print(f"num_list: {num_list}")
# print("num_list: {}".format(num_list))
# print("num_list: %s" % num_list)


print("----------- 增删改查 ----------")
# 增
num_list.append("new value")
# 删
num_list.remove(1)  # 输入序号 从1开始
# 查
num = num_list[1]
print(num)
# 改
num_list[2] = 22


print("----------- 常用操作 ----------")
# 获取长度
num_list2 = [2, 4, 1, -3, 6, 0, 10, 2]
list_len = len(num_list2)
print(f"len: {list_len}")

# 遍历
for item in num_list:  # 简化方法
    print(item, end=" ")
print()
for i in range(len(complex_list)):  # 索引
    print(complex_list[i], end=" ")
print()

# 排序
num_list2.sort()
print(num_list2)

# 翻转
num_list2.reverse()
print(num_list2)

# 列表拼接
new_list = num_list2 + [666, 888]
print(new_list)

# 切片 [startIndex : endIndex : step]
num_list3 = [0, 1, 2, 3, 4, 5, 6]
# 常规用法：从1到3，默认步长为1  [1,2,3]
print(num_list3[1:4])
# 指定步长：1 -> 5  2  [1,3,5]
print(num_list3[1:6:2])
# 从0开始：0 -> 5 1  [0,1,2,3,4,5]
print(num_list3[:6])
# 到末尾：2 -> end  1  [2,3...]
print(num_list3[2:])
# 逆序：倒数index 2 -> 5  [5,4,3,2]
print(num_list3[-2:-6:-1])


'''
    Tuple 元组   有序不可变，相当于只读list
'''
print("\n************** tuple **************", end="\n")

# 创建
num_tuple = (1, 2, 3, 4, 5, 6)
empty_tuple = ()  # () 或 tuple()构造方法
print(type(num_tuple))  # <class 'tuple'>
print(num_tuple)

# 元组不可更改，其余的操作与list相同
