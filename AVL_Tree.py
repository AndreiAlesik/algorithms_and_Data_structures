import time
import random
class Node(object):

    """Obiekt węzła dla AVLTree.

     Klasa węzła jest opakowana w klasę AVLTree. Wszystkie metody użytkownika są tam ujawniane.
     Metody drukowania, wyszukiwania, wstawiania, usuwania i określania wysokości dostarczonego AVLTree.

    """

    def __init__(self, data):
        """Tworzy wystąpienie obiektu Node dla AVLTree.

         Parent, left, right to wskaźniki do węzłów nadrzędnych i podrzędnych.
        """
        self.data = data
        self.parent = None
        self.left = None
        self.right = None
        self.tallness = 1



    def print_tree(self, cur_node, order=None):
        """ Wyświetla drzewo w określonej kolejności na standardowe wyjście.

         : param cur_node: Węzeł główny z Tree.get_root.
         : kolejność parametrów: Argument słowa kluczowego dla kolejności przechodzenia po drzewie.
        """
        if order == 'pre-order':
            print(*self._pre_order(cur_node, []))
        elif order == 'in-order':
            print(*self._in_order(cur_node, []))
        elif order == 'post-order':
            print(*self._post_order(cur_node, []))

    def _pre_order(self, cur_node, output):
        """Wyświetla drzewo: Root -> Left node -> Right node.

        :param cur_node: Korzeń drzewa.
        :param output: pusty list.
        :return: posortowane.
        """
        if cur_node:
            output += [cur_node.data]
            self._pre_order(cur_node.left, output)
            self._pre_order(cur_node.right, output)
        return output

    def _in_order(self, cur_node, output):
        """Wyświetla dzewo: Left node -> Root -> Right node.

        :param cur_node: Węzeł. Korzeń drzewa.
        :param output: pusty list.
        :return: posortowane dzewo.
        """
        if cur_node:
            self._in_order(cur_node.left, output)
            output += [cur_node.data]
            self._in_order(cur_node.right, output)
        return output

    def _post_order(self, cur_node, output):
        """Prints tree: Left node -> Right node -> Root.

        :param cur_node: Korzeń dzewa.
        :param output: pusty list.
        :return: posortowane dzewo.
        """
        if cur_node:
            self._post_order(cur_node.left, output)
            self._post_order(cur_node.right, output)
            output += [cur_node.data]
        return output

    def height(self, cur_node, cur_height):
        """Oblicza i zwraca wysokość drzewa.

        :param cur_node: korzeń dzewa.
        :param cur_height:  0.
        :return: Wysokość dzewa.
        """
        if not cur_node:
            return cur_height
        left_height = self.height(cur_node.left, cur_height + 1)
        right_height = self.height(cur_node.right, cur_height + 1)
        return max(left_height, right_height)

    def search(self, cur_node, data):
        """Przeszukuje dane w drzewie, wraca bool.

        :param cur_node: Korzeń dzewa.
        :param data: Dane do szukania.
        :return: bool. True jeżeli "data" znaleniona, jeżeli nie False.
        """
        if data == cur_node.data:
            return True
        elif data < cur_node.data and cur_node.left:
            return self.search(cur_node.left, data)
        elif data > cur_node.data and cur_node.right:
            return self.search(cur_node.right, data)
        return False

    def insert(self, cur_node, data):
        """Wstawia dane do drzewa.

        Wywołuje _inspect_insertion, aby sprawdzić, czy wstawienie spowodowało nierównowagę drzewa.

        :param cur_node: Korzeń drzewa.
        :param data: Data(element) do wstawienia.
        """
        if data < cur_node.data:
            if not cur_node.left:
                cur_node.left = Node(data)
                cur_node.left.parent = cur_node
                self._inspect_insertion(cur_node.left, [])
            else:
                self.insert(cur_node.left, data)

        elif data > cur_node.data:
            if not cur_node.right:
                cur_node.right = Node(data)
                cur_node.right.parent = cur_node
                self._inspect_insertion(cur_node.right, [])
            else:
                self.insert(cur_node.right, data)

        elif data == cur_node.data and cur_node.parent is not None:
            print(f'{data} już jest w dzewie. Dodawanie niemożliwe.')

    def _inspect_insertion(self, cur_node, nodes):
        """ Sprawdza, czy wstawienie stwarza potrzebę zrównoważenia poddrzewa..

        Konieczne jest ponowne wyważenie, jeśli różnica wysokości węzłów potomnych jest> 1.
        Tworzy listę węzłów do obrócenia, jeśli powyższy warunek jest spełniony.
        Wywołuje _rebalance_node z węzłami, które mają być zrównoważone.

        :param cur_node: Nowo wstawiony węzeł.
        :param nodes: pusta lista.
        """
        if not cur_node.parent:
            return

        nodes = [cur_node] + nodes
        left = self._get_height(cur_node.parent.left)
        right = self._get_height(cur_node.parent.right)
        if abs(left - right) > 1 and len(nodes) > 2:
            nodes = [cur_node.parent] + nodes
            self._rebalance_node(*nodes[:3])
            return

        new = 1 + cur_node.tallness

        if new > cur_node.parent.tallness:
            cur_node.parent.tallness = new

        self._inspect_insertion(cur_node.parent, nodes)

    def _get_height(self, cur_node):
        """ Bierze wysokość cur_node. Zwraca 0, jeśli node ma wartość None, w przeciwnym razie zwraca node.tallness.

        :param cur_node: Węzeł
        :return: Node.tallness
        """
        if not cur_node:
            return 0
        return cur_node.tallness

    def _rebalance_node(self, z, y, x):
        """Określa orientację niezrównoważonych węzłów i wywołuje wskazane metody równoważenia.

        Wywołuje _rotate_right lub _rotate_left zgodnie z orientacją niezrównoważonych węzłów.

        :param z: Najwyższy węzeł. Równowaga występuje „wokół” tego węzła.
        :param y: Dziecko z
        :param x: Dziecko y
        """
        if y == z.left and x == y.left:
            """    z
                  /
                 y
                /
               x   """
            self._right_rotate(z)

        elif y == z.left and x == y.right:
            """   z
                 /
                y 
                 \
                  x  """
            self._left_rotate(y)
            self._right_rotate(z)

        elif y == z.right and x == y.right:
            """   z
                   \
                     y 
                      \
                        x  """
            self._left_rotate(z)

        elif y == z.right and x == y.left:
            """   z
                    \
                      y
                    /
                  x  """
            self._right_rotate(y)
            self._left_rotate(z)

        else:
            raise Exception('Drzewo uszkodzone')

    def _right_rotate(self, z):
        """Obraca się wokół z, aby zrównoważyć poddrzewo.

        :param z: Korzeń poddrzewa do zrównoważenia.
        """
        temp = z.parent
        y = z.left
        x = y.right

        y.right = z
        z.parent = y
        z.left = x

        if x:
            x.parent = z

        y.parent = temp

        if y.parent:
            if y.parent.left == z:
                y.parent.left = y
            else:
                y.parent.right = y

        z.tallness = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.tallness = 1 + max(self._get_height(y.left), self._get_height(y.right))

    def _left_rotate(self, z):
        """Obraca się wokół z, aby zrównoważyć poddrzewo.

        :param z: Korzeń poddrzewa do zrównoważenia.
        """
        temp = z.parent
        y = z.right
        x = y.left

        y.left = z
        z.parent = y
        z.right = x

        if x:
            x.parent = z

        y.parent = temp

        if y.parent:
            if y.parent.left == z:
                y.parent.left = y
            else:
                y.parent.right = y

        z.tallness = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.tallness = 1 + max(self._get_height(y.left), self._get_height(y.right))

    def delete(self, node):
        """ Usuwa węzeł znaleziony w _find_node.

        Usuwa węzły i obsługuje osierocone elementy potomne usuniętego węzła, jeśli takie istnieją.
        Usunięte węzły z dwojgiem dzieci są obsługiwane przez znalezienie najmniejszego krewnego prawego dziecka usuniętego węzła,
        zastąpienie danych węzła, który ma zostać usunięty, danymi jego mniejszego krewnego, a następnie zaznaczenie mniejszego krewnego
        zamiast tego zostać usunięty. To zachowuje imperatyw BST.
        Wywołuje _inspect_deletion, aby zapewnić prawidłowe równoważenie poddrzewa po usunięciu.

        :param node: Węzeł do usunięcia.
        """
        def smallest_node(curr_node):
            """ Znajduje najmniejszego krewnego curr_node.

            :param curr_node: Węzeł.
            :return: Względem curr_node z najmniejszą wartością.
            """
            while curr_node.left:
                curr_node = curr_node.left
            return curr_node

        def children(curr_node):
            """ Znajduje liczbę dzieci curr_node.

             :param curr_node: Węzeł
             :return: Liczba dzieci curr_node.
            """
            num = 0
            if curr_node.left:
                num += 1
            if curr_node.right:
                num += 1
            return num

        node_parent = node.parent
        node_children = children(node)

        # Węzły liści można po prostu usunąć.
        if node_children == 0:
            if node_parent:
                if node_parent.left == node:
                    node_parent.left = None
                else:
                    node_parent.right = None
            else:
                return None

        # Rodzic usuniętego węzła stał się rodzicem usuniętego dziecka.
        if node_children == 1:
            if node.left:
                child = node.left
            else:
                child = node.right
            if node_parent:
                if node_parent.left == node:
                    node_parent.left = child
                else:
                    node_parent.right = child
            else:
                child.parent = node_parent
                return child  # wraca, żeby promować dziecko w węźle głównym
            child.parent = node_parent

        """Jeśli węzeł, który ma zostać usunięty, ma dwoje dzieci, dane jego najmniejszego krewnego są promowane do kategorii do usunięcia węzełów.
        Zamiast tego usuwany jest najmniejszy krewny.
        """
        if node_children == 2:
            progeny = smallest_node(node.right)
            node.data = progeny.data
            self.delete(progeny)
            return

        # Wyreguluj wysokość i sprawdź równowagę drzewa.
        if node_parent:
            node_parent.tallness = 1 + max(self._get_height(node_parent.left), self._get_height(node_parent.right))
            self._inspect_deletion(node_parent)

    def _inspect_deletion(self, cur_node):
        """Zapewnia równowagę drzewa po usunięciu.

        Wywołuje _rebalance_node, jeśli zostanie wykryta nierównowaga.
        Wywołuje _inspect_insertion, aby zapewnić równowagę w drzewie.

        :param Rodzic usuniętego węzła.
        """
        if not cur_node:
            return

        left = self._get_height(cur_node.left)
        right = self._get_height(cur_node.right)

        if abs(left - right) > 1:
            y = self.taller_child(cur_node)
            x = self.taller_child(y)
            self._rebalance_node(cur_node, y, x)

        if cur_node.parent:
            self._inspect_insertion(cur_node, [])

    def taller_child(self, cur_node):
        """Znajduje wyższego z dzieci węzła.

        :param cur_node: Node. Węzeł do sprawdzenia.
        :return: Node. Element potomny curr_node o większej wysokości.
        """
        left = self._get_height(cur_node.left)
        right = self._get_height(cur_node.right)
        if left >= right:
            return cur_node.left
        return cur_node.right


