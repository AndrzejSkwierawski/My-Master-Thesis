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
    currentDeff = Deff
    # TODO: In Future version make also current init, Deff and so on
    # ----------------------------
    Image = 'images/warrior.jpg'

    Position = (0, 0)
    Spot = (0, 0)
    CanBeReached = True
    flee = False
    OpponentTeam = False

    def __init__(self, name="Dave", attack=25, hp=100, init=50, deff=0, class_r=ClassEnumerate["shortDistance"], size=1):
        self.Name = name
        self.Attack = attack
        self.HP = hp
        self.Init = init
        self.Deff = deff
        self.Class = class_r
        self.Size = size
        self.currentHP = hp

    def __repr__(self):
        return repr((self.Name, self.Attack, self.currentHP, "/", self.HP, self.Init, self.Deff, self.Class, self.Size))

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
            before_attack = target_char.currentHP
            target_char.currentHP -= self.Attack * ((100 * (100 - target_char.currentDeff)/100) - target_char.Deff)/100
            after_attack = target_char.currentHP
            if target_char.currentHP <= 0:
                target_char.Alive = False
                target_char.currentHP = 0
            # print(self.Name, "attacked", target_char.Name, "(HP from", before_attack, "to", after_attack, ")")
            return before_attack - after_attack
        else:
            warnings.warn("THIS CHARACTER IS ALREADY DEAD")
            return 0

    def defence(self):
        # print(self.Name, "is blocking")
        self.currentDeff = 50

    def wait(self):
        # print(self.Name, "waits")
        pass

    def start_flee(self):
        # print(self.Name, "flees")
        pass

    def cancel_defence(self):
        self.currentDeff = 0

    def set_image(self):
        if self.Class == 1:
            self.Image = 'images/warrior1.jpg'
            if self.Size == 2:
                self.Image = 'images/warrior2.jpg'
        elif self.Class == 2:
            self.Image = 'images/archer1.jpg'
            if self.Size == 2:
                self.Image = 'images/archer2.jpg'
        elif self.Class == 3:
            self.Image = 'images/mage1.jpg'
            if self.Size == 2:
                self.Image = 'images/mage2.jpg'
