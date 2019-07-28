import warnings


class Character:
    ClassEnumerate = {"shortDistance": 1, "longDistance": 2, "wholeArea": 3}

    # fields --------------------
    Name = "Dave"
    Attack = 25
    HP = 100
    Init = 50
    Deff = 0
    Class = ClassEnumerate["shortDistance"]
    Size = 1
    Alive = True

    currentHP = HP
    # TODO: In Future version make also current init, Deff and so on
    # ----------------------------
    Image = 'images/warrior.jpg'

    def __init__(self, name="Dave", attack=25, hp=100, init=50, deff=0, class_r=ClassEnumerate["shortDistance"], size=1):
        self.Name = name
        self.Attack = attack
        self.HP = hp
        self.Init = init
        self.Deff = deff
        self.Class = class_r
        self.Size = size
        self.currentHP = hp

    def print_properties(self):
        print("Name: ", self.Name)
        print("HP: ", self.currentHP, "/",  self.HP)
        print("Attack: ", self.Attack)
        print("Initiative: ", self.Init)
        print("Defence: ", self.Deff)
        print("Class: ", self.Class)
        print("Size: ", self.Size)
        print("Alive: ", self.Alive)

    def attack_character(self, target_char):
        if target_char.Alive:
            target_char.currentHP -= self.Attack * (100-target_char.Deff)/100
            if target_char.currentHP <= 0:
                target_char.Alive = False
                target_char.currentHP = 0
        else:
            warnings.warn("THIS CHARACTER IS ALREADY DEAD")

    def set_image(self):
        if self.Class == 1:
            self.Image = 'images/warrior.jpg'
        elif self.Class == 2:
            self.Image = 'images/archer.jpg'
        elif self.Class == 3:
            self.Image = 'images/mage.jpg'
