from Character import Character
from Equipment import Equipment
from random import randrange

class Tank(Character):
    def __init__(self, name, attack_speed=2, delay=0, equipment=None, max_health=0, max_delay=5, attack_range=None):
        super().__init__(name, attack_speed, delay, equipment, max_health, max_delay, attack_range)
        self.max_health = self.max_health * 2
        self.health = 2 * self.health
    
    def __str__(self):
        return f'Tank Player-->{super().__str__()}'
    
    def __repr__(self):
        return f'This is a Tank Player-->{super().__str__()}'
    


class Mage(Character):
    def __init__(self, name, attack_speed=2, delay=0, equipment=None, max_health=0, max_delay=5, attack_range=None):
        super().__init__(name, attack_speed, delay, equipment, max_health, max_delay, attack_range)
        self.attack_range = tuple([i for i in range(8, 18)])
        self.mana = 100
        self.max_mana = 100
    
    def __str__(self):
        return f'This is a Mage Player-->{super().__str__()}'
    
    def lightning_spell(self):
        self.mana -= 50
        return randrange(30, 51)
    
    def attack(self):
        if self.mana <= 0:
            print('This is a Regular Attack')
            return super().attack()
        else:
            print('This is a lighting spell Attack')
            return self.lightning_spell()
    
    def end_round(self):
        self.mana += 1
        return super().end_round()
        