import numpy as np
from queue import Queue
import random

# arr = np.array([1, 2, 3, 4, 5])
# print(arr) # Output: array([1, 2, 3, 4, 5])

# class Stack:
#   def __init__(self):
#     self.stack = []
# # Додавання елемента до стеку
#   def push(self, item):
#     self.stack.append(item)
# # Видалення елемента зі стеку
#   def pop(self):
#     if len(self.stack) < 1:
#       return None
#     return self.stack.pop()
# # Перевірка, чи стек порожній
#   def is_empty(self):
#     return len(self.stack) == 0
# # Перегляд верхнього елемента стеку без його видалення
#   def peek(self):
#     if not self.is_empty():
#       return self.stack[-1]

# s = Stack()
# s.push('a')
# s.push('b')
# s.push('c')
# print(s.peek())# Output: 'c'
# print(s.pop())# Output: 'c'
# print(s.peek())# Output: 'b'
# print(s.is_empty())# Output: False



class Client:
  def __init__(self, name):
    self.name = name
    self.operations = random.randint(1, 5)# Випадкова кількість операцій

class Bank:
  def __init__(self):
    self.clients = Queue()

  def new_client(self, client):
    self.clients.put(client)

  def serve_clients(self):
    while not self.clients.empty():
      current_client = self.clients.get()
      print(f"Обслуговуємо клієнта {current_client.name} з {current_client.operations} операцій")
   # Тут можна додати час обслуговування та іншу логіку

# Створюємо банк
bank = Bank()
# Додаємо клієнтів
for i in range(5):
  bank.new_client(Client(f"Client-{i}"))
# Обслуговуємо клієнтів
bank.serve_clients()
