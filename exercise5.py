a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

def duplicate(list1,list2):
    lista= []
    for i in list1:
        if i in list2:
            lista.append(i)
    
    print(lista)


duplicate(a, b)
