import random
lst = []
def num():
    i = 0
    while i < 4:
        r = random.randint(1, 9)
        lst.append(r)
        i += 1

a = 0
while a < 4:
    lst = []
    num()
    for el in lst:
        if lst.count(el) == 2:
            break
        else:
            a += 1
print(lst)
while True:
    i = 0
    c = 0
    b = 0 
    num_1 = input("Enter the number:")
    for el in lst:
        n = 0
        while i < 4:
            if el == int(num_1[i]):
                c += 1
                i += 1
                break
            while n < 4:
                if el == int(num_1[n]):
                    b += 1
                    n += 1
                    continue
                else:
                    n += 1
            else:
                i += 1
                break
    print(c, "Cows", b, "Bulls")
    if c == 4:
        break