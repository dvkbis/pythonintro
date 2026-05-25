# Créer une grille (liste de listes) remplie avec la valeur donnée.
def create_grid(rows, cols, value):
    pass


# Retourner la liste des coordonnées des cases voisines (8 directions)
#  en respectant les limites de la grille.
def get_neighbors(rows, cols, r, c):
    pass

# Générer un ensemble de positions de mines.
# Contraintes pour generate_mines
# - ne pas placer deux mines au même endroit
# - ne pas placer de mine sur forbidden_cell
def generate_mines(rows, cols, nb_mines, forbidden_cell):
    pass

# Créer la grille interne du jeu :
# - "*" pour les mines
# - un entier pour le nombre de mines adjacentes sinon
def create_hidden_grid(rows, cols, mines):
    pass

# Révéler une case :
# - si la case contient un nombre différent de 0 → révéler uniquement cette case
# - si la case contient 0 → révéler récursivement les cases voisines
def reveal(hidden, visible, r, c):
    pass
# Afficher la grille dans la console.
def print_grid(grid):
    pass

# Retourner True si toutes les cases non minées ont été révélées, sinon False.
def has_won(hidden, visible):
    pass

# Fonction principale :
# - gère les entrées utilisateur
# - gère la logique du jeu
# - appelle les autres fonctions
def minesweeper(rows, cols, nb_mines):
    pass

# Commandes utilisateur
# - o ligne colonne → ouvrir une case
# - f ligne colonne → poser ou retirer un drapeau
# 
def convert_input_user(commandes):
    pass 

