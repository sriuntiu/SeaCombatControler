import random


class SeaMap(object):
    board = []

    # Заполнение знаками '~'(волна) всего поля
    def sea_draw(self):
        for number in range(10):
            self.board.append(["~"] * 10)

    # Выбираем направление корабля
    def direction(self):
        dir_number = input('\tВведите направление корабля ( v или > ):  ')
        if dir_number == 'v':
            return 'row'
        elif dir_number == '>':
            return 'col'
        elif dir_number != 'v' and dir_number != '>':
            print('##### IOError #####: Введите правильный символ повторно')
            return SeaMap.direction(self)  # рекурсия

    def searching_free_slots(self, dir, len_ship):
        ship_coordinates = []
        valid_slots = 0
        random_slot = int(input('\tВведите координату столбца (от 0 до 9):  '))
        # Для облегчения ввода координат - координата строки будет выбрана рандомно
        ship_start_random = random.randint(0, 9 - len_ship)

        # Проверка карты на достаточное количество клеток для размещения корабля
        while valid_slots < len_ship:
            if dir == 'row' and self.board[ship_start_random][random_slot] == '~':

                ship_start_random += 1
                ship_coordinates.append({ship_start_random - 1: random_slot})
                valid_slots += 1
            elif dir == 'col' and self.board[random_slot][ship_start_random] == '~':
                ship_start_random += 1
                ship_coordinates.append({random_slot: ship_start_random - 1})
                valid_slots += 1
            else:
                ship_coordinates = []
                random_slot = random.randint(0, 9)
                ship_start_random = random.randint(0, 9 - len_ship)
                valid_slots = 0

        return ship_coordinates


class Warship(SeaMap):
    def placing_ships_and_dots(self, coordinates):
        # Координаты вокруг выбранной клетки [0,0]
        dot_coordinates = [[1, 1], [1, 0], [0, 1], [-1, -1], [-1, 0], [0, -1], [-1, 1], [1, -1]]
        len_ship = len(coordinates)

        for coord in coordinates:
            for row, col in coord.items():
                # Устанавливаем метку корабля согласно его типу палубы
                self.board[row][col] = str(len_ship)
                for index in dot_coordinates:
                    # Вне границ поля точки не ставим
                    if row + index[0] < 0 or row + index[0] > 9 or col + index[1] < 0 or col + index[1] > 9:
                        continue
                    # Если попали на точку или корабль, продолжаем искать свободный слот
                    elif self.board[row + index[0]][col + index[1]] != '~':
                        continue
                    else:
                        # Ставим точки, чтобы избежать расположения кораблей вплотную друг к другу
                        self.board[row + index[0]][col + index[1]] = '.'
