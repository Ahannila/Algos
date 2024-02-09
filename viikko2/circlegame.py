def create(n):
    if n == 1:
        return [1]
    lista = list(range(1, n+1))
    newlist = []

    for _ in range(n-1):
        
        newlist.append(lista.pop(1))
        lista = lista[1:] + [lista[0]]

    newlist.append(lista[0])
    return newlist
    
if __name__ == "__main__":
    print(create(1)) # [1]
    print(create(3)) # [2,1,3]
    print(create(7)) # [2,4,6,1,5,3,7]