def find(t):
    sorted = t.sort()

    for i in range(len(t)):
        if i == 0 and t[i] != t[i+1]:
            return t[i]
        elif i == len(t) - 1 and t[i] != t[i-1]:
            return t[i]
        elif t[i] != t[i-1] and t[i] != t[i+1]:
            return t[i]
        
    return None
if __name__ == "__main__":
    print(find([1,1,2,1])) # 2
    print(find([4,5,5])) # 4
    print(find([1,1,1,1,2])) # 2
    print(find([8,8,5,8,8])) # 5
    print(find([5, 5, 5, 5, 5, 2, 5, 5]))