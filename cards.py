from itertools import permutations
from itertools import product


class Solver:
    def __init__(self):
        self.results = []
        self.operations = list(product(["+", "-", "*", "/"],repeat = 4))
        # This is damn stupid please fix this
        self.brackets = list(list(x) for x in list(filter(lambda bracket: sum(bracket) == 5, list(product([0,1,2,3,4,5], repeat = 6)))))
        self.brackets = list(set(tuple(filter((0).__ne__, x)) for x in self.brackets))

    def solve(self, cards, target):
        possibleMoves = list(permutations(cards))

        for move in possibleMoves:
            for seq in self.operations:
               self.addRelevant(move, seq, target) 

        return self.results
    
    def addRelevant(self, numbers, seq, target):
        for bracket in self.brackets:
            lNumbers = numbers
            lSeq = list(seq)
            lSeq.insert(0, "")
            string = ""
            for i in bracket:
                string += lSeq.pop(0)
                string += "("
                string += str(lNumbers[0])
                for j in range(1,len(lNumbers[:i])):
                    string += lSeq.pop(0)
                    string += str(lNumbers[j])
                string += ")"
                lNumbers = lNumbers[i:]
            try:
                res = eval(string)
                if int(res) == target:
                    self.results.append(string)
            except:
                pass


if __name__ == "__main__":
    solver = Solver()
    print(solver.solve([6,7,3,2,1], 79))
