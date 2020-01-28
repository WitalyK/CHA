# -*- coding: utf-8 -*-
'''
Задание 6.3

Создать функцию queue, которая работает как очередь.
После вызова функции queue, должна быть доступна возможность обращаться к
атрибутам:
* put - добавляет элемент в очередь
* get - удаляет элемент с начала очереди и возвращает None, если элементы закончились

Пример работы функции queue:

In [2]: tasks = queue()

In [3]: tasks.put('a')

In [4]: tasks.put('b')

In [5]: tasks.put('c')

In [6]: tasks.get()
Out[6]: 'a'

In [7]: tasks.get()
Out[7]: 'b'

In [8]: tasks.get()
Out[8]: 'c'

In [9]: tasks.get()

In [10]: tasks.get()
'''
def queue():
    sum = []
    def put(item):
        nonlocal sum
        sum.append(item)
    def get():
        nonlocal sum
        if not sum:
            return None
        else:
            return sum.pop(0)
    queue.put = put
    queue.get = get
    return queue
    

# don't run on import
if __name__ == "__main__":
    tasks = queue()
    tasks.put('a')
    tasks.put('b')
    tasks.put('c')
    print(tasks.get())
    print(tasks.get())
    print(tasks.get())
    print(tasks.get())
    print(tasks.get())
