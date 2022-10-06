
# import copy
import random
import time

# data_read = list()
# adj_matrix = list()
# succ_list = list()
number_of_edges = 0
number_of_vertices = 0


# user_graph_choice = -1
# path = list()
# visited = list()
# start = 0


def generator_ham(n, sat):
    global number_of_vertices, number_of_edges
    data_read = list()
    succ_list = [[] for k in range(n)]
    pred_list = [[] for k in range(n)]
    saturation = int((n * (n - 1)) * sat)
    visited = list()

    for k in range(saturation + 1):
        if k == saturation:
            node = visited[0]
        else:
            node = random.randint(0, n - 1)
            if visited:
                counter = 0
                while node == visited[-1] or node in succ_list[visited[-1]] or (node in visited and k < n):
                    if counter > 50:
                        return False
                    node = random.randint(0, n - 1)
                    counter += 1

        if not visited:
            visited.append(node)
        else:
            succ_list[visited[-1]].append(node)
            pred_list[node].append(visited[-1])
            visited.append(node)
    number_of_vertices = n
    number_of_edges = (n * (n - 1)) * saturation
    for x in range(n):
        for y in succ_list[x]:
            data_read.append([x, y])

    return data_read


# def generator(nov):
#     global number_of_vertices, number_of_edges, data_read
#     data_read.clear()
#
#     noe = int((nov * (nov - 1) / 2) // 2)
#
#     graph_list = []
#     vertex_dag = []
#
#     while len(vertex_dag) != nov:
#         x = random.randint(1, nov)
#         if not (x in vertex_dag):
#             vertex_dag.append(x)
#
#     index = 1
#     h = []
#
#     for i in range(nov):
#         for j in range(index, nov):
#             h.append([vertex_dag[i], vertex_dag[j]])
#         index += 1
#
#     for i in range(len(h)):
#         if i % 2 != 0:
#             graph_list.append(h[i])
#
#     graph_list.sort()
#
#     graph_list.insert(0, [nov, noe])
#
#     number_of_vertices = graph_list[0][0]
#     number_of_edges = graph_list[0][1]
#     graph_list = graph_list[1:]
#     data_read = copy.deepcopy(graph_list)


# def remove_edge(x, y, array, g_type):
#     if g_type == 1:
#         array[x][y] = 0
#         array[y][x] = 0
#     elif g_type == 2:
#         array[x][y] = 0
#         array[y][x] = 0


# funkcja pobiera od uzytkownika informacje na temat rodzaju grafu; skierowany lub nieskierowany
def choose_graph_type():
    user_graph_choice = -1

    while int(user_graph_choice) not in (1, 2):
        user_graph_choice = input("NON-DIRECTED GRAPH - enter \"1\"\nDIRECTED GRAPH - enter \"2\"\n")
        if user_graph_choice.isnumeric():
            user_graph_choice = int(user_graph_choice)
        else:
            user_graph_choice = -1

    return user_graph_choice


# funkcja pobiera od uzytkownika informacje na temat  sposobu pobierania danych; recznie lub z klawiatury
def choose_data_input():
    user_input_choice = -1

    # check if input is a number
    while int(user_input_choice) not in (1, 2):
        user_input_choice = input("To enter data by hand - enter \"1\"\nTo enter data from a file - enter \"2\"\n")
        if user_input_choice.isnumeric():
            user_input_choice = int(user_input_choice)
        else:
            user_input_choice = -1

    return user_input_choice


# funkcja wczytuje od uzytkownika informacje na temat grafu
def read_by_hand():
    global number_of_vertices, number_of_edges
    data_read = list()

    while True:
        number_of_vertices = input("ENTER NUMBER OF VERTICES: ")
        number_of_edges = input("ENTER NUMBER OF EDGES: ")
        if number_of_edges.isnumeric() and number_of_vertices.isnumeric():
            break
    number_of_vertices = int(number_of_vertices)
    number_of_edges = int(number_of_edges)

    while len(data_read) < number_of_edges:
        while True:
            user_input_edge = input("ENTER EDGE NO." + str(len(data_read) + 1) + " (EX. 1 2): ")
            if len(user_input_edge.split()) == 2:
                user_input_edge_l, user_input_edge_r = user_input_edge.split()
                if user_input_edge_l.isnumeric() and user_input_edge_r.isnumeric():
                    user_input_edge_l = int(user_input_edge_l)
                    user_input_edge_r = int(user_input_edge_r)
                    if 0 < user_input_edge_l < number_of_vertices + 1 and 0 < user_input_edge_r < number_of_vertices + 1:
                        break
        data_read.append([user_input_edge_l, user_input_edge_r])

    return data_read


