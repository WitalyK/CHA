# -*- coding: utf-8 -*-
'''
Задание 4.5

Создать примесь InheritanceMixin с двумя методами:

* subclasses - отображает дочерние классы
* superclasses - отображает родительские классы

Методы должны отрабатывать и при вызове через класс и при вызове
через экземпляр:
In [2]: A.subclasses()
Out[2]: [__main__.B, __main__.D]

In [3]: A.superclasses()
Out[3]: [__main__.A, __main__.InheritanceMixin, object]

In [4]: a.subclasses()
Out[4]: [__main__.B, __main__.D]

In [5]: a.superclasses()
Out[5]: [__main__.A, __main__.InheritanceMixin, object]

В задании заготовлена иерархия классов, надо сделать так, чтобы у всех
этих классов повились методы subclasses и superclasses.
Определение классов можно менять.
'''


class InheritanceMixin:
    @classmethod
    def subclasses(cls):
        return cls.__subclasses__()

    @classmethod
    def superclasses(cls):
        return list(cls.__mro__)


class A(InheritanceMixin):
    pass


class B(A):
    pass


class C(InheritanceMixin):
    pass


class D(A, C):
    pass


# don't run on import
if __name__ == "__main__":
    a = A()
    print(A.subclasses())
    print(A.superclasses())
    print(a.subclasses())
    print(a.superclasses())
    b = B()
    print(B.subclasses())
    print(B.superclasses())
    print(b.subclasses())
    print(b.superclasses())
    c = C()
    print(C.subclasses())
    print(C.superclasses())
    print(c.subclasses())
    print(c.superclasses())
    d = D()
    print(D.subclasses())
    print(D.superclasses())
    print(d.subclasses())
    print(d.superclasses())
