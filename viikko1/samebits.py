def count(s):
    ones = 0
    zeros = 0
    for i in range(len(s)):
        if s[i] == "1":
            ones += 1
        else: zeros +=1

    if ones == zeros:
        return ones
    smallest = min(ones, zeros)
    return smallest

if __name__ == "__main__":
    print(count("01101")) # 2
    print(count("1111")) # 0
    print(count("101111")) # 1
    print(count("00001111")) # 4