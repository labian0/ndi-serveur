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
        if (not(choix_possible(self.plateau, action, coord, self.state))):
            erreur()
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



#def nouveau_tour():

def choix_action():
    #traitement actions
    return 'f'

def choix_coord():
    #traitement coordonnées
    return (0,0)

def choix_possible(plateau, action, coord, state):
    if (action == 'r'):
        return (plateau[coord[0]][coord[1]].type == 'D')
    elif (action == 'f'):
        return (plateau[coord[0]][coord[1]].type == ' ')
    elif (action == 'm'):
        return (plateau[coord[0]][coord[1]].type == 'M')
    elif (action == 'p'):
        return (plateau[coord[0]][coord[1]].type == ' ')
    elif (action == 'j'):
        return (plateau[coord[0]][coord[1]].type == 'D')
    elif (action == 'd'):
        return (state == "pollue")
    elif (action == 'c'):
        return (plateau[coord[0]][coord[1]].type == 'B')
    
def retirer_dechet()    
        