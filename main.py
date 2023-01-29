
class Drink:

    Gaz_drink = "Coca_cola"
    Juice = "Orange_Juice"
    Milk = "Chocolate_milk"
    Kompot = "Strawberry_kompot"
    def __init__(self):
        print(id(self))

dr2 = Drink()

print(Drink.Gaz_drink)
print(Drink.Juice)
print(Drink.Milk)
print(Drink.Kompot)

class Food:

    Snacks = "Meat_Balls"
    pourige = "Flakes"
    Meat = "Beef_steak"
    Fish = "Skumbriya"
    def __init__(self):
        print(id(self))

fd1 = Food()

print(Food.Snacks)
print(Food.pourige)
print(Food.Meat)
print(Food.Fish)

class Pearsonal:

    Waiter = "Nikita"
    Waitress = "Elena"
    Chef = "Igor"
    Boss = "Konstantin"
    def __init__(self):
        print(id(self))

Pr3 = Pearsonal()

print(Pearsonal.Chef)
print(Pearsonal.Waiter)
print(Pearsonal.Waitress)
print(Pearsonal.Boss)
