if __name__ == "__main__":
    # Write your solution here
    speed = int(input("Введите скорость передачи данных байт/сек: "))
    time = int(input("Время загрузки данных мин.: "))
    coast = int(input("Стоимость трафика данных за Гб: "))
    # Переводим время в секунды
    time_sec = time * 60
    # Переводим скорость передачи данных в Гб/сек
    speed_gb_sec = speed / (1024 * 1024 * 1024)
    # Размер файла в ГБ
    filesize = time_sec * speed_gb_sec
    print("Стоимость: ", ((filesize - 1) / coast))
    print("Размер файла (Гб): ", (time_sec * speed_gb_sec))