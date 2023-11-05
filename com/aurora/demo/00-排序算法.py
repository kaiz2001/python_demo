arr = [-1, 10, 2, 5, 12, 8, -4, 9]


# ********************** 冒泡排序 **********************
# 核心思想：循坏遍历列表，比较相邻的元素并交换它们，
#           将最大或最小的元素“冒泡”到列表的一端，直到列表有序
# 时间复杂度：O(n^2)
def bubble_sort(arr):
    if len(arr) <= 1:
        return arr
    n = len(arr)  # 待排序列表的长度
    for i in range(n):
        for j in range(n-i-1):  # n-i-1表示未排序列表的长度
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]  # 交换
    return arr


# ********************** 快速排序 **********************
# 核心思想：选取一个基准元素，将列表分为两部分，
#           一部分小于基准元素，另一部分大于基准元素，对这两部分进行递归快速排序
# 时间复杂度：O(nlogn)
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    # 选取一个基准元素
    pivot = arr[0]
    left, right = [], []
    for element in arr[1:]:  # 元素分组
        if element < pivot:
            left.append(element)
        else:
            right.append(element)
    # 对两部分进行递归快速
    result = quick_sort(left) + [pivot] + quick_sort(right)
    return result


def main():
    print(bubble_sort(arr))


if __name__ == "__main__":
    main()
