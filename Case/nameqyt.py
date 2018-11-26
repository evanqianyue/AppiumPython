class Test():
    def __init__(self, a, b):
        self.a = int(a)
        self.b = int(b)

    def print_out(self):
        print("print_out:", self.a + self.b)

    @classmethod
    def classmethod_sum(cls, a, b):
        cls.a = int(a)
        cls.b = int(b)
        print('classmethod_sum:', cls.a + cls.b)

    @staticmethod
    def staticmethod_sum(a, b):
        print("staticmethod_sum:", a + b)

    @classmethod
    def list_to_num(cls, list_num):
        print(type(cls(list_num[0], list_num[1])))  # <class '__main__.Test'>
        return cls(list_num[0], list_num[1])


S = Test(1, 2)
S.print_out()

Test.classmethod_sum(2, 2)
Test.staticmethod_sum(2, 3)

V = Test.list_to_num([3, 4])
V.print_out()


