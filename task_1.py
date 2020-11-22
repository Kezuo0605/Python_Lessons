"""
Задание 1.
Реализуйте кодирование строки "по Хаффману".
У вас два пути:
1) тема идет тяжело? тогда вы можете, опираясь на пример с урока, сделать свою версию алгоритма
Разрешается и приветствуется изменение имен переменных, выбор других коллекций, различные изменения
и оптимизации.
КОПИПАСТ ПРИМЕРА ПРИНИМАТЬСЯ НЕ БУДЕТ!
2) тема понятна? постарайтесь сделать свою реализацию.
Вы можете реализовать задачу, например, через ООП или предложить иной подход к решению.

ВНИМАНИЕ: примеры заданий будут размещены в последний день сдачи.
Но постарайтесь обойтись без них.
"""
class BinaryTree:
    def __init__(self, robj):
        self.root = robj
        self.lchild = None
        self.right_child = None

    def ileft(self, new):
        if self.lchild == None:
            self.lchild = BinaryTree(new)
        else:
            tree = BinaryTree(new)
            tree.lchild = self.lchild
            self.lchild = tree

    def iright(self, new):
        if self.rchild == None:
            self.rchild = BinaryTree(new)
        else:
            tree = BinaryTree(new)
            tree.rchild = self.rchild
            self.rchild = tree

    def get_rchild(self):
        return self.rchild
    def get_lchild(self):
        return self.lchild
    def root(self, obj):
        self.root = obj
    def root(self):
        return self.root


r = BinaryTree(8)
print(r.root())
print(r.get_lchild())
r.insert_left(4)
print(r.get_lchild())
print(r.get_lchild().get_root())
r.insert_right(12)
print(r.get_rchild())
print(r.get_rchild().get_root())
r.get_rchild().set_root(16)
print(r.get_rchild().get_root())
