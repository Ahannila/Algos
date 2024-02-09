def create(t, x):
    newlist = t.copy()
    
    for i in range(len(t)):
        newlist[i] += x
    
    return newlist
    

if __name__ == "__main__":
    a = [1, 2, 3]
    b = create(a, 1)
    print(a)

    print(create([1,2,3],1)) # [2,3,4]
    print(create([1,1,1,1,1],4)) # [5,5,5,5,5]
    print(create([0],10**9)) # [1000000000]