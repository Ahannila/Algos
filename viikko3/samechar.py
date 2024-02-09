def count(s):
    result = 0
    counter = 0
    for i in range(len(s)):
        if i > 0 and s[i-1] != s[i]:
            counter = 0
        counter += 1
        result += counter
    return result

if __name__ == "__main__":
    print(count("aaa")) # 6
    print(count("abbbcaa")) # 11
    print(count("abcde")) # 5