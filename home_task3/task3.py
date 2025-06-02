def draw_rods(rods_state: dict, num_disks_total: int):
    if num_disks_total == 0:
        print("Немає дисків для відображення.")
        # Простий вивід для порожнього випадку
        print("  |     |     |  ")
        print(" ---   ---   --- ")
        print("  A     B     C  ")
        print()
        return
    # Визначаємо максимальну ширину для відображення диска
    # Наприклад, для диска N, представлення буде (N-1)*'=' + str(N) + (N-1)*'='
    s_largest_disk_val = str(num_disks_total)
    # Ширина найбільшого диска (наприклад, для 3: "==3==" -> 5; для 10: "=========10=========" -> 20)
    max_content_width = (num_disks_total - 1) + len(s_largest_disk_val) + (num_disks_total - 1)
    # Гарантуємо, що ширина хоча б 1 (для символу '|')
    if max_content_width < 1:
        max_content_width = 1
    for height_level in range(num_disks_total, 0, -1):
        line_parts = []
        for rod_char in ['A', 'B', 'C']:
            rod_disks = rods_state[rod_char]  # Диски на цьому стрижні: [дно, ..., вершина]
            current_stack_height_on_rod = len(rod_disks)            
            display_segment = ""
            # Чи є диск на цьому стрижні на поточній висоті `height_level`?
            # (height_level рахується знизу, 1 - найнижчий можливий диск)
            if height_level <= current_stack_height_on_rod:
                # Так, є диск. Його значення - rod_disks[height_level - 1]
                disk_value = rod_disks[height_level - 1]
                s_disk_value = str(disk_value)                
                # Кількість символів '=' з кожного боку від числа
                # Для диска 1: 0. Для диска D: D-1.
                num_equals_padding = disk_value - 1                
                disk_visual_representation = ("=" * num_equals_padding) + s_disk_value + ("=" * num_equals_padding)
                display_segment = disk_visual_representation.center(max_content_width)
            else:
                # Немає диска на цьому рівні для цього стрижня
                display_segment = "|".center(max_content_width)
            line_parts.append(display_segment)
        print("  ".join(line_parts)) # Два пробіли між стрижнями
    # Друк основи стрижнів
    base_segment = "-" * max_content_width
    print("  ".join([base_segment] * 3))    
    # Друк міток стрижнів
    labels = [char.center(max_content_width) for char in ['A', 'B', 'C']]
    print("  ".join(labels))
    print() # Додатковий порожній рядок для кращого візуального розділення

def solve_hanoi(num_disks_to_move: int, source_rod: str, destination_rod: str, auxiliary_rod: str, rods_state: dict, total_disks_for_drawing: int):    
    if num_disks_to_move == 1:
        disk = rods_state[source_rod].pop()
        rods_state[destination_rod].append(disk)
        print(f"Перемістити диск з {source_rod} на {destination_rod}: {disk}")
        print(f"Проміжний стан: {rods_state}")
        draw_rods(rods_state, total_disks_for_drawing)
    else:
        solve_hanoi(num_disks_to_move - 1, source_rod, auxiliary_rod, destination_rod, rods_state, total_disks_for_drawing)
        disk = rods_state[source_rod].pop()
        rods_state[destination_rod].append(disk)
        print(f"Перемістити диск з {source_rod} на {destination_rod}: {disk}")
        print(f"Проміжний стан: {rods_state}")
        draw_rods(rods_state, total_disks_for_drawing)
        solve_hanoi(num_disks_to_move - 1, auxiliary_rod, destination_rod, source_rod, rods_state, total_disks_for_drawing)

def main():
    try:
        num_disks_total = int(input("Введіть кількість дисків: "))
        if num_disks_total < 0: # Дозволимо 0 дисків для коректного відмальовування "немає дисків"
            print("Кількість дисків не може бути від'ємною.")
            return
    except ValueError:
        print("Будь ласка, введіть дійсне ціле число для кількості дисків.")
        return
    rods = {
        'A': list(range(num_disks_total, 0, -1)),
        'B': [],
        'C': []
    }
    print(f"Початковий стан: {rods}")
    draw_rods(rods, num_disks_total)

    if num_disks_total > 0: # Розв'язуємо тільки якщо є диски
        solve_hanoi(num_disks_total, 'A', 'C', 'B', rods, num_disks_total)
        print(f"Кінцевий стан: {rods}")
        draw_rods(rods, num_disks_total)
    elif num_disks_total == 0:
        print("Немає дисків для переміщення.")
        print(f"Кінцевий стан: {rods}") # `draw_rods` вже викликана для 0 дисків

if __name__ == "__main__":
    main()
