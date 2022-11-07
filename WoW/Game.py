from random import randrange
from Character import Character
from Arena import Arena
from Equipment import Equipment
from TankMage import Tank, Mage

game = Arena([Character('Orc', attack_speed=2, delay=randrange(0,3)) for i in range(5)],
            [Character('Night Elf', attack_speed=3, delay=randrange(0,3)) for i in range(3)])
game.TeamB += [Mage('Night-Elf Mage')]
game.TeamA += [Tank('Orc-Tank')]
game.play()