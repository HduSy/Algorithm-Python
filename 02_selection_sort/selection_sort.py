# 选择排序
def findSmallest(list):
    smallest_index = 0
    smallest = list[smallest_index]
    for i in range(1, len(list)):
        if list[i] < smallest:
            smallest = list[i]
            smallest_index = i
    return smallest_index


# O(n*n) 执行n次findSmallest
def selectionSort(list):
    newList = []
    for i in range(len(list)):
        smallest_index = findSmallest(list)
        newList.append(list.pop(smallest_index))
    return newList


if __name__ == '__main__':
    print(selectionSort([5, 3, 6, 2, 10]))
