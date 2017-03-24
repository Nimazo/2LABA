class Queue:
    def __init__(se):
        se.items = [] #Создали очередь
    def isEmpty(se):
        return se.items == []  #Проверяем на пустоту

    def enqueue(se, item):
        se.items.insert(0,item) #Добавляем элемент в очередь
        print(se.items)

    def dequeue(se):
        return se.items.pop() #Удаляем элемент из очереди

    def smotim(se):    #Смотрим в очередь
        print(se.items)

    def size(se):
        return len(se.items) #Промеряем размер очереди

    def __del__(self):  # Деструктор класса
        print ('Удалено')

a = Queue()
print(a.isEmpty())
a.enqueue('2')
a.enqueue('3')
a.enqueue('Эй, красавица')
a.enqueue('4')
print(a.isEmpty())
print(a.size())
print(a.dequeue())
print(a.dequeue())
print(a.smotim())
print(a.size())
del a


