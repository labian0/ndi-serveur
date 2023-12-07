from random import randint


class Case:
    def __init__(self):
        rng = randint(1,100)
        if (rng < 11):
            self.type = 'D'
        elif (rng < 31):
            self.type = 'B'
        elif (rng < 46):
            self.type = 'M'
        else:
            self.type = 'N'

    def afficher(self):
        print(self.type)


class Plateau:
    def __init__(self, mat):
        self.mat = mat


    def afficher_plateau(self):
        for i in range(0,10):
            for j in range (10):
                self.mat[i][j].afficher()
                print(" / ")
            
            
def init_plateau():
        mat = []
        L = []
        for i in range(1, 101):
            case = Case()
            L.append(case)
            if (i%10 == 0):
                mat.append(L)
                L = []
        return mat

    

pla = Plateau(init_plateau())
pla.afficher_plateau()
