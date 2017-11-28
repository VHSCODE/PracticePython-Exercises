a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

def evenNumbers(lista):
    evenNumb = []
    for i in lista:
        if i % 2 == 0:
            evenNumb.append(i)
    
    print(evenNumb)


evenNumbers(a)

