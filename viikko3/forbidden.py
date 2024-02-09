def count(s):
    n = len(s)
    total_count = 0
    current_count = 0

    for i in range(n):
        if s[i] != 'a':
            current_count += 1
            total_count += current_count
        else:
            current_count = 0

    return total_count

if __name__ == "__main__":
    print(count("aaa"))               # 0
    print(count("saippuakauppias"))   # 23
    print(count("x"))                 # 1
    print(count("aybabtu"))           # 9