# funkcja wczytuje z pliku informacje na temat grafu
def read_file():
    global number_of_vertices, number_of_edges
    data_read = list()

    # proba otwarcia podanego pliku
    while True:
        try:
            read_dir_path = input("Please enter absolute path of your file: ")
            read_dir_handle = open(read_dir_path, "rt")
            break
        except IOError:
            print("File not accessible")
            pass

    # wczytywanie kazdej linii
    for line in read_dir_handle:
        try:
            left, right = line.split()
            left.strip()
            right.strip()

            left = int(left)
            right = int(right)
            data_read.append([left, right])

        except ValueError:
            print("ERROR: NOT ENOUGH VALUES IN A LINE OR FILE CONTAINS NON-NUMERIC CHARACTERS")

    # jesli zadeklarowana liczba krawedzi nie zgadza sie z liczba linijek, uruchom funkcje ponownie
    if len(data_read) - 1 != data_read[0][1]:
        print("FILE DATA IS CORRUPTED. DECLARED NUMBER OF EDGES DOESN'T MATCH A NUMBER OF LINES IN A FILE.")
        read_file()

    number_of_vertices = data_read[0][0]
    number_of_edges = data_read[0][1]
    data_read = data_read[1:]

    return data_read


# funkcja tworzy liste nastepnikow
def succ_list_build(data_read, number_of_vertices):
    succ_list = [[] for i in range(number_of_vertices)]
    for x in data_read:
        succ_list[x[0] - 1].append(x[1] - 1)

    return succ_list


# funkcja tworzy macierz sasiedztwa
def adj_matrix_build(data_read, number_of_vertices, user_graph_choice):
    if number_of_vertices > 1:

        adj_matrix = [[0] * number_of_vertices for i in range(number_of_vertices)]
        for x in range(len(data_read)):
            l = data_read[x][0]
            r = data_read[x][1]

            if user_graph_choice == 1:
                adj_matrix[r - 1][l - 1] += 1
                adj_matrix[l - 1][r - 1] += 1
            elif user_graph_choice == 2:
                adj_matrix[r - 1][l - 1] -= 1
                adj_matrix[l - 1][r - 1] += 1
        return adj_matrix

    else:
        print("GRAPH MUST CONTAIN AT LEAST TWO VERTICES TO CREATE AN ADJACENCY MATRIX")


# funkcja przechodzi przez graf metoda dfs i zwraca tablice z informacja o odwiedzonych wierzcholkach
def dfs(x, visited, adj_matrix):
    visited[x] = True

    for y in [z for z in range(number_of_vertices) if adj_matrix[x][z] == 1]:
        if visited[y] is False:
            dfs(y, visited, adj_matrix)


# funkcja analogiczna do dfs, ale na liscie nastepnikow
def dfs_d(x, visited, succ_list):
    visited[x] = True

    for y in succ_list[x]:
        if visited[y] is False:
            dfs_d(y, visited, succ_list)


# funkcja sprawdza czy graf spelnia warunki na istnienie cyklu eulera
def verify(x, user_graph_choice, adj_matrix):
    # zweryfikuj spojnosc grafu
    visited = [False for z in range(number_of_vertices)]
    dfs(x, visited, adj_matrix)
    # if False in visited:
    #     print("GRAF NIE JEST SPÓJNY")
    #     return False

    if user_graph_choice == 1:
        for y in adj_matrix:
            if sum(y) % 2 != 0:
                print("NIE WSZYSTKIE WIERZCHOLKI W GRAFIE SA PARZYSTEGO STOPNIA")
                return False
    elif user_graph_choice == 2:
        for y in adj_matrix:
            if sum(y) != 0:
                print("NIE WSZYSTKIE WIERZCHOLKI MAJA STOPIEN ZEROWY")
                return False

    return True


# funkcja weryfikuje czy wierzcholek nie jest mostem do innych wierzcholkow
# i czy mozna uzyc wierzcholka jako nastepnego w cyklu eulera
def is_not_bridge_nond(adj_matrix, x, y):
    # jesli wierzcholek posiada tlyko jeden nastepnik to zwraca prawde
    if len([z for z in range(number_of_vertices) if adj_matrix[x][z] == 1]) == 1:
        return True
    else:

        # liczymy wierzcholki, do ktorych mozemy sie dostac gdy istnieje krawedz x-y
        visited = [False for z in range(number_of_vertices)]
        dfs(x, visited, adj_matrix)
        count1 = len([z for z in visited if z is True])

        # usuwamy krawedz x-y
        adj_matrix[x][y] = 0
        adj_matrix[y][x] = 0

        # liczymy wierzcholki, do ktorych mozemy sie dostac gdy nie istnieje krawedz x-y
        visited = [False for z in range(number_of_vertices)]
        dfs(x, visited, adj_matrix)
        count2 = len([z for z in visited if z is True])

        # dodajemy z powrotem krawedz x-y
        adj_matrix[x][y] = 1
        adj_matrix[y][x] = 1

        # jesli mozemy dostac sie do wiekszej ilosci wierzcholkow gdy istnieje krawedz x-y, to krawedz jest mostem
        return False if count1 > count2 else True


