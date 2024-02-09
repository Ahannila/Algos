def count(t):
    n = len(t)
    result = 0
    left_min = float('inf')
    right_min = float('inf')

    for i in range(n - 1):
        left_min = min(left_min, t[:i])
        right_min = min(right_min, t[-(i + 1)])

        if left_min == right_min:
            result += 1

    return result


if __name__ == "__main__":
    print(count([2,1,1,3])) # 1
    print(count([1,1,1,1])) # 3
    print(count([1,2,3,1,2,3])) # 3
    print(count([1,2,3,4,3,2,1])) # 6
    print(count([4,3,2,1,2,3,4])) # 0
    print(count([5, 3, 5, 5, 2, 3, 4, 3, 3, 4])) # 