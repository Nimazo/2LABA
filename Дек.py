class Deque:
    def __init__(se):
        se.items = [] #создаём дек

    def isEmpty(se):
        return se.items == [] #Проверяем дек на пустоту

    def addFront(se, item):
        se.items.append(item) #Добавляем элемент в конец

    def addRear(se, item):
        se.items.insert(0,item) #Добавляем элемент в начало

    def removeFront(se):
        return se.items.pop() #Удаляем элемент из конца

    def removeRear(se):
        return se.items.pop(0) #Удаляем элемент из начала

    def size(se):
        return len(se.items) #проверяем размер дека

    def smotim(se):    #Смотрим в очередь
        print(se.items)

    def __del__(self):  # Деструктор класса
        print ('Удалено')


a=Deque()
print(a.isEmpty())
a.addRear(1)
a.addRear(2)
a.addFront(3)
a.addFront(4)
print(a.smotim())
print(a.size())
print(a.isEmpty())
print(a.removeRear())
print(a.removeFront())
print(a.smotim())
del a
