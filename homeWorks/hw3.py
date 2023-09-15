class Bank:
    def __init__(self, name, balanse):
        self._name = name
        self._balanse = balanse

    def tprint(self):
        print(f'Name: {self._name}\n'
              f'Balanse: {self._balanse}')

    def moneyX(self):
        add_m = int(input('Enter the amount to add: '))
        self._balanse += add_m
        print(self._balanse)

    def _kill(self):
        kill = int(input('Enter the withdrawal amount: '))
        self._balanse -= kill
        print(self._balanse)

    def jackpot(self):
        print(self.__jackpot())

    def __jackpot(self):
        print(f'Jackpot:{self._balanse * 10}')

    def _copy(self):
        print(Ben._balanse + Gven._balanse)


Ben = Bank('Ben', 2598)
Gven = Bank('Gven', 342)

print(Ben.tprint())
print(Ben.moneyX())
print(Ben._kill())
print(Ben.jackpot())
print(Ben._copy())
print(Gven.tprint())

