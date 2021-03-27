from itertools import permutations
from itertools import product


class Solver:
    def __init__(self):
        self.results = {}
        self.operations = list(product(["+", "-", "*", "/"],repeat = 4))
        # This is damn stupid please fix this
        self.brackets = list(list(x) for x in list(filter(lambda bracket: sum(bracket) == 5, list(product([0,1,2,3,4,5], repeat = 6)))))
        self.brackets = list(set(tuple(filter((0).__ne__, x)) for x in self.brackets))

    def solve(self, cards, number):
        possibleMoves = list(permutations(cards))

        for move in possibleMoves:
            for seq in self.operations:
               self.evalwBrackets(move, seq) 

        for k in self.results:
            if k == number:
                self.printResults(self.results[k])
    
    def evalwBrackets(self, numbers, seq):
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
                if int(res) == res and res > 0:
                    if res in self.results.keys():
                        self.results[res].append(string)
                    else:
                        self.results[res] = [string]
            except:
                pass


    def printResults(self, results):
        results = set(results)
        if len(results) == 0: 
            print("Not possible")
        else: 
            print("There are {res} results. ".format(res = len(results)))
            print(results)

if __name__ == "__main__":
    solver = Solver()
    solver.solve([6,7,3,2,1], 79)
