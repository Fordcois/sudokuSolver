class SingleNumber:
    def __init__(self, YLocation,XLocation,number=None,):
        self.Number = number
        if number is None:
            self.PossibleNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            self.Solved=False
        else:
            self.PossibleNumbers = [number]
            self.Solved=True
        self.GridLocation = (f'X{YLocation // 3}Y{XLocation // 3}')

    def RemovePossibleNumber(self,NumberToBeRemoved):
        if NumberToBeRemoved in self.PossibleNumbers:
            self.PossibleNumbers.remove(NumberToBeRemoved)
            self.TryToSolve()

    def TryToSolve(self):
        if len(self.PossibleNumbers)==1:
            self.Number=self.PossibleNumbers[0]
            self.Solved=True

    def __str__(self):
        if self.Solved:
            return str(self.Number)
        else:
            return 'X'


