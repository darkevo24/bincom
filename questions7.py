def recursive_search(lst, num):
    if len(lst) == 0:
        return False
    elif lst[0] == num:
        return True
    else:
        return recursive_search(lst[1:], num)

lst = [1, 2, 3, 4, 5]
num = 3
print(recursive_search(lst, num))  # Output: True