class AVLTree(object):

    """

    Opakuje klasę Node. Metody wywołują odpowiednie metody klasy Node.

    """

    def __init__(self):
        """Drzewo jest reprezentowane przez węzeł główny, początkowo Brak."""
        self.root = None

    def __repr__(self):
        """Wyświetla tekstową strukturę drzewa.

        :return: str. Struktura dzewa.
        """
        if not self.root:
            return 'Dzewo puste. Proszę dodać elementy.'
        the_tree = '\n'
        nodes = [self._get_root()]
        cur_tallness = self.root.tallness
        space = ' ' * (40 - int(len(str(self.root.data))) // 2)
        buffer = ' ' * (60 - int(len(str(self.root.data))) // 2)
        while True:
            if all(n is None for n in nodes):
                break
            cur_tallness -= 1
            this_row = ' '
            next_row = ' '
            next_nodes = []
            for cur_node in nodes:
                if not cur_node:
                    this_row += '           ' + space
                    next_nodes.extend([None, None])
                if cur_node and cur_node.data is not Node:
                    this_row += f'{buffer}{str(cur_node.data)}{buffer}'
                if cur_node and cur_node.left:
                    next_nodes.append(cur_node.left)
                    next_row += space + '/' + space
                else:
                    next_nodes.append(None)
                    next_row += '       ' + space
                if cur_node and cur_node.right:
                    next_nodes.append(cur_node.right)
                    next_row += '\\' + space
                else:
                    next_nodes.append(None)
                    next_row += '       ' + space
            the_tree += (cur_tallness * '   ' + this_row + '\n' + cur_tallness * '   ' + next_row + '\n')
            space = ' ' * int(len(space) // 2)
            buffer = ' ' * int(len(buffer) // 2)
            nodes = next_nodes
        return the_tree

    def MinVal(self):
        if self.root == None:
            return None
        else:
            return self._MinVal(self.root)
    def _MinVal(self, data):
        "Idziemy do skrajnie lewego węzla"
        element=self.root
        while element.left:
            print(element.data)
            element=element.left
        return element.data

    def DeleteTree(self):
        if self.root == None:
            return None
        else:
            return self.deleteTree(self.root)
    def deleteTree(self, node):
        if node is not None:
            self.deleteTree(node.left)
            self.deleteTree(node.right)
            print(node.data)
            node.left = node.right = None
        else:
            self.root = None

    def MaxVal(self):
        if self.root==None:
            return None
        else:
            return self._MaxVal(self.root)
    def _MaxVal(self, data):
        element=self.root
        while element.right:
            print(element.data)
            element=element.right
        return element.data

    def Podzewo(self,root):

        if self.root == None:
            return
        else:
            return self._Podzewo(self.root,root,output=[])
    def _Podzewo(self,node,root,output=[]):
        if node is not None:
            output.append(node.data)
            if node.data==root:
                for i in range(len(output)):
                    output[i]=str(output[i])
                return print(' '.join(output[0:len(output)]))
            else:
                self._Podzewo(node.left,root,output)
                self._Podzewo(node.right,root,output)

    def _get_root(self, data=None):
        """Zwraca węzeł główny.

         Tworzy węzeł główny, jeśli jest wywoływany z Tree.insert, a drzewo jest puste.

        :param data: Jeśli podano, a drzewo jest puste, korzenie drzewa są ustanawiane z danymi.
        :return: Węzeł główny drzewa.
        """
        if not self.root:
            if data is not None:
                self.root = Node(data)
            else:
                print('Dzewo puste.')
                return

        else:
            while self.root.parent:
                self.root = self.root.parent

        return self.root

    def print_tree(self, order=None):
        """Interfejs użytkownika do drukowania drzewa.

         Wywołuje _print_tree z rootem z _get_root.
         Drukuje zamówienie wprowadzone przez użytkownika w celu poprawienia literówek itp.
         Zapewnia, że żądana kolejność drukowania jest ważna.

        :param order: 'in-order', 'pre-order', or 'post-order'
        :return: _print_tree
        """
        print(order)
        if not order or not any([order == 'pre-order', order == 'post-order', order == 'in-order']):
            return
        return self._print_tree(self._get_root(), order)

    def _print_tree(self, root, order=None):
        """Wywołuje metodę print_tree klasy Node.

        :param root: Węzeł główny
        :param order: 'in-order', 'pre-order', or 'post-order'
        :return: Node.print_tree
        """
        return root.print_tree(root, order)

    def height(self, print_result=False):
        """Interfejs użytkownika do znajdowania wysokości drzewa.

        Wywołuje _height z rootem z _get_root.
        Opcja drukowania wysokości na standardowe wyjście.

        :param print_result: Wyświetla wysokość na standardowym wyjściu, jeśli prawda.
        :return: _height
        """
        height = self._height(self._get_root())
        if print_result:
            print(height)
        return height

    def _height(self, root):
        """Wywołuje metodę wysokości klasy Node.

        :param root: Węzeł główny.
        :return: Node.height
        """
        return root.height(root, 0)

    def search(self, data, print_result=False):
        """Interfejs użytkownika dla metody wyszukiwania.

        :param print_result: Ustawić na True, aby wydrukować wyniki wyszukiwania.
        :param data: Dane do poszukiwania w drzewie.
        :return: _search
        """
        result = self._search(self._get_root(), data)

        if print_result:
            if result:
                print(f'{data} znaleziony.')
            else:
                print(f'{data} nie znaleziony.')

        return result

    def _search(self, root, data):
        """Wywołuje metodę wyszukiwania klasy Node.

        :param root: Główny węzeł
        :param data: Data do wyszukiwania w dzewie
        :return: Node.search
        """
        return root.search(root, data)

    def insert(self, data):
        """Interfejs użytkownika do wstawiania danych do drzewa.

        Wywołuje _insert z rootem dostarczonym przez _get_root.
        Pole danych dostarczone do _get_root zapewnia utworzenie korzenia drzewa przy pierwszym wstawieniu.

        :param data: Dane do wstawienia w dzewo.
        :return: _insert
        """
        return self._insert(self._get_root(data=data), data)

    def _insert(self, root, data):
        """Wywołuje metodę wstawiania klasy Node.

        :param root: Węzeł główny.
        :param data: Dane do wstawienia
        :return: Node.insert
        """
        return root.insert(root, data)


    def _find_node(self, cur_node, data):
        """Znajduje i zwraca węzeł z podanymi danymi, w przeciwnym razie zwraca None.

        :param cur_node: Węzeł główny z _get_root.
        :param data: Dane zawarte w węźle do znalezienia.
        :return: Węzeł zawierający dane, jeśli taki węzeł istnieje. W przeciwnym przupadku brak.
        """
        if cur_node and data == cur_node.data:
            return cur_node
        elif cur_node and data < cur_node.data:
            return self._find_node(cur_node.left, data)
        elif cur_node and data > cur_node.data:
            return self._find_node(cur_node.right, data)
        return None

    def delete(self, data):
        """Przekazuje root i dane do usunięcia do _delete.

        Wywołuje _delete z rootem z _get_root.
        :param data: Dane do usunięcia z drzewa.
        :return: _delete jeśli dane w drzewie, w przeciwnym przypadku None.
        """
        node = self._find_node(self._get_root(), data)

        if not node:
            print(f'{data} nie ma w dzewie, usunięcie niemożliwe.')
            return

        return self._delete(node)

    def _delete(self, node):
        """Wywołuje metodę usuwania klasy Node.

         Jeśli root ma zostać usunięty i nie ma dzieci, root jest ustawiony na None.
         Jeśli Node.delete zwraca węzeł, jest to nowy węzeł główny.

        :param node: Węzeł do usunięcia
        """
        if node == self.root and (not node.left and not node.right):
            self.root = None
            return self.root

        result = node.delete(node)

        if result:
            self.root = result

        return self.root



    def clear_tree(self):
        """Czyści dzewo.
        """
        print(self.root)
        self.root = None
        return self.root


tree = AVLTree()

def height(node):
    # Base Case : Tree is empty
    if node is None:
        return 0
    leftHeight = height(node.left)
    rightHeight = height(node.right)
    if leftHeight > rightHeight:
        return leftHeight + 1
    else:

        return rightHeight + 1
def isBalanced(root):
    # Base condition
    if root is None:
        return True

    # for left and right subtree height
    lh = height(root.left)
    rh = height(root.right)

    # allowed values for (lh - rh) are 1, -1, 0
    if (abs(lh - rh) <= 1) and isBalanced(
            root.left) is True and isBalanced(root.right) is True:
        return True
    return False
root=None
response=''
while response!="Exit":
    print("Choose option: ")
    print("show the tree")
    print("add items")
    print("remove items")
    print("find an item")
    print("in-order")
    print("pre-order")
    print("post-order")
    print("search for the element with the lowest and highest value (enter the appropriate Min or Max)")
    print("Subtree")
    print("Clear the tree")
    print("Finish")
    print()
    response=input()
    print()
    print()
    if response=="show the tree":
        print(tree)
        print()
        print()
    elif response=="add items":
        print("How many items do you want to add?")
        ilosc=input()
        elementy=[]
        if ilosc.isdigit() and int(ilosc)>0:
            for i in range(int(ilosc)):
                print(f"Enter {i+1} element: ")
                liczba=input()
                if liczba.isdigit() and int(liczba)>0:
                    elementy.append(int(liczba))
                else:
                    print("Incorrect data")
                    break
            if int(ilosc)==len(elementy):
                start_time=time.time()
                for i in range(int(ilosc)):
                    root=tree.insert(int(elementy[i]))
                    print(tree)
                    print(tree.print_tree('pre-order'))
                print(time.time()-start_time)
        else:
            print("Incorrect data")
        print()
        print()

    elif response=="random data":
        print("Enter the number of generated items: ")
        l = []
        start_time=time.time()
        try:
            tree.DeleteTree()
            n = int(input())
            if  n>0:
                j = 10 * n + 1
                for i in range(n):
                    j = random.randint(n - i, j - 1)
                    l = l + [j]
                start_time=time.time()
                for i in l:
                    tree.insert(i)
                print(f"{time.time()-start_time} second")

            else: print(f'{n} is not a positive number')
        except: print("Invalid number")
        print()
        print()

    elif response=="remove items":
        print("How many items do you want to delete?")
        ilosc = input()
        if ilosc.isdigit() and int(ilosc)> 0:
            for i in range(int(ilosc)):
                print("What item you want to delete?")
                liczba = input()
                if liczba.isdigit() and int(liczba) > 0:
                    root = tree.delete(int(liczba))
                else:
                    print("Incorrect data")
                    break
        else:
            print("Incorrect data")
        print()
        print()
    elif response=="in-order":
        start_time=time.time()
        try:
            print(tree)
            print(tree.print_tree(response))
        except:
            print("Empty tree")
        print(time.time()-start_time)
        print()
        print()
    elif response=="pre-order":
        try:
            print(tree)
            print(tree.print_tree(response))
        except: print("Empty tree")

        print()
        print()
    elif response=="post-order":
        try:
            print(tree)
            print(tree.print_tree(response))
        except:
            print("Empty tree")
        print()
        print()
    elif response=="Min":
        start_time=time.time()
        print(tree.MinVal())
        print(time.time()-start_time)
        print()
        print()
    elif response=="Max":
        print(tree)
        print(tree.MaxVal())
        print()
        print()
    elif response=="Subtree":
        print("Enter the item: ")
        element=input()
        if element.isdigit() and int(element)>0:
            try:
                if tree.search(int(element))==True:
                    print(tree.Podzewo(int(element)))
            except: print("Item not found")
        else: print("Incorrectly typed item, please try again")
        print()
        print()
    elif response=="Clear the tree":
        print(tree.DeleteTree())
        print(tree)
        print()
        print()
    elif response=="Finish":
        print("The program has ended")
        exit()
    elif response=="check":
        print(isBalanced(tree.root))
    else:
        print("It is not possible")
        print()




