from collections import deque

def is_palindrome_deque(input_string):    
    # Готуємо рядок: видаляємо пробіли та переводимо в нижній регістр
    formatted_string = ''.join(input_string.split()).lower()    
    # Створюємо двосторонню чергу з символів підготовленого рядка
    char_deque = deque(formatted_string)    
    is_palindrome = True
    while len(char_deque) > 1:
        # Порівнюємо символи з обох кінців черги
        if char_deque.popleft() != char_deque.pop():
            is_palindrome = False
            break            
    return is_palindrome

# Приклади використання:
Phrase1 = "А роза упала на лапу Азора"
Phrase2 = "Race car"
Phrase3 = "Hello, World!"
Phrase4 = "12345"
Phrase5 = "12321"
print(f" {Phrase1} є паліндромом: {is_palindrome_deque(Phrase1)}")
print(f" {Phrase2} є паліндромом: {is_palindrome_deque(Phrase2)}")
print(f" {Phrase3} є паліндромом: {is_palindrome_deque(Phrase3)}")
print(f" {Phrase4} є паліндромом: {is_palindrome_deque(Phrase4)}")
print(f" {Phrase5} є паліндромом: {is_palindrome_deque(Phrase5)}")