class Stack:
     def __init__(se):
         se.items = []
         
     def isEmpty(se):
         return se.items == []

     def push(se, item):
         se.items.append(item)

     def pop(se):
         return se.items.pop()

     def peek(se):
         return se.items[len(se.items)-1]

     def size(se):
         return len(se.items)

     def smotim(se):    
        print(se.items)
        
t = open('Скобки.txt')
t = t.read()
t = t.split(' ')
s = Stack()
w = Stack()
m = Stack()
b = Stack()
l=0


for i in t:
    l+=1

    if (i == '('):
       if (s.isEmpty() == False):
           if (s.peek() == '('):
               j=w.peek()
               w.pop()
               m.push(j)
               
       w.push(l)  
       s.push(i)

    if (i == ')'):
        if (s.peek() == ')'):
            w.push(l)
            k=w.peek()
            w.pop()
            b.push(k)
       
        if (s.peek() == '('):
            w.push(l)
        s.push(i)
    if (w.size() == 2):
        print(w.smotim())
        w.pop()
        w.pop()
u=0
e = m.size()

while u<e:
    u+=1
    print('[', m.peek(),',', b.peek(), ']')
    b.pop()
    m.pop()
    




