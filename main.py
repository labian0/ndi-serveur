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
    def __init__(self, mat):
        self.mat = mat

    def afficher_plateau(self):
        for i in range(0,10):
            for j in range (10):
                self.mat[i][j].afficher()
            print("")
            

class Partie:
    def __init__(self):
        self.plateau = Plateau(init_plateau())
        self.tour = 1
        self.energie = 30
        self.bois = 30
        self.metal = 30
        self.state = "normal"

    def nouveau_tour(self):
        action = choix_action()
        coord = choix_coord()
        while (not(self.choix_possible(self.plateau, action, coord, self.state))):
            print("mauvais choix!!")
            action = choix_action()
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
        self.fin_tour()


    def retirer_dechet(self, coord):
        self.plateau[coord[0]][coord[1]].type = ' '
        self.energie -= 15

    def fabriquer_infrastructure(self, coord):
        self.plateau[coord[0]][coord[1]].type = 'I'
        self.bois -= 10
        self.metal -= 5
        self.energie -= 15

    def recolter_minerais(self, coord):
        self.plateau[coord[0]][coord[1]].type = ' '
        self.bois -= 15
        self.metal += 20
        self.energie -= 10

    def planter_arbre(self, coord):
        self.plateau[coord[0]][coord[1]].type = 'P'

    def jeter_dechet(self, coord):
        self.state = "pollue"
        self.plateau[coord[0]][coord[1]].type = ' '

    def depolluer(self):
        self.state = "normal"
        self.bois -= 20
        self.metal -= 10
        self.energie -= 15

    def couper_arbre(self, coord):
        self.plateau[coord[0]][coord[1]].type = ' '
        self.bois += 15
        self.energie -= 5

    def choix_possible(self, plateau, action, coord, state):
        if (action == 'r'):
            return (plateau[coord[0]][coord[1]].type == 'D' and self.energie >= 15)
        elif (action == 'f'):
            return (plateau[coord[0]][coord[1]].type == ' ' and self.energie >= 15 and self.bois >= 10 and self.metal >= 5)
        elif (action == 'm'):
            return (plateau[coord[0]][coord[1]].type == 'M' and self.energie >= 10 and self.bois >= 15)
        elif (action == 'p'):
            return (plateau[coord[0]][coord[1]].type == ' ' and self.energie >= 10)
        elif (action == 'j'):
            return (plateau[coord[0]][coord[1]].type == 'D')
        elif (action == 'd'):
            return (state == "pollue" and self.energie >= 30 and self.bois >= 20 and self.metal >= 10)
        elif (action == 'c'):
            return (plateau[coord[0]][coord[1]].type == 'B' and self.energie >= 5)

    def fin_de_tour(self):
        self.tour += 1
        compteur_dechet = 0
        compteur_nature = 0
        self.spread()
        for i in self.plateau:
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

               


    def spread(self):
        if (self.state == "normal"):
            odds = 20
        else:
            odds = 40
        for i in range (10):
            for j in range (10):
                if (self.plateau[i][j].type == 'D'):
                    if (randint(1,100) > odds):
                        direction = randint(0,7)
                        if (direction == 4):
                            direction = 8
                        self.plateau[i+(direction//3)][j+(direction%3)].type = 'D'


                

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

def perte():
    print(":'(")

def victoire():
    print("yipee!!")

def choix_action():
    #traitement actions
    return 'f'

def choix_coord():
    #traitement coordonnées
    return (0,0)
        