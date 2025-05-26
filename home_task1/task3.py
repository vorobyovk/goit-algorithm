def check_brackets_symmetry(expression): 
    stack = []
    brackets_map = {")": "(", "]": "[", "}": "{"}
    opening_brackets = set(brackets_map.values()) # {"(", "[", "{"}
    closing_brackets = set(brackets_map.keys())   # {")", "]", "}"}

    for char in expression:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack: # Якщо стек порожній, а зустріли закриваючу дужку
                return f"{expression}: Несиметрично (зайва закриваюча дужка)"
            # Перевіряємо, чи відповідає остання відкриваюча дужка поточній закриваючій
            if stack[-1] == brackets_map[char]:
                stack.pop()
            else:
                # Невідповідність типів дужок
                return f"{expression}: Несиметрично (невідповідність типів дужок: {stack[-1]} та {char})"
        # Інші символи (цифри, оператори, пробіли) ігноруються
    if not stack: # Якщо стек порожній після проходження всього рядка
        return f"{expression}: Симетрично"
    else:
        # Якщо в стеку залишились відкриваючі дужки
        return f"{expression}: Несиметрично (незакрито {len(stack)} дужок(ки))"

# Приклади використання:
print(check_brackets_symmetry("( ){[ 1 ]( 1 + 3 )( ){ }}")) # Виправлено для очікуваного "Симетрично"
print(check_brackets_symmetry("( ( ( )"))
print(check_brackets_symmetry("( 11 }"))
print(check_brackets_symmetry("((()))"))
print(check_brackets_symmetry("([)]"))
print(check_brackets_symmetry("{[]}"))
print(check_brackets_symmetry("]"))
print(check_brackets_symmetry("() { [ ] ( ) ( ) { } }")) # Ваш приклад з опису
print(check_brackets_symmetry("( 23 ( 2 - 3);")) # Ваш приклад з опису