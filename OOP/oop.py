cars = []


class ControlPanel():

    def add_car(self):
        manufacturer = input("Введите производителя: ")
        model = input("Введите модель: ")

        print("Выберите вид машины:")
        print("1. Легковая")
        print("2. Грузовая")
        print("3. Мотоцикл")
        car_type_choice = input("Введите номер вида машины (1, 2 или 3): ")

        if car_type_choice == '1':
            car_type = "Легковая"
        elif car_type_choice == '2':
            car_type = "Грузовая"
        elif car_type_choice == '3':
            car_type = "Мотоцикл"
        else:
            print("Неверный выбор. Вид машины неопределен.")
            car_type = "Неопределен"

        car_number = input("Введите номер автомобиля: ")
        car_color = input("Введите цвет автомобиля: ")

        print("Был ли автомобиль в ДТП?")
        print("1. Да")
        print("2. Нет")
        dtp_choice = input("Выберите (1 - Да, 2 - Нет): ")
        car_dtp = "Да" if dtp_choice == '1' else "Нет"

        car = {
            "manufacturer": manufacturer,
            "model": model,
            "car_type": car_type,
            "number": car_number,
            "color": car_color,
            "dtp": car_dtp
        }

        cars.append(car)
        print("Автомобиль добавлен.")

    def edit_car(self, car_index):
        if 0 <= car_index < len(cars):
            car = cars[car_index]

            while True:
                print(f"1. Редактировать производителя ({car['manufacturer']})")
                print(f"2. Редактировать модель ({car['model']})")
                print(f"3. Редактировать вид авто ({car['car_type']})")
                print(f"4. Редактировать номер авто ({car['number']})")
                print(f"5. Редактировать цвет авто ({car['color']})")
                print(f"6. Редактировать информацию о ДТП (Да/Нет) ({car['dtp']})")
                print("7. Удалить авто")
                choice = input("Выберите, что вы хотите редактировать (1-7, или 'Enter' для отмены): ")

                if choice == '1':
                    car['manufacturer'] = input("Введите нового производителя: ")
                elif choice == '2':
                    car['model'] = input("Введите новую модель: ")
                elif choice == '3':
                    print("Выберите новый вид авто:")
                    print("1. Легковая")
                    print("2. Грузовая")
                    print("3. Мотоцикл")
                    car_type_choice = input("Введите номер вида авто (1, 2 или 3): ")
                    if car_type_choice == '1':
                        car['car_type'] = "Легковая"
                    elif car_type_choice == '2':
                        car['car_type'] = "Грузовая"
                    elif car_type_choice == '3':
                        car['car_type'] = "Мотоцикл"
                    else:
                        print("Неверный выбор. Вид авто не изменен.")
                elif choice == '4':
                    car['number'] = input("Введите новый номер автомобиля: ")
                elif choice == '5':
                    car['color'] = input("Введите новый цвет автомобиля: ")
                elif choice == '6':
                    print("Был ли автомобиль в ДТП?")
                    print("1. Да")
                    print("2. Нет")
                    dtp_choice = input("Выберите (1 - Да, 2 - Нет): ")
                    car['dtp'] = "Да" if dtp_choice == '1' else "Нет"
                elif choice == '7':
                    del cars[car_index]
                    print("Машина удалена.")
                    break
                else:
                    print("Редактирование отменено\n")
                    break
        else:
            print("Неверный номер автомобиля.")

    def save_cars_to_file(self):
        with open('cars.txt', 'w') as file:
            for car in cars:
                file.write(f"Производитель: {car['manufacturer']}\n")
                file.write(f"Модель: {car['model']}\n")
                file.write(f"Вид машины: {car['car_type']}\n")
                file.write(f"Номер автомобиля: {car['number']}\n")
                file.write(f"Цвет автомобиля: {car['color']}\n")
                file.write(f"Был ли автомобиль в ДТП: {car['dtp']}\n")
                file.write("\n")

    def load_cars_from_file(self):
        try:
            with open('cars.txt', 'r') as file:
                lines = file.readlines()
                car = None
                for line in lines:
                    line = line.strip()
                    if line.startswith("Производитель: "):
                        _, manufacturer = line.split(": ", 1)
                    elif line.startswith("Модель: "):
                        _, model = line.split(": ", 1)
                    elif line.startswith("Вид машины: "):
                        _, car_type = line.split(": ", 1)
                    elif line.startswith("Номер автомобиля: "):
                        _, number = line.split(": ", 1)
                    elif line.startswith("Цвет автомобиля: "):
                        _, color = line.split(": ", 1)
                    elif line.startswith("Был ли автомобиль в ДТП: "):
                        _, dtp = line.split(": ", 1)
                    elif not line:
                        car = {
                            "manufacturer": manufacturer,
                            "model": model,
                            "car_type": car_type,
                            "number": number,
                            "color": color,
                            "dtp": dtp
                        }
                        cars.append(car)
        except FileNotFoundError:
            pass



