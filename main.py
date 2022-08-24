import random

class Barrel:
    def __init__(self, length = 90):
        self.lst = [x for x in range(1, length + 1)]
        self.number = '-'
        self.last_bumber = '-'

    def get_barrel(self):
        self.last_number = self.number
        try:
            idx = random.randrange(0, len(self.lst))
            num = self.lst[idx]
            self.lst.pop(idx)
            self.number = num
            return num
        except ValueError:
            return "Лист пустий"

    def print_new(self):
        print('Новий барил: {} (Минулий барил: {}. Залишилось барил: {})'
              .format(self.get_barrel(), self.last_number, len(self.lst)))

class Cart:
    def __init__(self, length=90):
        self.lst = [x for x in range(1, length + 1)]
        self.fifteen = []
        self.health = 15 
        self._get_fifteen_items()
        self.original_line = [x for x in range(9)]
        self.lines = self._sort_random(self.original_line.copy())
        
    def _my_func(self, x):
        return int(x)
        
    def _get_fifteen_items(self):
        try:
            five = []
            copy_list = self.lst.copy()
            for x in range(1, 4):
                for y in range(1, 6):
                    idx = random.randrange(0, len(copy_list))
                    five.append(copy_list[idx])
                    copy_list.pop(idx)
                five.sort()
                self.fifteen.append(five.copy())
                five.clear()
            return self.fifteen
        except ValueError:
            return "Список менший"

    def _sort_random(self, lst):
        lines = []
        for x in range(3):
            for _ in range(10):
                x1 = random.randint(0, 8)
                x2 = random.randint(0, 8)
                if x1 != x2:
                    lst[x1], lst[x2] = lst[x2], lst[x1]
            lines.append(lst.copy())
        return lines
    
    def cross_out(self, num, delete=False):
        try:
            for x in range(0, 3):
                for y in range(0, 5):
                    if num == self.fifteen[x][y]:
                        if delete:
                            self.health -= 1
                            self.fifteen[x][y] = ' x'
                            return True
                        return True
            return False
        except ValueError:
            pass
        return "Список менший"

    def _print_name_cart(self):
        print('---------- Ваша карточка ----------')

    def print_cart(self):
        self._print_name_cart()

        for x in range(3):
            line = ''
            y = 0
            for j, el in enumerate(self.lines[x]):
                if el == 5 or el == 6 or el == 7 or el == 8:
                    line += ''.rjust(2)
                else:
                    line += str(self.fifteen[x][y]).rjust(2)
                    y += 1
                if j < len(self.lines[x]) - 1:
                    line += ''.rjust(2)
            print(line)
        print('-----------------------------------')

class CartComp(Cart):
    def _print_name_cart(self):
        print('------- Карточка суперника --------')

class Game:
    def __init__(self, human, comp):
        self.human = human
        self.comp = comp
        self.last_gamer = comp

    def go_comp(self):
        if self.comp.cross_out(barrel.number, True):
            self.check_cart()
            self.print_game()
            if self.game_over():
                return True
            else:
                return False
        else:
            self.check_cart()
            self.print_game()
            if self.game_over():
                return True
            else:
                return False

    def check_cart(self):
        if self.last_gamer.cross_out(barrel.number, True):
            pass
        if self.last_gamer == self.comp:
            self.last_gamer = self.human
        else:
            self.last_gamer = self.comp

    def game_over(self):
        if self.human.health == 0:
            print('Перемога за вами!')
            return True
        elif self.comp.health == 0:
            print('Перемога суперника!')
            return True
        else:
            return False

    def print_game(self):
            barrel.print_new()
            self.human.print_cart()
            self.comp.print_cart()

    def start(self):
        self.print_game()
        while True:
            try:
                key = input('Закрестили цифру? (y/n). Вихід (q) ')
                if key == 'y':
                    if self.human.cross_out(barrel.number, True):
                        self.check_cart()
                        self.print_game()
                        if self.game_over():
                            break
                        if self.go_comp():
                            break
                    else:
                        print("Ви програли, кінець гри")
                        break
                elif key == 'n':
                    if self.human.cross_out(barrel.number):
                        print("Ви програли, кінець гри")
                        break
                    else:
                        self.check_cart()
                        self.print_game()
                        if self.game_over():
                            break
                        if self.go_comp():
                            break
                elif key == 'q':
                    print("Завершення гри")
                    break
                else:
                    print()
            except Exception as cls:
                print('Помилка: ', cls)

barrel = Barrel()
my_cart = Cart()
cart_comp = CartComp()
game = Game(my_cart, cart_comp)

while True:
    try:
        mode = int(input('Почати грати\n'
                         '[1] - Так\n'
                         '[2] - вихід\n'))
        if mode == 1:
            game.start()
            break
        elif mode == 2:
            break
        else:
            print('Помилка, такій вибір не можливий')
    except ValueError:
        print('Введіть число')