from random import randrange
from wow import Character
from Arena import Arena

game = Arena([Character('Orc', attack_speed=2, delay=randrange(0,3)) for i in range(5)],
            [Character('Night Elf', attack_speed=3, delay=randrange(0,3)) for i in range(3)])
game.play()
