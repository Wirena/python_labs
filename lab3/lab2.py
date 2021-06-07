A = 0
B = 1
C = 2
D = 3
E = 4
F = 5
ERR = -1


class C32:
    currentState = A
    stateTable = (((B, 0), (ERR,)), ((D, 2), (C, 1)), ((D, 3), (E, 4)),
                  ((A, 6), (E, 5)), ((F, 7), (E, 8)), ((ERR,), (ERR,)))

    def rev(self):
        stepInfo = self.stateTable[self.currentState][0]
        if stepInfo[0] == ERR:
            raise RuntimeError
        self.currentState = stepInfo[0]
        return stepInfo[1]

    def zoom(self):
        stepInfo = self.stateTable[self.currentState][1]
        if stepInfo[0] == ERR:
            raise RuntimeError

        self.currentState = stepInfo[0]
        return stepInfo[1]


