class Tank:
    x = 0
    speed = 1
    health = 1

    def draw(self):
        print(f"I'm Tank at {self.x}")

    def move(self):
        self.x += self.speed

    def shoot(self):
        print("Ba-bah")


class T34(Tank):
    def draw(self):
        print(f"I'm T34 at {self.x}")

class Tiger(Tank):
    def draw(self):
        print(f"I'm Tiger at {self.x}")


tanks = [Tank(), T34(), Tiger()]
for tank in tanks:
    tank.draw()
while True:
    cmd = input("Введите команду (shoot или move): ")
    n = int(input("Введите номер танка (от 0 до 2): "))
    if cmd == "move":
        tanks[n].move()
    elif cmd == "shoot":
        tanks[n].shoot()
    else:
        break
    for tank in tanks:
        tank.draw()

