
class Node:


    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:

    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("Стек пуст, нечего извлекать")

        popped_value = self.top.value
        self.top = self.top.next
        self.size -= 1
        return popped_value

    def peek(self):

        if self.is_empty():
            raise IndexError("Стек пуст, нечего смотреть")

        return self.top.value

    def is_empty(self):

        return self.top is None


stack_1 = Stack()
stack_input = input("Введите начальные элементы стека через пробел (или нажмите Enter для пустого стека): ")
elements = stack_input.split()

for element in elements:

    stack_1.push(element)
    
while True:
    
    print("\n--- МЕНЮ ---")
    print("1. Добавить элемент (push)")
    print("2. Извлечь элемент (pop)")
    print("3. Показать верхний элемент (peek)")
    print("4. Выход")
    choice = input("Выберите пункт меню (1-4): ")

    if choice == '1':

        element = input("Введите значение для добавления в стек: ")
        stack_1.push(element)
        
    elif choice == '2':
        
        try:
            
            popped_val = stack_1.pop()
            print(f"Извлеченный элемент: {popped_val}")

        except IndexError as e:
            
            print(f"Ошибка: {e}")
            
    elif choice == '3':
        
        try:
            
            peeked_val = stack_1.peek()
            print(f"Верхний элемент стека: {peeked_val}")

        except IndexError as e:

            print(f"Ошибка: {e}")
            
    elif choice == '4':
        
        print("Выход из программы. До свидания!")
        break
        
    else:
        
        print("Ошибка: нет такого пункта меню. Пожалуйста, введите число от 1 до 4.")
