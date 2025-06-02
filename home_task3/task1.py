import argparse
import shutil
from pathlib import Path
import sys

def parse_arguments():
    parser = argparse.ArgumentParser(description="Рекурсивно копіює та сортує файли за розширенням.")
    parser.add_argument("source_dir", type=Path, help="Шлях до вихідної директорії.")
    parser.add_argument("dest_dir", type=Path, nargs='?', default=Path("dist"),
                        help="Шлях до директорії призначення (за замовчуванням: 'dist').")  
    if len(sys.argv) <= 1 and (not hasattr(sys, 'ps1')): # sys.ps1 для перевірки інтерактивного режиму
         # Якщо запускається без аргументів не в інтерактивному режимі, показуємо допомогу
         parser.print_help(sys.stderr)
         sys.exit(1)         
    return parser.parse_args()

def copy_files_recursively(source_path: Path, dest_base_path: Path):
    try:
        for item in source_path.iterdir():
            if item.is_dir():
                # Рекурсивно обробляємо піддиректорії
                copy_files_recursively(item, dest_base_path)
            elif item.is_file():
                # Обробляємо файли
                extension = item.suffix[1:].lower() if item.suffix else "no_extension"
                target_subdir = dest_base_path / extension             
                try:
                    # Створюємо піддиректорію для розширення, якщо вона не існує
                    target_subdir.mkdir(parents=True, exist_ok=True)                    
                    # Формуємо повний шлях до файлу призначення
                    dest_file_path = target_subdir / item.name                    
                    # Копіюємо файл
                    shutil.copy2(item, dest_file_path)
                    print(f"Скопійовано: '{item}' -> '{dest_file_path}'")
                except OSError as e:
                    print(f"Помилка обробки файлу {item.name}: {e}")
                except Exception as e:
                    # Обробка інших можливих помилок під час копіювання конкретного файлу
                    print(f"Неочікувана помилка з файлом {item.name}: {e}")
                    
    except FileNotFoundError:
        # Цей блок може не спрацювати, якщо source_path перевіряється перед викликом
        print(f"Помилка: Директорію '{source_path}' не знайдено під час ітерації.")
    except PermissionError:
        print(f"Помилка: Відмовлено в доступі до '{source_path}'.")
    except Exception as e:
        # Загальна обробка помилок для поточної директорії source_path
        print(f"Неочікувана помилка під час обробки директорії {source_path}: {e}")

def main():    
    try:
        args = parse_arguments()
    except SystemExit as e:
        # argparse викликає SystemExit при помилках або --help
        if e.code == 0: # Успішний вихід (наприклад, --help)
             sys.exit(0)
        # print("Помилка парсингу аргументів. Використайте --help для довідки.")
        sys.exit(e.code) # Вихід з кодом помилки від argparse

    source_directory = args.source_dir
    destination_directory = args.dest_dir

    if not source_directory.exists():
        print(f"Помилка: Вихідна директорія '{source_directory}' не існує.")
        return
    if not source_directory.is_dir():
        print(f"Помилка: Вихідний шлях '{source_directory}' не є директорією.")
        return
    try:
        # Переконуємося, що базова директорія призначення існує
        destination_directory.mkdir(parents=True, exist_ok=True)
        print(f"Початок копіювання з '{source_directory}' до '{destination_directory}'...")
        copy_files_recursively(source_directory, destination_directory)
        print("Копіювання та сортування файлів завершено.")
    except OSError as e:
        print(f"Помилка створення директорії призначення '{destination_directory}': {e}")
    except Exception as e:
        print(f"Неочікувана помилка в головній функції: {e}")

if __name__ == "__main__":
#потрібно запустити скрипт з аргументами, наприклад:
#python task1.py C:/Games
    main()
