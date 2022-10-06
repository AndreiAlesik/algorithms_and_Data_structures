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
def ShellSort(sequence, n):
    global change_counter
    global compare_counter
    sc=0
    interval = 1
    while interval < n:
        interval = 3 * interval + 1
        # print(interval)
    interval = interval // 9


    if interval == 0:
        interval = 1
    print("interval = ", interval)
    while interval > 0:
        sc += 1
        print(sc)
        compare_counter+=1
        for i in range(interval, n):
            temp = sequence[i]
            j = i
            compare_counter+=1
            while j >= interval and sequence[j - interval] < temp:
                change_counter+=1
                sequence[j] = sequence[j - interval]
                j -= interval
            change_counter+=1
            sequence[j] = temp


        interval //= 3
        print("interval = ", interval)

start_time = time.time()
ShellSort(sequence,len(sequence))
print("Posortowany ciag: ",(sequence))
print("Liczba operacji porównania: ",compare_counter)
print("Liczba operacji zamiany elementów: ",change_counter)
print("--- s seconds:",  (time.time() - start_time))
