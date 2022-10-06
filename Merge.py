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

start_time = time.time()
def MergeSort(sequence):
    if len(sequence) > 1:
        middle = len(sequence) // 2
        Left_part = sequence[:middle]
        Right_part = sequence[middle:]
        MergeSort(Left_part)
        MergeSort(Right_part)
        left_position = right_position = k = 0
        while left_position < len(Left_part) and right_position < len(Right_part):
            if Left_part[left_position] > Right_part[right_position]:
                sequence[k] = Left_part[left_position]
                left_position += 1
            else:
                sequence[k] = Right_part[right_position]
                right_position += 1
            k += 1
        while left_position < len(Left_part):
            sequence[k] = Left_part[left_position]
            left_position += 1
            k += 1
        while right_position < len(Right_part):
            sequence[k] = Right_part[right_position]
            right_position += 1
            k += 1

MergeSort(sequence)
print("\nPosortowany ciag: ",sequence)
print("--- s seconds:",  (time.time() - start_time))
