print("Hello, world!")
# declarare lista
list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
list1 = list

# sortare ascendenta a listei
list.sort()
print(list)

# sortare descendenta a listei
list.reverse()
print(list)

# afisare elemente pare folosind slice
lista_para = list1[0:9:2]
print(lista_para)

# afisare elemente impare folosind slice
lista_impara = list[1:10:2]
print(lista_impara)

# afisare elemente multipli ai lui 3
lista_3 = list[1:8:3]
print(lista_3)
