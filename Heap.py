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
def heapify(array, length, i):
    global change_counter
    global compare_counter
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2

    compare_counter = compare_counter + 1
    if left < length and array[left] < array[smallest]:
        smallest = left

    compare_counter = compare_counter + 1
    if right < length and array[right] < array[smallest]:
        smallest = right

    compare_counter = compare_counter + 1
    if smallest != i:
        change_counter = change_counter + 1
        clipboard = array[i]
        array[i] = array[smallest]
        array[smallest] = clipboard
        heapify(array, length, smallest)

def heapSort(array, length):
    global change_counter
    global compare_counter
    # Build heap
    for i in range(int(length // 2), -1, -1):
        heapify(array, length, i)

    for i in range(length - 1, -1, -1):
        change_counter = change_counter + 1
        array[0], array[i] = array[i], array[0]
        heapify(array, i, 0)

start_time=time.time()
heapSort(sequence,len(sequence))
print("\nPosortowany ciąg: ",sequence)
print("Liczba operacji porównania: ",compare_counter)
print("Liczba operacji zamiany elementów: ",change_counter)
print("--- s seconds:",  (time.time() - start_time))
