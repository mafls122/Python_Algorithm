from bisect import bisect, bisect_left, bisect_right
# bisect(list, n) : 입력값 n의 list 위치(인덱스+1)를 반환
# bisect_left(list, n) : 입력값 n의 왼쪽 인덱스를 반환
# bisect_right(list, n) : 입력값 n의 오른쪽 인덱스를 반환

def binary_search_bisect(seq, n):
    i = bisect_left(seq, n)
    if i != len(seq) and seq[i] == n:
        return i
    else:
        return -1

def res_print(n):
    if n == -1:
        return print("없음")
    else:
        return print("%d 위치에 있음" %n)
    
if __name__ == '__main__':
    arr = [1, 3, 5, 7, 9]
    a = 2
    b = 3
    a_res = binary_search_bisect(arr, a)
    b_res = binary_search_bisect(arr, b)
    res_print(a_res)  # 없음
    res_print(b_res)  # 1 위치에 있음

    arr2 = [1, 2, 2, 2, 3, 4, 5]
    c = 2
    print(bisect(arr2, c))  # 4
    print(bisect_right(arr2, c))  # 4
    print(bisect_left(arr2, c))  # 1
    # 중복값이 몇 개?
    print(bisect_right(arr2, c) - bisect_left(arr2, c))  # 3