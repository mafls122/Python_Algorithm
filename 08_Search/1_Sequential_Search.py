def sequential_search(seq, n):
    for item in seq:
        if n == item:
            return True
    return False

if __name__ == '__main__':
    arr = [1, 52, 32, 11, 99]
    a = 32
    b = 100
    print(sequential_search(arr, a))  # True
    print(sequential_search(arr, b))  # False