import time
import sys
class Tree:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val
        self.tallness = 1

    def size(self):

        size = 0
        if self != None:
            size += 1
            if self.left != None:
                size += self.left.size()
            if self.right != None:
                size += self.right.size()
        return size
    def add(self, val):
        if not self.val:
            self.val = val
            return
        if self.val == val:
            return
        if val < self.val:
            if self.left:
                self.left.add(val)
                return
            self.left = Tree(val)
            return
        if self.right:
            self.right.add(val)
            return
        self.right = Tree(val)

    def find(self, val):
        if self is not None:
            return self._find(val, self)
        else:
            return None
    def _find(self, val, node):
        if val == node.val:
            return node
        elif (val < node.val and node.left is not None):
            return self._find(val, node.left)
        elif (val > node.val and node.right is not None):
            return self._find(val, node.right)


    def delete_postorder(self):
        if self.left is not None:
            self.left.delete_postorder()
        if self.right is not None:
            self.right.delete_postorder()
        if self.val is not None:
            print(self.val)
            self.left=self.right=None
            self.val = None
        return

    def delete(self, val):
        if self == None or self.val == None:
            return self
        if val < self.val:
            self.left = self.left.delete(val)
            return self
        if val > self.val:
            self.right = self.right.delete(val)
            return self
        if self.right == None:
            return self.left
        if self.left == None:
            return self.right
        min_larger_node = self.right
        while min_larger_node.left:
            min_larger_node = min_larger_node.left
        self.val = min_larger_node.val
        self.right = self.right.delete(min_larger_node.val)
        return self

    def inorder(self, vals):
        if self.left is not None:
            self.left.inorder(vals)
        if self.val is not None:
            vals.append(self.val)
        if self.right is not None:
            self.right.inorder(vals)
        return vals

    def preorder(self, vals):
        if self.val is not None:
            vals.append(self.val)
        if self.left is not None:
            self.left.preorder(vals)
        if self.right is not None:
            self.right.preorder(vals)
        return vals

    def postorder(self, vals):
        if self.left is not None:
            self.left.postorder(vals)
        if self.right is not None:
            self.right.postorder(vals)
        if self.val is not None:
            vals.append(self.val)
        return vals

    def Podzewo(self,vals,output):
        if self.val is not None:
            try:
                output.index(int(vals))>=0
            except: output.append(self.val)
        if self.left is not None:
            self.left.Podzewo(vals,output)
        if self.right is not None:
            self.right.Podzewo(vals,output)
        return output

    def repr(self):
        """Wyświetla tekstową strukturę drzewa.

        :return: str. Struktura dzewa.
        """
        if not self:
            return 'Dzewo puste. Proszę dodać elementy.'
        the_tree = '\n'
        nodes = [self]
        cur_tallness = self.tallness
        space = ' ' * (40 - int(len(str(self.val))) // 2)
        buffer = ' ' * (60 - int(len(str(self.val))) // 2)
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
                if cur_node and cur_node.val is not Tree:
                    this_row += f'{buffer}{str(cur_node.val)}{buffer}'
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
class BST_Tree(object):
    def __init__(self, val=None):
        self.root = Tree()

    def getRoot(self):
        return self.root

    def DSW(self):
        if None != self.root:
            self.createBackbone()  # effectively: createBackbone( self.root)
            self.createPerfectBST()

    def createBackbone(self):
        grandParent = None
        parent = self.root
        leftChild = None

        while None != parent:
            leftChild = parent.left
            if None != leftChild:
                grandParent = self.rotateRight(grandParent, parent, leftChild)
                parent = leftChild
            else:
                grandParent = parent
                parent = parent.right

        # =======================================================================
        #   Before      After
        #    Gr          Gr
        #     \           \
        #     Par         Ch
        #    /  \        /  \
        #   Ch   Z      X   Par
        #  /  \            /  \
        # X    Y          Y    Z
        # =======================================================================

    def rotateRight(self, grandParent, parent, leftChild):
        if None != grandParent:
            grandParent.right = leftChild
        else:
            self.root = leftChild

        parent.left = leftChild.right
        leftChild.right = parent
        return grandParent

    def createPerfectBST(self):
        n = self.root.size()

        # m = 2^floor[lg(n+1)]-1, ie the greatest power of 2 less than n: minus 1
        m = self.greatestPowerOf2LessThanN(n + 1) - 1
        self.makeRotations(n - m)

        while m > 1:
            m //= 2
            self.makeRotations(m)

    def greatestPowerOf2LessThanN(self, n):
        x = self.MSB(n)  # MSB
        return (1 << x)  # 2^x

        # =======================================================================
        # Time complexity: log(n)
        # return the index of most significant set bit: index of
        # least significant bit is 0
        # =======================================================================

    def MSB(self, n):
        ndx = 0
        while 1 < n:
            n = (n >> 1)
            ndx += 1
        return ndx

    def makeRotations(self, bound):
        grandParent = None
        parent = self.root
        child = self.root.right
        while bound > 0:
            try:
                if None != child:
                    self.rotateLeft(grandParent, parent, child)
                    grandParent = child
                    parent = grandParent.right
                    child = parent.right
                else:
                    break
            except AttributeError:  # TypeError
                break
            bound -= 1

    def rotateLeft(self, grandParent, parent, rightChild):
        if None != grandParent:
            grandParent.right = rightChild
        else:
            self.root = rightChild

        parent.right = rightChild.left
        rightChild.left = parent

def height(node):
    if node is None:
        return 0
    leftHeight = height(node.left)
    rightHeight = height(node.right)
    if leftHeight > rightHeight:
        return leftHeight + 1
    else:

        return rightHeight + 1

def minValue(node):
    current = node
    print("Śćieżka do minimalnej wartości:")
    while (current.left is not None):
        print(current.val)
        current = current.left

    print("Minimalna wartość: ")
    return current.val


def maxValue(node):
    current = node
    print("Śćieżka do maksymalnej wartości:")
    # loop down to find the lefmost leaf
    while (current.right is not None):
        print(current.val)
        current = current.right
    print("Maksymalna wartość: ")
    return current.val

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
import random
tree = BST_Tree()
print()

root=None
response=''
while response!="Wyjść":
    print("Co chcesz zrobić z drzewem: ")
    print("pokazać drzewo")
    print("losowe dane")
    print("dodać elementy")
    print("usunąć elementy")
    print("znaleźć element")
    print("in-order")
    print("pre-order")
    print("post-order")
    print("wyszukać element o najmniejszej i największej wartości (wpisz Min lub Max odpowiednie)")
    print("Poddrzewo")
    print("Wyczyść drzewo")
    print("Zakończ")
    print("Zrównoważyć")
    print()
    response=input()
    print()
    print()
    if response=="pokazać drzewo":
        print(tree.root.repr())
        print((height(tree.root.left)))
        print()
        print()

    elif response=="dodać elementy":
        print("Ile elementów chcesz dodać?")
        ilosc=input()
        elementy=[]
        if ilosc.isdigit() and int(ilosc)>0:
            for i in range(int(ilosc)):
                print(f"Wpisz {i+1} element: ")
                liczba=input()
                if liczba.isdigit() and int(liczba)>0:
                    elementy.append(int(liczba))
                else:
                    print("Nieprawidlowe dane")
                    break
            if int(ilosc)==len(elementy):
                start_time=time.time()
                for i in range(int(ilosc)):
                    tree.root.add(elementy[i])
                    print(tree.root.preorder([]))
                print(time.time()-start_time)
        else:
            print("Nieprawidlowe dane")
        print()
        print()

    elif response=="losowe dane":
        print("Wpisz ilość generowanych elementów: ")
        l = []
        n = int(input())
        try:
            tree.root.delete_postorder()
            start_time = time.time()
            if  n>0:
                j = 10 * n + 1
                for i in range(n):
                    j = random.randint(n - i, j - 1)
                    l = l + [j]
                print(len(l))
                for i in l:
                    tree.root.add(i)
            else: print(f'{n} nie jest liczbą dodatnią')
        except:
            print("Nieprawidlowa liczba")
        print(time.time() - start_time)
        print()
        print()

    elif response=="usunąć elementy":
        print("Ile elementów chcesz usunąć?")
        ilosc = input()
        if ilosc.isdigit() and int(ilosc)> 0:
            for i in range(int(ilosc)):
                print("Jaki element chcesz usunąć?")
                liczba = input()
                if liczba.isdigit() and int(liczba) > 0:
                    tree.root.delete(int(liczba))
                else:
                    print("Nieprawidlowe dane")
                    break
        else:
            print("Nieprawidlowe dane")
        print()
        print()
    elif response=="in-order":
        start_time=time.time()
        try:
            print(tree.root.inorder([]))
        except:
            print("Drzewo puste")
        print(time.time()-start_time)
        print()
        print()
    elif response=="pre-order":
        try:
            print(tree.root.preorder([]))
        except: print("Drzewo puste")

        print()
        print()
    elif response=="post-order":
        try:
            print(tree.root.postorder([]))
        except:
            print("Drzewo puste")
        print()
        print()
    elif response=="Min":
        start_time=time.time()
        print(minValue(tree.root))
        print(time.time()-start_time)
        print()
        print()
    elif response=="Max":
        print(maxValue(tree.root))
        print()
        print()
    elif response=="Zakończ":
        print("Program zakończony")

        exit()
    elif response=="Poddrzewo":
        print("Wpisz element: ")
        element=input()
        if element.isdigit() and int(element)>0:
            try:
                print(tree.root.Podzewo(element,[]))

            except: print("Element nie znaleziony")
        else: print("Nieprawidlowo wpisany element, spróbuj ponownie")
        print()
        print()
    elif response=="Wyczyść drzewo":
        print(tree.root.delete_postorder())
        print()
        print()
    elif response=="Zrównoważyć":
        print(tree.root.preorder([]))
        start_time = time.time()
        try:
            tree.DSW()
        except: print("RecursionError: maximum recursion depth exceeded in comparison")
        print(tree.root.preorder([]))
        print(f"{time.time() - start_time} second")
    else:
        print("Nie ma takiej możliwości")
        print()
