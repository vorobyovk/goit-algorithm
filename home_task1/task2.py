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
print(f"'А роза упала на лапу Азора' є паліндромом: {is_palindrome_deque('А роза упала на лапу Азора')}")
print(f"'Race car' є паліндромом: {is_palindrome_deque('Race car')}")
print(f"'hello' є паліндромом: {is_palindrome_deque('hello')}")
print(f"'Madam' є паліндромом: {is_palindrome_deque('Madam')}")
print(f"'12321' є паліндромом: {is_palindrome_deque('12321')}")
print(f"'No lemon, no melon.' є паліндромом: {is_palindrome_deque('No lemon, no melon.')}")
print(f"'' (порожній рядок) є паліндромом: {is_palindrome_deque('')}")
print(f"'a' є паліндромом: {is_palindrome_deque('a')}")