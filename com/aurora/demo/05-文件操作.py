# 文件操作的简单使用 （基本IO操作）
# open(文件路径, 操作方式, 编码格式)

# ************** 读取 **************
# file = open("文件操作测试数据.txt", "r", encoding="utf-8")

# # 读取文件的全部内容 （所有行）
# content = file.read()  # 读取完成后，指针停留在末尾
# print(content)

# # 读取所有行，并存储为列表
# content_list = file.readlines()  # 读取完成后，指针停留在末尾
# print(content_list)

# # 读取一行内容
# line = file.readline()  # 读取完成后，指针停留在第一行末尾
# print(line)

# line2 = file.readline() # 读取的是第二行
# print(line2)

# 指针移动，将指针移动到起始位置
# file.seek(0)

# 操作完成后关闭文件，释放资源
# file.close()


# ************** 写入 **************
# 覆盖源文件内容
# file = open("文件操作测试数据.txt", "w", encoding="utf-8")
# file.write("这是新写入的内容")
# file.close()

# 在源文件末尾追加内容
# file = open("文件操作测试数据.txt", "a", encoding="utf-8")
# file.write("这是新写入的内容")
# file.close()

# ************** 实际使用时 **************
# 使用with（上下文管理器）包裹，实现资源的自动释放和异常处理
with open("文件操作测试数据.txt", "r", encoding="utf-8") as file:
    # content = file.read()
    # print(content)

    content_list = file.readlines()

    for line in content_list:
        print(line)
