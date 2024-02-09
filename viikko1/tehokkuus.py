import random
import time

def count_even(numbers):
    result = 0
    for x in numbers:
        if x % 2 == 0:
            result += 1
    return result

def count_even2(numbers):
    return sum(x % 2 == 0 for x in numbers)


if __name__ == "__main__":
    #lista = []
    random.seed(1337)
    #for i in range(10**7):
    #    lista.append(random.randint(1, 10**7))

    n = 10**7

    lista = [random.randint(1, 10**7) for _ in range(n)]

    start_time = time.time()
    result = count_even(lista)
    end_time = time.time()

    print("result:", result)
    print("time:", round(end_time - start_time, 2), "s")

    start_time = time.time()
    result = count_even2(lista)
    end_time = time.time()

    print("result:", result)
    print("time:", round(end_time - start_time, 2), "s")