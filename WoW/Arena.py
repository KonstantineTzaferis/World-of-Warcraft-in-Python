from wow import Character
from random import randrange

class Arena:
    def __init__(self, TeamA, TeamB):
        self.TeamA = TeamA 
        self.TeamB = TeamB

    def print_state(self):
        print('This is TeamA\n')
        for character in self.TeamA:
            character.print()
        print('=' * 50)
        print('This is TeamB\n')
        for character in self.TeamB:
            character.print()
        print('=' * 50)

    def play(self):
        time = -1
        while True:
            time += 1
            print(f'Time:{time}')
            print('=' * 50)
            print('Welcome to the game of WoW!')
            print('=' * 50)
            print('These are the Teams')
            print('=' * 50)
            self.print_state()
            print('This is the list of able players')
            print('=' * 50)
            able_players = []
            for character in self.TeamA:
                if character.delay == 0:
                    able_players.append(('A', character))
            for character in self.TeamB:
                if character.delay == 0:
                    able_players.append(('B', character))
            
            for team, character in able_players:
                print(team,end=':')
                character.print() 
            for character in able_players:
                attacking = character[1]
                if character[0] == 'A':
                    defending = self.TeamB[randrange(len(self.TeamB))]
                else:
                    defending = self.TeamA[randrange(len(self.TeamA))]
                damage = attacking.attack()
                defending.health -= damage
                print(f'{attacking.name} made {damage} damage to {defending.name}')

            for i in range(len(self.TeamA)-1, -1, -1):
                if self.TeamA[i].is_dead():
                    self.TeamA.pop(i)
            for i in range(len(self.TeamB)-1, -1, -1):
                if self.TeamB[i].is_dead():
                    self.TeamB.pop(i)

            if len(self.TeamA) == 0 and len(self.TeamB) == 0:
                print('We have a draw!')
                break
            elif len(self.TeamA) == 0:
                print('TeamB wins this game!')
                break
            elif len(self.TeamB) == 0:
                print('TeamA wins this game')
                break
            else:
                pass

            for character in self.TeamA:
                character.end_round()
            for character in self.TeamB:
                character.end_round()






















