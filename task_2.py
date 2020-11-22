"""
Задание 2.**

Доработайте пример структуры "дерево",
рассмотренный на уроке.

Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии с требованиями для бинарного дерева)

Поработайте с доработанной структурой, позапускайте на реальных данных.
"""

class BTree:
    def __init__(self, root):
        self.root = root
        self.lchild = None
        self.rchild = None


    def __str__(self):
        return str(self.root)

    def insert_l(self, new):
        try:

            if self.root >= new:
                if self.lсhild is None:
                    self.lchild = BTree(new)

                else:

                    tree_obj = BTree(new)

                    tree_obj.lchild = self.lchild
                    self.lchild = BTree
            else:
                raise Exception('Ошибка')
        except Exception as e:
            print(e)


    def insert_r(self, new):
        try:
            if self.root <= new:

                if self.rchild is None:


                    self.rchild = BTree(new)

                else:

                    tree = BTree(new)

                    tree.rchild = self.rchild
                    self.rchild = tree
            else:
                raise Exception('Ошибка')
        except Exception as e:
            print(e)


    def get_rchild(self):
        try:
            return self.rchild
        except AttributeError:
            print('Ошибка')


    def get_lchild(self):
        try:
            return self.lchild
        except AttributeError:
            print('Ошибка')


    def set_root_val(self, obj):
        self.root = obj


    def get_root_val(self):
        try:
            return self.root
        except AttributeError:
            print('Ошибка')


r = BTree(8)
print(r.get_root_val())
print(r.get_lchild())
r.insert_left(4)
print(r.get_lchild())
print(r.get_lchild().get_root_val())
r.insert_right(12)
print(r.get_rchild())
print(r.get_rchild().get_root_val())
r.get_rchild().set_root_val(16)
print(r.get_rchild().get_root_val())
