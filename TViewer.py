from SeaModel.SeaCombatMap import *
from FileOperations.Save import *
from FileOperations.Load import *


def main():
    try:
        print('\nВас приветствует генератор расположения кораблей на карте для игры "Морской бой"')
        if input("Загрузить ранее сохраненной карту? Введите y: ") == 'y':
            fle = LoadFromFile("SeaMap.txt")
            with fle as ctx:
                print('Предыдущая карта:')
                buf = ctx.read()
                print(buf)

        else:
            print('Загрузка отменена')
            a = SeaMap()
            b = Warship()

            a.sea_draw()
            # ship_board = [4, 3, 2, 1]
            # Расстановка  кораблей в порядке уменьшения их палуб.
            for x in range(4,0,-1):
                # x = 3 для отладки
                print('Process: Установка {} палубного корабля на карту'.format(x))
                for i in range(5 - x, 0, -1):
                    b.placing_ships_and_dots(a.searching_free_slots(a.direction(), i))

            fout = SaveToFile("SeaMap.txt")

            with fout:
                print('Ваша карта:')
                for x in a.board:
                    print(" ".join(x), file=fout)
                    print(" ".join(x))
                    # fout.write(" ".join(x)) # почему-то через вызов функции работает неверно
    except OpenFileError:
        print('can`t open file')


if __name__ == '__main__':
    main()