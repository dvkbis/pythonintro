import random

# Créer une grille (liste de listes) remplie avec la valeur donnée.
def create_grid(rows, cols, value):
    if rows < 0 or cols < 0:
        return None
    
    grid = []
    for _ in range(rows):
        row = []
        for _ in range(cols):
            row.append(value)
        grid.append(row)

    return grid

# Retourner la liste des coordonnées des cases voisines (8 directions)
#  en respectant les limites de la grille.
def get_neighbors(rows, cols, r, c):
    if not is_in_grid(rows, cols, r, c):
        return None
    
    neighbors_adds = [(-1,-1), (-1, 0), (-1,1),
                 (0,-1), (0,1),
                 (1,-1), (1,0), (1,1)]
    neighbors = set()

    for add in neighbors_adds:
        next_r, next_c = add[0] + r, add[1] + c
        if is_in_grid(rows, cols, next_r, next_c):
            neighbors.add((next_r, next_c))
            
    return neighbors

def is_in_grid(rows, cols, r, c):
    if r < 0 or r >= rows:
        return False
    if c < 0 or c >= cols:
        return False
    return True

# def is_mine(rows, cols, r, c):
#     if is_in_grid(rows, cols, r, c):
#         return False
        
#     return minesweeper_grid[r][c] == 1

# Générer un ensemble de positions de mines.
# Contraintes pour generate_mines
# - ne pas placer deux mines au même endroit
# - ne pas placer de mine sur forbidden_cell
def generate_possible_mines(rows, cols, forbidden_cell):
    mines = []
    for r in range(rows):
        for c in range(cols):
            if (r,c) == forbidden_cell:
                continue
            mines.append((r,c))
    return mines

def generate_mines(rows, cols, nb_mines, forbidden_cell):
    if rows < 0 or cols < 0:
        return None
    if nb_mines > rows * cols - 1:
        return None

    mines = generate_possible_mines(rows, cols, forbidden_cell)

    return random.sample(mines, nb_mines)

# Créer la grille interne du jeu :
# - "*" pour les mines
# - un entier pour le nombre de mines adjacentes sinon
def create_hidden_grid(rows, cols, mines):
    minesweeper_grid = create_grid(rows, cols, 0)
    for r, c in mines:
        minesweeper_grid[r][c] = 1

    return minesweeper_grid


# Révéler une case :
# - si la case contient un nombre différent de 0 → révéler uniquement cette case
# - si la case contient 0 → révéler récursivement les cases voisines
# visible

def reveal(hidden, visible, r, c):
    rows = len(hidden)
    cols = len(hidden[0])

    if not is_in_grid(rows, cols, r, c):
        return
    if hidden[r][c] == 1 or visible[r][c] == 'f':
        return 
    
    def reveal_neighbors(r, c):
        if visible[r][c] != '?': # and visible[r][c] != 'f':
            return
        if hidden[r][c] == 1:
            return
        neighbors = get_neighbors(rows, cols, r, c)
        count = 0
        for neighbor_r, neighbor_c in neighbors:
            if hidden[neighbor_r][neighbor_c] == 1:
                count += 1

        visible[r][c] = count
        if count == 0:
            for neighbor_r, neighbor_c in neighbors:
                reveal_neighbors(neighbor_r, neighbor_c)
   
    reveal_neighbors(r, c)


# Afficher la grille dans la console.
def print_grid(grid):
    for row in grid:
        print(" ".join(map(str,row)))

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

