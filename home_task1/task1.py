import queue
import time
import uuid # Для генерації унікальних ID заявок
import random # Для імітації різного часу обробки та генерації

# Створюємо чергу заявок
request_queue = queue.Queue()
request_counter = 0 # Лічильник для простих ID, якщо uuid не потрібен

def generate_request():   
    global request_counter
    request_counter += 1
    # Створюємо унікальний ID для заявки
    request_id = uuid.uuid4()      
    # Імітуємо деякі дані заявки
    request_data = {
        "id": str(request_id),
        "type": random.choice(["Технічна проблема", "Запит на інформацію", "Скарга"]),
        "priority": random.choice(["Високий", "Середній", "Низький"])
    }    
    request_queue.put(request_data)
    print(f"➡️  Нова заявка додана: {request_data['id']} (Тип: {request_data['type']}, Пріоритет: {request_data['priority']}). Черга: {request_queue.qsize()} заявок.")

def process_request():    
    if not request_queue.empty():
        current_request = request_queue.get()
        print(f"⏳ Обробка заявки: {current_request['id']}...")
        # Імітація часу на обробку заявки
        processing_time = random.uniform(0.5, 2.0) # Випадковий час від 0.5 до 2 секунд
        time.sleep(processing_time)
        print(f"✅ Заявка {current_request['id']} оброблена за {processing_time:.2f} сек. Залишилось в черзі: {request_queue.qsize()} заявок.")
        request_queue.task_done() # Повідомляємо черзі, що задача виконана (важливо для деяких типів черг)
    else:
        print("Черга заявок пуста. Немає чого обробляти.")

# Головний цикл програми
if __name__ == "__main__":
    print("🚀 Симулятор сервісного центру запущено. Натисніть CTRL+C для виходу.")
    try:
        while True:
            # Імітація випадкової генерації заявок
            if random.random() < 0.7: # З ймовірністю 70% генеруємо нову заявку
                generate_request()            
            # Імітація обробки заявок
            if random.random() < 0.5 or not request_queue.empty(): # З ймовірністю 50% або якщо черга не пуста
                process_request()            
            # Невелика затримка, щоб не перевантажувати вивід і процесор
            time.sleep(random.uniform(0.1, 0.5))             
    except KeyboardInterrupt:
        print("\n🛑 Симулятор сервісного центру зупинено користувачем.")
    finally:
        # Завершення всіх задач у черзі перед виходом (якщо потрібно)
        # request_queue.join() # Розкоментуйте, якщо використовуєте task_done() і хочете дочекатися завершення всіх задач
        print("🚪 Програма завершена.")