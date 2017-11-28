lista= [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

numeroUser = int(input("Inserta un numero: "))


def printLessThan5(l):
    lista2= []
    for i in l:
        if i < 5:
            lista2.append(i)
    print(lista2)

def printLessThanUser(l,userNumber):
    lista2= []
    for i in l:
        if i < userNumber:
            lista2.append(i)
    print(lista2)

# printLessThan5(lista)
#printLessThanUser(lista,numeroUser)
