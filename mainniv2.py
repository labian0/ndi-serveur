from random import randint


class Case:
    def __init__(self):
        self.type=' '
        self.background = 'M'
        rng = randint(1,100)
        if (rng < 30):
            self.type = 'D'
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

class Partie:
    def __init__(self):
        self.plateau = Plateau()
        self.tour = 1
        self.energie = 30
        self.bois = 30
        self.plastique = 30
        self.state = "normal"
        self.rapport= False

    def nouveau_tour(self):
        self.plateau.afficher_plateau()
        print(self.energie, self.bois, self.plastique)
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
                    self.collecter_plastique(coord)
                elif (action == 'f'):
                    self.fabriquer_infrastructure(coord)
                elif (action == 'p'):
                    self.planter_arbre(coord)
                elif (action == 'b'):
                    self.bruler_dechet(coord)
                elif (action == 'd'):
                    self.depolluer()
                elif (action == 'c'):
                    self.couper_arbre(coord)
                action = choix_action()
                if (action != 'e'):
                    coord = choix_coord()
        self.fin_de_tour()

    def collecter_plastique(self, coord):
        if (self.plateau.mat[coord[0]][coord[1]].background == 'M'):
            self.plateau.mat[coord[0]][coord[1]].type = ' '
        else:
            self.plateau.mat[coord[0]][coord[1]].type = 'T'
        self.energie -= 10
        self.plastique += 10

    def fabriquer_infrastructure(self, coord):
        self.plateau.mat[coord[0]][coord[1]].type = 'I'
        self.bois -= 10
        self.plastique -= 20
        self.energie -= 10

    def planter_arbre(self, coord):
        self.plateau.mat[coord[0]][coord[1]].type = 'P'
        self.energie -= 10

    def bruler_dechet(self, coord):
        self.state = "pollue"
        self.plateau.mat[coord[0]][coord[1]].type = ' '

    def depolluer(self):
        self.state = "normal"
        self.bois -= 20
        self.plastique -= 10
        self.energie -= 30

    def couper_arbre(self, coord):
        if (self.plateau.mat[coord[0]][coord[1]].background == 'M'):
            self.plateau.mat[coord[0]][coord[1]].type = ' '
        else:
            self.plateau.mat[coord[0]][coord[1]].type = 'T'
        self.bois += 15
        self.energie -= 5

    def lancer_rapport(self):
        self.rapport = True
        self.bois -= 10
        self.plastique -= 20
        self.energie -= 50

    def choix_possible(self, action, coord):
        if (action == 'r'):
            return (self.plateau.mat[coord[0]][coord[1]].type == 'D' and self.energie >= 10)
        elif (action == 'f'):
            return (self.plateau.mat[coord[0]][coord[1]].type == 'T' and self.energie >= 10 and self.bois >= 10 and self.plastique >= 20)
        elif (action == 'p'):
            return (self.plateau.mat[coord[0]][coord[1]].type == 'T' and self.energie >= 10)
        elif (action == 'b'):
            return (self.plateau.mat[coord[0]][coord[1]].type == 'D')
        elif (action == 'd'):
            return (self.state == "pollue" and self.energie >= 30 and self.bois >= 20 and self.plastique >= 10)
        elif (action == 'c'):
            return (self.plateau.mat[coord[0]][coord[1]].type == 'B' and self.energie >= 5)
        elif (action == 'l'):
            return (self.energie >= 50 and self.bois >= 10 and self.plastique >= 20)
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
                if (case.type == 'T' or case.type == 'B' or case.type == 'P' or case.type == ' '):
                    compteur_nature+=1
        for i in self.plateau.mat:
            for case in i:
                if (case.type == 'T' or case.type == 'B' or case.type == 'P'):
                    rng = randint(0,99)
                    if (rng < compteur_dechet//10):
                        case.type == ' '
        if (compteur_nature < 10):
            perte()
        if (compteur_dechet == 0):
            victoire()
        else:
            self.nouveau_tour()

    def spread(self):
        odds = 10
        if (self.state=="pollue"):
            odds*=2
        if (self.rapport==True):
            odds/=2
        for i in self.plateau.mat:
            for case in i:
                rng = randint(0,99)
                if (rng < odds):
                    case.type= "D"

    def serialiser(self):
        newmat=[]
        for i in range(0,10):
            L = []
            for j in range (10):
                L.append(self.plateau.mat[i][j].type)
            newmat.append(L)
        return({ "mat" : newmat, "energie" : self.energie, "bois" : self.bois, "plastique" : self.plastique, "tour" : self.tour})
        
def init_plateau():
        mat = []
        L = []
        for i in range(1, 101):
            L.append(Case())
            if (i%10 == 0):
                mat.append(L)
                L = []
        for i in range (4):
            mat = creer_ile(mat) 
        return mat

def creer_ile(mat):
    rng= randint (0,99)
    taille = randint(5,10)
    mat = agrandir_ile(mat, (rng//10, rng%10), taille)
    return mat

def agrandir_ile(mat, coord, taille):
    while (taille > 0):
        i = randint (-1, 1)
        j = randint (-1, 1)
        coord = (coord[0] + i , coord[1] + j)
        if (coord[0] > -1 and coord[0] < 10 and coord[1] > 0 and coord[1] < 10):
            mat[coord[0]][coord[1]].background = 'T'
            if (randint(1,10)<=3):
                mat[coord[0]][coord[1]].type = 'B'
            else:
                mat[coord[0]][coord[1]].type = 'T'
        taille -=1
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