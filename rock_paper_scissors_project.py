import random

moves = ['rock', 'paper', 'scissors']


class Player:
    my_move = None
    their_move = None

    def move(self):
        pass

    def learn(self, my_move, their_move):
        pass


class AllRockPlayer(Player):
    def move(self):
        return 'rock'


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    def move(self):
        while True:
            move = input("Rock, paper, scissors? > ").lower()
            if move in moves:
                return move
            elif move == 'quit':
                exit()


class ReflectPlayer(Player):
    def learn(self, my_move, their_move):
        self.their_move = their_move

    def move(self):
        if self.their_move is None:
            return random.choice(moves)
        else:
            return self.their_move


class CyclePlayer(Player):
    def learn(self, my_move, their_move):
        self.my_move = my_move

    def move(self):
        if self.my_move is None:
            return random.choice(moves)
        else:
            index = moves.index(self.my_move) + 1
            if index % len(moves) == 0:
                index = 0
            self.my_move = moves[index]
            return self.my_move


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1.score = 0
        self.p2.score = 0

    def get_rounds(self):
        while True:
            rounds = input("How many rounds? > ")
            if rounds.isnumeric():
                return int(rounds) + 1
            elif rounds == 'quit':
                exit()

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()

        print(f"You played {move1}")
        print(f"Opponent played {move2}\n")

        if beats(move1, move2):
            self.p1.score += 1
            print("** PLAYER ONE WINS THIS ROUND **")
        elif beats(move2, move1):
            self.p2.score += 1
            print("** PLAYER TWO WINS THIS ROUND **")
        else:
            print("** THIS ROUND'S A TIE **")
        print("Scores:")
        print(f"Player One: {self.p1.score}")
        print(f"Player Two: {self.p2.score}\n")

        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Rock paper scissors, Go!\n")
        for round in range(1, self.get_rounds()):
            print(f"Round {round}:")
            self.play_round()
        if self.p1.score > self.p2.score:
            print("** PLAYER ONE WINS THE GAME! **")
        elif self.p2.score > self.p1.score:
            print("PLAYER TWO WINS THE GAME!")
        else:
            print("THE GAME IS TIED!")
        print(f"Final Scores:")
        print(f"Player One: {self.p1.score}")
        print(f"Player Two: {self.p2.score}\n")
        print("Game over!")


players = [AllRockPlayer(), RandomPlayer(), ReflectPlayer(), CyclePlayer()]
random_player = random.choice(players)

if __name__ == '__main__':
    game = Game(HumanPlayer(), random_player)
    game.play_game()
