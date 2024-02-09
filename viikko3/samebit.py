def count(s):
    n = len(s)
    result = 0
    zeros = 0
    ones = 0
    for i in range(n):
        if s[i] == '0':
            zeros += 1
        else:
            ones += 1
    zeros = zeros * (zeros - 1) // 2 
    ones = ones * (ones - 1) // 2
    result = zeros + ones
    return result

if __name__ == "__main__":
    print(count("0101"))               # 2
    print(count("000000"))             # 15
    print(count("000111"))             # 6
    print(count("00100001101100"))     # 46


