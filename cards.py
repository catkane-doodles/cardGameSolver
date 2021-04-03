import multiprocessing
import os

from itertools import permutations
from itertools import product
from itertools import chain


class Solver:
    def __init__(self):
        self.cpu_count = os.cpu_count()

        self.operations = list(product(["+", "-", "*", "/"],repeat = 4))
        self.brackets = list(list(x) for x in list(filter(lambda bracket: sum(bracket) == 5, list(product([0,1,2,3,4,5], repeat = 6)))))
        self.brackets = list(set(tuple(filter((0).__ne__, x)) for x in self.brackets))

        self.target = None

    def worker(self, move):
        results = []
        target = self.target

        for seq in self.operations:
            for bracket in self.brackets:
                lNumbers = move
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
                        results.append(string)
                except:
                    pass
        
        return results

    def solve(self, cards, target):
        possibleMoves = list(permutations(cards))

        self.target = target

        pool = multiprocessing.Pool(processes=self.cpu_count)
        result = pool.map(self.worker, possibleMoves)

        return set(chain(*result))
    

if __name__ == "__main__":
    solver = Solver()
    print(solver.solve([10,10,9,8,2], 46))