# def is_not_bridge_d(succ_list, x, y):
#     # The edge u-v is valid in one of the following two cases:
#
#     #  1) If v is the only adjacent vertex of u
#     if len(succ_list[x]) == 1:
#         return True
#     else:
#         '''
#          2) If there are multiple adjacents, then u-v is not a bridge
#              Do following steps to check if u-v is a bridge
#
#         2.a) count of vertices reachable from u'''
#         visited = [False for z in range(number_of_vertices)]
#         dfs_d(x, visited, succ_list)
#         count1 = len([z for z in visited if z is True])
#         #print(x,visited)
#         '''2.b) Remove edge (u, v) and after removing the edge, count
#             vertices reachable from u'''
#         #print(x, y, succ_list)
#         index = None
#         for z in range(len(succ_list[x])):
#
#             if succ_list[x][z] == y:
#                 index = z
#                 succ_list[x].pop(z)
#                 break
#
#         visited = [False for z in range(number_of_vertices)]
#         dfs_d(x, visited, succ_list)
#         count2 = len([z for z in visited if z is True])
#         #print(x, visited)
#         #print("///////////////////////")
#         # 2.c) Add the edge back to the graph
#         succ_list[x].insert(index, y)
#
#         # 2.d) If count1 is greater, then edge (u, v) is a bridge
#         return False if count1 > count2 else True


def ham_nond(start, path, visited, adj_matrix, x):
    # zaznaczamy wierzchołek jako odwiedzony
    visited[x] = True

    # dla wszystkich następników
    for y in [z for z in range(number_of_vertices) if adj_matrix[x][z] == 1 and z != x]:

        # jeśli dotarliśmy do węzła początkowego, to zwracamy prawdę
        if y == start and len([j for j in range(number_of_vertices) if visited[j] is True]) == number_of_vertices:
            path.append(x + 1)
            return True

        # jeśli węzeł nie został jeszcze odwiedzony, to wykonujemy dla niego funkcję i jeśli zwraca prawdę, to dodajemy go do ścieżki
        if not visited[y]:
            if ham_nond(start, path, visited, adj_matrix, y):
                path.append(x + 1)
                return True

    # jeśli funkcja nie zwróciła prawdy, czyli nie znaleziono cyklu dla następników naszego węzła, to kończymy działanie funkcji
    visited[x] = False
    return False


def ham_d(start, path, visited, succ_list, x):
    # zaznaczamy wierzchołek jako odwiedzony
    visited[x] = True

    # dla wszystkich następników
    for y in succ_list[x]:

        # jeśli dotarliśmy do węzła początkowego, to zwracamy prawdę
        if y == start and len([j for j in range(number_of_vertices) if visited[j] is True]) == number_of_vertices:
            path.append(x + 1)
            return True

        # jeśli węzeł nie został jeszcze odwiedzony, to wykonujemy dla niego funkcję i jeśli zwraca prawdę, to dodajemy go do ścieżki
        if not visited[y]:
            if ham_d(start, path, visited, succ_list, y):
                path.append(x + 1)
                return True
    # jeśli funkcja nie zwróciła prawdy, czyli nie znaleziono cyklu dla następników naszego węzła, to kończymy działanie funkcji
    visited[x] = False
    return False


def euler_d(succ_list, x, path):
    # jesli istnieja nastepniki, to wykonujemy funkcje
    if succ_list[x]:

        # dla kazdego nastepnika
        for y in succ_list[x]:
            # if is_not_bridge_d(succ_list, x, y):

            # usun krawedz i wykonaj funkcje dla nastepnego wierzcholka
            succ_list[x].remove(y)
            euler_d(succ_list, y, path)

        path.append(x + 1)


def euler_nond(adj_matrix, x, path):
    if 1 in adj_matrix[x]:
        for y in [z for z in range(number_of_vertices) if adj_matrix[x][z] == 1]:

            if is_not_bridge_nond(adj_matrix, x, y):
                adj_matrix[x][y] = 0
                adj_matrix[y][x] = 0

                euler_nond(adj_matrix, y, path)

        path.append(x + 1)


