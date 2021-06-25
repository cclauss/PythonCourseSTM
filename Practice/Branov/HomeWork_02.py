# Задание 1

def print_max(*args):
    print(f'Самое большое число из {args}: ', max(args))


print_max(3, 1, 5, 9, 12, 0)


# Задание 2

def get_max(*args):
    return max(args)


result = get_max(5, 8, 333, 0, 7)
print(result)

# Задание 3

'''
* Провести объектно-ориентированный анализ задачи и определить объекты, которые потребуется использовать 
(подсказка: необходимо инкапсулировать изменяемые аспекты поведения объектов): 
создается компьютерная игра, поддерживающая одновременное управление несколькими персонажами; 
каждый персонаж умеет бегать, стрелять и собирать предметы; 
некоторые персонажи умеют летать; 
каждый тип действий сопровождается определенной анимацией; 
собираемые предметы могут менять характеристики действий и соответствующую анимацию 
(например, вдвое ускорять или, наоборот, замедлять бег персонажа).
'''

from random import randint

ITEMS = [{'apple': {'strength': 1}},
         {'booze': {'agility': -2, 'intelligence': -4}},
         {'fire_blade': {'strength': 4, 'agility': 2}},
         {'wizard_staff': {'strength': 1, 'intelligence': 6}}
         ]


class BaseCharacter:

    def __init__(self, name):
        self.name = name
        self.level = 1
        self.strength = 10
        self.agility = 10
        self.intelligence = 10
        self.position = [0, 0]
        self.base_speed = 2
        self.items = []

    def move(self):
        self.position[0] += self.base_speed + self.agility * .2
        print(f'{self.name} перешел в {self.position}')

    def shoot(self):
        print(f'{self.name} выстрелил!')

    def _change_stats(self, meta, drop=False):
        k = -1 if drop else 1
        for stat, val in meta.items():
            if stat == 'strength':
                self.strength += val * k
            elif stat == 'agility':
                self.agility += val * k
            elif stat == 'intelligence':
                self.intelligence += val * k

    def get_item(self, item):
        self.items.append(item)
        item_meta = list(item.items())
        self._change_stats(item_meta[0][1])
        print(f'{self.name} нашел {item_meta[0][0]}, характеристики изменены: {item_meta[0][1]}')


class FlyingCharacter(BaseCharacter):

    def __init__(self, name):
        super().__init__(name)
        self.fly_speed = self.agility * .4 + self.strength * .2

    def fly(self):
        self.position[0] += self.fly_speed
        print(f'{self.name} перелетел в {self.position}')


if __name__ == '__main__':
    nick = BaseCharacter('Nick')
    nick.move()
    nick.shoot()
    nick.get_item(ITEMS[randint(0, len(ITEMS) - 1)])
    nick.move()
