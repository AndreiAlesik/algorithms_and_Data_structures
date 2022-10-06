import time
import random
#--------------------------- generator danych ----------------------------------------------
print("Czy chcesz wpisac ciag danych? - odpowiedz: Tak/Nie")
response = input()
sequence = []
if response == "Tak":
    print("Wpisz ciag liczb naturalnych ktore chcesz posortowac: ")
    sequence = [int(i) for i in input().split()]
    n = len(sequence)
    print("Ciąg wejściowy: ",sequence)
else:
    if response == "Nie":
        print("Jaki ciąg danych wygenerować: losowy/rosnący/malejący/V-kształt/A-kształt? ")
        response=input()
        if response=="losowy":
            print("Wpisz ilość generowanych elementów: ")
            n = int(input())
            for i in range(n):
                j = random.randint(1, 10*n)
                sequence = sequence + [j]
            print("Ciąg wejściowy: ",sequence)
        elif response == "rosnący":
            print("Wpisz ilość generowanych elementów: ")
            n = int(input())
            j = 0
            for i in range(n):
                j = random.randint(j+1,10*n - (n-i-1))
                sequence = sequence + [j]
            print("Ciąg wejściowy: ",sequence)
        elif response == "malejący":
            print("Wpisz ilość generowanych elementów: ")
            n = int(input())
            j = 10*n + 1
            for i in range(n):
                j = random.randint(n-i, j-1)
                sequence = sequence + [j]
            print("Ciąg wejściowy: ", sequence)
        elif response=="A-kształt":
            print("Wpisz ilość generowanych elementów: ")
            n = int(input())
            j = 0
            for i in range(n//2+1):
                j = random.randint(j+1,10*n - (n//2-i))
                sequence = sequence + [j]
            for i in range(n-n//2-1):
                j = random.randint(n-n//2-1- i, j - 1)
                sequence = sequence + [j]
            print("Ciąg wejściowy: ", sequence)
        elif response=="V-kształt":
            print("Wpisz ilość generowanych elementów: ")
            n=int(input())
            j = 10*n
            for i in range(n//2+1):
                j = random.randint(n-n//2+1-i, j-1)
                sequence = sequence + [j]
            for i in range(n-n//2-1):
                j = random.randint(j+1,10*n - (n//2-1-i))
                sequence = sequence + [j]
            print("Ciąg wejściowy: ",sequence)
        else:
            print("Niepoprawna odpowiedź")
            exit()
    else:
        print("Niepoprawna odpowiedź")
        exit()

#---------------------------------- właściwy program ----------------------------------------
change_counter = 0
compare_counter = 0
def partition(array, start, end):
    global change_counter
    global compare_counter
    i = start - 1
    pivot = 5
    print("pivot = ",pivot)
    for j in range(start, end):
        compare_counter = compare_counter + 1
        if array[j] >= pivot:
            i = i + 1
            array[i], array[j] = array[j], array[i]
            change_counter = change_counter + 1
    array[i + 1], array[end] = array[end], array[i + 1]
    #change_counter = change_counter + 1
    print(change_counter)
    return (i + 1)

def quickSort(array, start, end):
    global change_counter
    global compare_counter
    compare_counter = compare_counter + 1
    if len(array) == 1:
        return array
    compare_counter = compare_counter + 1
    if start < end:
        part_index = partition(array, start, end)
        quickSort(array, start, part_index - 1)
        quickSort(array, part_index + 1, end)

start_time = time.time()
n = len(sequence)
quickSort(sequence, 0, n - 1)
print("Posortowany ciąg: ",sequence)
print("Liczba operacji porównania: ",compare_counter)
print("Liczba operacji zamiany elementów: ",change_counter)
print("--- s seconds:",  (time.time() - start_time))
