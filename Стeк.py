class Stack:
    def __init__(se): #Создаём стек
        se.items = []  

    def isEmpty(se):
        return se.items == [] #Проверяем стек на пустоту

    def push(se, item):
        se.items.append(item) #Добавляем элемент в стек

    def pop(se):
        return se.items.pop() #Удаляем элемент из стека

    def peek(se):
        return se.items[len(se.items) - 1] #Смотрим на стек

    def size(se):
        return len(se.items) #Узнаём размер стека

a = Stack()
print(a.isEmpty()) 
a.push(5)
print(a.isEmpty())
a.push(6)
print(a.peek())
print(a.size())
a.push(4)
print(a.pop())
print(a.size())
