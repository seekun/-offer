def quick_sort(lst):
    if len(lst) <= 1:
        return lst
    less = []
    greater = []
    pivot = lst.pop()
    for item in lst:
        if item < pivot:
            less.append(item)
        else:
            greater.append(item)
    lst.append(pivot)
    return quick_sort(less) + [pivot] + quick_sort(greater)