control_panel = ControlPanel()
control_panel.load_cars_from_file()


def characteristic_search(cars, characteristic, value):
    result = []
    for car in cars:
        if car.get(characteristic) == value:
            result.append(car)
    for i, cars in enumerate(result):
        return f"{i + 1}. {cars['manufacturer']} {cars['model']} ({cars['car_type']})"


while True:
    print("1. Вывести список автомобилей")
    print("2. Добавить автомобиль")
    print("3. Редактировать автомобиль")
    print("4. Поиск по характеристике")
    print("5. Сохранить и выйти")

    choice = input("Выберите действие: ")

    if choice == '1':
        if not cars:
            print("Список автомобилей пуст.")
        else:
            for i, car in enumerate(cars):
                print(f"{i + 1}. {car['manufacturer']} {car['model']} ({car['car_type']})")
    elif choice == '2':
        control_panel.add_car()
    elif choice == '3':
        if not cars:
            print("Список автомобилей пуст.")
        else:
            car_index = int(input("Введите номер автомобиля для редактирования: ")) - 1
            control_panel.edit_car(car_index)
    elif choice == '4':
        print('Введите номер характеристики для поиска:')
        print('1. Производитель')
        print('2. Модель')
        print('3. Вид машины')
        print('4. Номер машины')
        print('5. Цвет машины')
        print('6. Наличие ДТП')
        characteristic = None
        choice = int(input())
        if choice == 1:
            characteristic = 'manufacturer'
            print('введите значение характеристики')
            value = str(input())
            print('найденные машины:')
            found_cars = characteristic_search(cars, characteristic, value)
            print(found_cars)
        elif choice == 2:
            characteristic = 'model'
            print('введите значение характеристики')
            value = str(input())
            print('найденные машины:')
            found_cars = characteristic_search(cars, characteristic, value)
            print(found_cars)
        elif choice == 3:
            characteristic = 'car_type'
            print('введите значение характеристики')
            value = str(input())
            print('найденные машины:')
            found_cars = characteristic_search(cars, characteristic, value)
            print(found_cars)
        elif choice == 4:
            characteristic = 'number'
            print('введите значение характеристики')
            value = str(input())
            print('найденные машины:')
            found_cars = characteristic_search(cars, characteristic, value)
            print(found_cars)
        elif choice == 5:
            characteristic = 'color'
            print('введите значение характеристики')
            value = str(input())
            print('найденные машины:')
            found_cars = characteristic_search(cars, characteristic, value)
            print(found_cars)
        elif choice == 6:
            characteristic = 'dtp'
            print('введите значение характеристики')
            value = str(input())
            print('найденные машины:')
            found_cars = characteristic_search(cars, characteristic, value)
            print(found_cars)
        else:
            print('Неверное значение!')
        break
    elif choice == '5':
        control_panel.save_cars_to_file()
        print("Информация об автомобилях сохранена.")
        break


