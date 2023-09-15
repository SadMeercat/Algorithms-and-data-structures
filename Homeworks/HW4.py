import enum


class Color(enum.Enum):
    red = 'Red'
    black = 'Black'


class Node:

    def __init__(self):
        self.left = None
        self.right = None
        self.color = Color.red


class RedBlackTree:
    def __init__(self):
        self.root = None
        self.counter = 0
    def add(self, value):
        if self.root is not None:
            result = self.add_node(self.root, value)
            self.root = self.rebalance(self.root)
            self.root.color = Color.black
            return result
        else:
            self.root = Node()
            self.root.color = Color.black
            self.root.value = value

    def add_node(self, node, value):
        if node.value == value:
            return False
        else:
            if (node.value > value):
                if node.left != None:
                    result = self.add_node(node.left, value)
                    node.left = self.rebalance(node.left)
                    return result
                else:
                    node.left = Node()
                    node.right = Color.red
                    node.left.value = value
                    return True
            else:
                if node.right != None:
                    result = self.add_node(node.right, value)
                    node.right = self.rebalance(node.right)
                    return result
                else:
                    node.right = Node()
                    node.right.color = Color.red
                    node.right.value = value
                    return True

    def deleteNode(self, root, key):

        # Указатель для хранения родителя текущего узла
        parent = None

        # запускается с корневого узла
        curr = root

        # Ключ поиска и установка его родительского указателя
        while curr and curr.value != key:

            # обновляет родителя до текущего узла
            parent = curr

            # если данный ключ меньше текущего узла, перейти к левому поддереву;
            # иначе перейти к правому поддереву
            if key < curr.value:
                curr = curr.left
            else:
                curr = curr.right

        # возврат, если ключ не найден в дереве
        if curr is None:
            return root

        # Случай 1: удаляемый узел не имеет потомков, т. е. это конечный узел.
        if curr.left is None and curr.right is None:

            # если удаляемый узел не является корневым узлом, то установить его
            # родительский левый/правый дочерний в None
            if curr != root:
                if parent.left == curr:
                    parent.left = None
                else:
                    parent.right = None

            # если дерево имеет только корневой узел, установите для него значение None.
            else:
                root = None

        # Случай 2: удаляемый узел имеет два дочерних элементов
        elif curr.left and curr.right:

            # находит свой неупорядоченный узел-преемник
            successor = self.getMinimumKey(curr.right)

            # сохраняет значение преемника
            val = successor.value

            # рекурсивно удаляет преемника.
            self.deleteNode(root, successor.value)

            # копирует значение преемника в текущий узел
            curr.value = val

        # Случай 3: удаляемый узел имеет только одного потомка
        else:

            # выбирает дочерний узел
            if curr.left:
                child = curr.left
            else:
                child = curr.right

            # если удаляемый узел не является корневым узлом, установить его родительский
            # своему потомку
            if curr != root:
                if curr == parent.left:
                    parent.left = child
                else:
                    parent.right = child

            # если удаляемый узел является корневым узлом, то установите корень в дочерний
            else:
                root = child
        self.rebalance(self.root)

    def getMinimumKey(self, curr):
        while curr.left:
            curr = curr.left
        return curr

    def rebalance(self, node: Node):
        result = node
        need_rebalance = True
        while need_rebalance:
            need_rebalance = False
            if result.right != None and result.right.color == Color.red and (result.left == None or result.left.color == Color.black):
                need_rebalance = True
                result = self.right_swap(result)
            if result.left != None and result.left.color == Color.red and result.left.left != None and result.left.left.color == Color.red:
                need_rebalance = True
                result = self.right_swap(result)
            if result.left != None and result.left.color == Color.red and result.right != None and result.right.color == Color.red:
                need_rebalance = True
                self.color_swap(result)
        return result

    def left_swap(self, node: Node):
        left_child = node.left
        between_child = node.right
        left_child.right = node
        node.left = between_child
        left_child.color = node.color
        node.color = Color.red
        return left_child

    def right_swap(self, node: Node):
        right_child = node.right
        between_child = right_child.left
        right_child.left = node
        node.right = between_child
        right_child.color = node.color
        node.color = Color.red
        return right_child

    def color_swap(self, node: Node):
        node.right.color = Color.black
        node.left.color = Color.black
        node.color = Color.red

    def find_count(self, node):
        self.counter += 1
        if node.left is not None:
            self.find_count(node.left)
        if node.right is not None:
            self.find_count(node.right)

        return self.counter

    def print_tree(self, node, indent):
        if node is None:
            return

        spacing = "\t" * indent
        self.print_tree(node.right, indent + 4)
        print(spacing + str(node.value))
        self.print_tree(node.left, indent + 4)


if __name__ == '__main__':
    tree = RedBlackTree()
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(8)
    print('Count nodes: ', tree.find_count(tree.root))
    tree.counter = 0
    print('---------------------------')
    tree.print_tree(tree.root, 0)
    tree.deleteNode(tree.root, 6)
    print('---------------------------')
    tree.print_tree(tree.root, 0)