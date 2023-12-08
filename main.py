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
            self.type = ' '
        self.plante = 0

    def afficher(self):
        print(self.type, end=' | ')


class Plateau:
    def __init__(self):
        self.mat = init_plateau()

    def afficher_plateau(self):
        for i in range(0,10):
            for j in range (10):
                self.mat[i][j].afficher()
            print("")

    def serialiser(self):
        newmat=[]
        for i in range(0,10):
            L = []
            for j in range (10):
                L.append(self.mat[i][j].type)
            newmat.append(L)
        return(newmat)
            

class Partie:
    def __init__(self):
        self.plateau = Plateau()
        self.tour = 1
        self.energie = 30
        self.bois = 30
        self.metal = 30
        self.state = "normal"

    def nouveau_tour(self):
        self.plateau.afficher_plateau()
        print(self.energie, self.bois, self.metal)
        action = choix_action()
        if (action != 'e'):
            coord = choix_coord()
            while (not(self.choix_possible(action, coord))):
                print("mauvais choix!!")
                action = choix_action()
                if (action != 'e'):
                    coord = choix_coord()
            while (action != 'e'):
                if (action == 'r'):
                    self.retirer_dechet(coord)
                elif (action == 'f'):
                    self.fabriquer_infrastructure(coord)
                elif (action == 'm'):
                    self.recolter_minerais(coord)
                elif (action == 'p'):
                    self.planter_arbre(coord)
                elif (action == 'j'):
                    self.jeter_dechet(coord)
                elif (action == 'd'):
                    self.depolluer()
                elif (action == 'c'):
                    self.couper_arbre(coord)
                action = choix_action()
                if (action != 'e'):
                    coord = choix_coord()
        self.fin_de_tour()

    def retirer_dechet(self, coord):
        self.plateau.mat[coord[0]][coord[1]].type = ' '
        self.energie -= 15

    def fabriquer_infrastructure(self, coord):
        self.plateau.mat[coord[0]][coord[1]].type = 'I'
        self.bois -= 10
        self.metal -= 5
        self.energie -= 15

    def recolter_minerais(self, coord):
        self.plateau.mat[coord[0]][coord[1]].type = ' '
        self.bois -= 15
        self.metal += 20
        self.energie -= 10

    def planter_arbre(self, coord):
        self.plateau.mat[coord[0]][coord[1]].type = 'P'
        self.energie -= 10

    def jeter_dechet(self, coord):
        self.state = "pollue"
        self.plateau.mat[coord[0]][coord[1]].type = ' '

    def depolluer(self):
        self.state = "normal"
        self.bois -= 20
        self.metal -= 10
        self.energie -= 30

    def couper_arbre(self, coord):
        self.plateau.mat[coord[0]][coord[1]].type = ' '
        self.bois += 15
        self.energie -= 5

    def choix_possible(self, action, coord):
        if (action == 'r'):
            return (self.plateau.mat[coord[0]][coord[1]].type == 'D' and self.energie >= 15)
        elif (action == 'f'):
            return (self.plateau.mat[coord[0]][coord[1]].type == ' ' and self.energie >= 15 and self.bois >= 10 and self.metal >= 5)
        elif (action == 'm'):
            return (self.plateau.mat[coord[0]][coord[1]].type == 'M' and self.energie >= 10 and self.bois >= 15)
        elif (action == 'p'):
            return (self.plateau.mat[coord[0]][coord[1]].type == ' ' and self.energie >= 10)
        elif (action == 'j'):
            return (self.plateau.mat[coord[0]][coord[1]].type == 'D')
        elif (action == 'd'):
            return (self.state == "pollue" and self.energie >= 30 and self.bois >= 20 and self.metal >= 10)
        elif (action == 'c'):
            return (self.plateau.mat[coord[0]][coord[1]].type == 'B' and self.energie >= 5)
        elif (action == 'e'):
            return True

    def fin_de_tour(self):
        self.tour += 1
        compteur_dechet = 0
        compteur_nature = 0
        self.spread()
        for i in self.plateau.mat:
            for case in i:
                if case.type == 'P':
                    if case.plante < 2:
                        case.plante+=1
                    else:
                        case.type = 'B'
                        case.plante = 0
                elif (case.type == 'I'):
                    self.energie += 10
                elif (case.type == 'D'):
                    compteur_dechet+=1
                if (case.type == ' ' or case.type == 'B' or case.type == 'P'):
                    compteur_nature+=1
        if (compteur_nature < 10):
            perte()
        if (compteur_dechet == 0):
            victoire()
        else:
            self.nouveau_tour()

    def spread(self):
        if (self.state == "normal"):
            odds = 20
        else:
            odds = 40
        for i in range (10):
            for j in range (10):
                if (self.plateau.mat[i][j].type == 'D'):
                    if (randint(1,100) < odds):
                        direction = randint(0,7)
                        if (direction == 4):
                            direction = 8
                        if(i+(direction//3 - 1) > -1 and i+(direction//3 - 1) < 10 and j+(direction%3 - 1) > -1 and j+(direction%3 - 1) < 10):
                            self.plateau.mat[i+(direction//3 - 1)][j+(direction%3 - 1)].type = 'D'
                if (self.plateau.mat[i][j].type == ' '):
                    if (randint(1,100) <= 2):
                        self.plateau.mat[i][j].type == 'D'

    def serialiser(self):
        newmat=[]
        for i in range(0,10):
            L = []
            for j in range (10):
                L.append(self.plateau.mat[i][j].type)
            newmat.append(L)
        return(newmat, self.energie, self.bois, self.metal, self.tour)


def init_plateau():
        mat = []
        L = []
        for i in range(1, 101):
            L.append(Case())
            if (i%10 == 0):
                mat.append(L)
                L = []
        return mat

def perte():
    #action si perte
    print(":'(")
    quit

def victoire():
    #action si victoire
    print("yipee!!")
    quit

def choix_action():
    #import des choix
    a = input("entre une action (la première lettre)")
    return a

def choix_coord():
    #import des choix
    a = int(input ("entre la ligne de la coord (entre 0 et 9)"))
    b = int(input ("entre la colonne de la coordonnée (entre 0 et 9)"))
    return (a,b)

if __name__ == "__main__":
    partie = Partie()
    partie.nouveau_tour()      