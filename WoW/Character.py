from random import randrange
from Equipment import Equipment
from random import uniform

class Character:
    def __init__(self, name, attack_speed=2, delay=0, equipment=None, max_health=0, max_delay=5, attack_range=None ):
        self.name = name 
        self.equipment = Equipment()
        self.max_health = 100 * self.equipment.cape 
        self.health = round(self.max_health * self.equipment.cape, 2)
        self.attack_speed = attack_speed
        self.delay = delay
        self.max_delay = 5
        self.attack_range = tuple([i for i in range(3, 12)])

    
    def attack(self):
        self.delay = 5 - self.attack_speed
        return int(randrange(3, 11) * self.equipment.sword)
    
    def __str__(self):
        return f'Name:{self.name}, Health:{int(self.health)}, Delay:{self.delay}'
    
    def __repr__(self):
        return f'Character:(Name:{self.name},Health:{self.health} Attack_Speed:{self.attack_speed}, Delay:{self.delay})'

    def is_dead(self):
        return self.health <= 0

    def end_round(self):
        self.health = self.health + 1 if self.health + 1 < self.max_health else  self.max_health
        self.delay -= 1

    def __iadd__(self, other):
        if isinstance(other, Character):
            self.health += other.health
            return self
        elif isinstance(other, int):
            self.health += other
            return self
    
    def __isub__(self, other):
        if isinstance(other, Character):
            self.health -= other.health
            return self
        elif isinstance(other, int):
            self.health -= other 
            return self













