""" set 列表  无序 唯一 """
print("************** set **************", end="\n")
# 创建
num_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}
empty_set = {}  # {} 或 set()构造方法
print(type(num_set))  # <class 'set'>
print(num_set)


print("----------- 增删改查 ----------")
# 增
num_set.add(8)
num_set.add("six")
# 删
num_set.remove(3)
num_set.discard(4)  # 当元素不存在时，该方法可避免异常崩溃
# 改  将7改为seven
num_set.remove(7)
num_set.add("seven")
print(num_set)


print("----------- 常用操作 ----------")
# 获取长度
set_len = len(num_set)
print(f"len: {set_len}")
# 交集
set1 = {1, 2, 3}
set2 = {2, 3, 4}
print(set1.intersection(set2))
# 并集
print(set1.union(set2))
# 差集: 在set1中去除，set1和set2都含有的元素（差集）
print(set1.difference(set2))

# 遍历操作与list相同，但不可通过索引获取元素

# 无序的数据容器不能进行切片操作


""" dict 字典  键值对数据  键唯一 """
print("************** dict **************", end="\n")
# 创建
person_dict = {"name": "张三", "age": "18", "gender": "male"}
print(type(person_dict))  # <class 'dict'>
print(person_dict)

print("----------- 增删改查 ----------")
# 增
person_dict["addr"] = "广西桂林"
# 删
person_dict.pop("age")
# 改
person_dict["age"] = 23
# 查
name = person_dict["name"]
age = person_dict["age"]
print("name: %s, age: %d" % (name, age))


print("----------- 常用操作 ----------")
# 获取长度
dict_len = len(person_dict)
print("len: {}".format(dict_len))
# 获取keys
keys = person_dict.keys()
print(f"keys: {keys}")
# 获取values
values = person_dict.values()
print("values: {}".format(values))
# 获取items
items = person_dict.items()
print("items: %s" % items)
# 检查键是否存在
if "name" in person_dict:
    print(True)
else:
    print(False)
