numberUser = int(input("Insert a number: "))


def divisors(number):
    lista= []
    for i in range(1,number + 1):
        if number % i == 0:
            lista.append(i)

    print(lista)


divisors(numberUser)

