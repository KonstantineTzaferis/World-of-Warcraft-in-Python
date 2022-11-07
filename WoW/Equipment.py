from random import uniform

class Equipment:
    def __init__(self):
        self.sword = uniform(1.1, 1.5)
        self.cape = uniform(1.1, 1.3)

    def __str__(self):
        return f'Sword:{self.sword}, Cape:{self.cape}'
    
    def __repr__(self):
        return f'Equipment Class:(Sword-{self.sword}, Cape-{self.cape})'

