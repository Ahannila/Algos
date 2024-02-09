import random
import time



if __name__ == "__main__":

    n = 10**5
    lista = []

    start_time = time.time()
    for i in range(n):
        lista.append(i)
    end_time = time.time()

    print("time for adding:", round(end_time - start_time, 2), "s")


    print(max(lista))
    start_time = time.time()
    for i in range(n):
        lista.remove(i)
        #print(lista[i])
    end_time = time.time()

    print("time to remove:", round(end_time - start_time, 2), "s")