def main():
    #g_type = int(choose_graph_type())
    #i_type = int(choose_data_input())#

    #if i_type == 1:
    #    data_read = read_by_hand()
    #elif i_type == 2:
    #    data_read = read_file()

    #if data_read:
    #    succ_list = succ_list_build(data_read, number_of_vertices)
    #    adj_matrix = adj_matrix_build(data_read, number_of_vertices, g_type)
    #else:
    #    print("ERROR RETRIEVING DATA FROM INPUT")
    #    main()

    visited = [False for x in range(number_of_vertices)]
    path = list()
    start = 0

    menu = True

    while menu is True:
        print("///////////// MAIN MENU /////////////")
        print("6. EXIT")
        print("7. TESTS")
        while True:
            user_input = input(": ")
            if user_input.isnumeric():
                break
        if user_input == "1":

            g_type = int(choose_graph_type())
            i_type = int(choose_data_input())

            if i_type == 1:
                data_read = read_by_hand()
            elif i_type == 2:
                data_read = read_file()

            if data_read:
                succ_list = succ_list_build(data_read, number_of_vertices)
                adj_matrix = adj_matrix_build(data_read, number_of_vertices, g_type)
            else:
                print("ERROR RETRIEVING DATA FROM INPUT")

        elif user_input == "2":

            format_row = "{:>12}" * (number_of_vertices + 1)
            print("\nADJACENCY MATRIX:")
            print(format_row.format("", *[i + 1 for i in range(number_of_vertices)]))
            for y in range(number_of_vertices):
                print(format_row.format(y + 1, *adj_matrix[y]))

        elif user_input == "3":

            print(len(max(succ_list, key=len)) + 1)
            format_row = "{:>12}" * (len(max(succ_list, key=len)))
            print("\nSUCCESSOR LIST:")
            for y in range(number_of_vertices):
                format_row = "{:>12}" * (len(succ_list[y]) + 1)
                print(format_row.format(y + 1, *[z + 1 for z in succ_list[y]]))

        elif user_input == "4":

            if g_type == 1:

                if ham_nond(start, path, visited, adj_matrix, start):
                    print("CYCLE FOUND: ", path[::-1])
                else:
                    print("CYCLE NOT FOUND")

            elif g_type == 2:

                if ham_d(start, path, visited, succ_list, start):
                    print("CYCLE FOUND: ", path[::-1])
                else:
                    print("CYCLE NOT FOUND")

        elif user_input == "5":

            if verify(start, g_type, adj_matrix):
                if g_type == 1:
                    euler_nond(adj_matrix, start, path)
                    print("CYCLE FOUND: ", path[::-1])

                elif g_type == 2:

                    euler_d(succ_list, start, path)
                    print("CYCLE FOUND: ", path[::-1])

        elif user_input == "6":
            print("GOOD BYE!")
            menu = False

        elif user_input == "7":
            location=str(input("wprowadź lokalizację, dokąd chcesz wstawić plik z testami (znak \ zmień na podwójny \ ):\n"))
            fopen = open(location, "wt")
            fopen.write("Number of vertexes, Saturation, Graph, Algorithm, Time\n")
            poczilosc=int(input("poczatkowa ilosc wierzcholków: "))
            koncilosc=int(input("poczatkowa ilosc wierzcholków: "))
            step=int(input("step: "))
            for x in range(poczilosc, koncilosc+1,step):
                for y in range(1, 10):
                    for z in range(15):
                        print(x, f"nasycenie {y*10}%", z)
                        data = False
                        while data is False:
                            data = generator_ham(x, y / 10)

                        visited = [False for x in range(number_of_vertices)]
                        path = list()
                        start = 0
                        adj_matrix = adj_matrix_build(data, x, 1)
                        succ_list = succ_list_build(data, x)
                        stop1 = time.perf_counter()
                        ham_d(start, path, visited, succ_list, start)
                        stop2 = time.perf_counter()
                        ham_nond(start, path, visited, adj_matrix, start)
                        stop3 = time.perf_counter()
                        euler_d(succ_list, start, path)
                        stop4 = time.perf_counter()
                        euler_nond(adj_matrix, start, path)
                        stop5 = time.perf_counter()
                        fopen.write(", ".join([str(x), str(y / 10), "directed", "euler", f"{stop4 - stop3:0.8f}\n"]))
                        fopen.write(", ".join([str(x), str(y / 10), "directed", "hamilton", f"{stop2 - stop1:0.8f}\n"]))
                        fopen.write(
                            ", ".join([str(x), str(y / 10), "non-directed", "euler", f"{stop5 - stop4:0.8f}\n"]))
                        fopen.write(", ".join([str(x), str(y / 10), "non-directed", "hamilton", f"{stop3 - 2:0.8f}\n"]))
            print("ready")

        else:
            print("WRONG OPTION SELECTED")

        u_input_menu = input("\nINPUT ANYTHING TO RETURN TO MENU: ")


main()

