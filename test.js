

class Matrice {
    constructor() {
        this.matrice = [[1, 2, 6], [5, 4, 7], [6, 5, 4]];
        this.elements = {
            1: 'sol',
            2: 'poubelles',
            3: 'décharges',
            4: 'usines',
            5: 'arbre',
            6: 'infra',
            7: 'minerais'
        };
    }

    afficherMatrice() {
        console.log("Matrice:");
        this.matrice.forEach(row => {
            const mappedRow = row.map(number => this.elements[number]);
            console.log(mappedRow.join(' '));
        });
    }
}

const p = new Matrice();
p.afficherMatrice();