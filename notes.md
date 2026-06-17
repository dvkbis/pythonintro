### Heap 
 - autant d'espace qu'on veut
### Stack (
 - géré par l'OS, 
 - chaque fois qu'on ouvre une fn - l'OS crée une "stack frame")
 - Toujours limité en taille (5Mb linux / 2Mb Windows)
 Stak aléatoirement placé (éviter les attaques de buffer)

### Vector -//- ArrayList
 
### RedBlackTree
 - Garantir une meme vitesse de lecture à gauche ou à droite
 - Colorer les nodes permet d'éviter les déséquilibres 
 - Garanti O(log(n))

### Algorithme de Tri
 Compléxité spatiale = impacte en mémoire
 - **Bubble Sort**
  - Optimisation (est-ce quelque chose a été swap -> Fin du tri)
  - A la fin des itérations : on peut enlever un element
 - **Quick Sort**
  - Complixité spatiale : Log(n)
  - Parcours avec deux pointeurs
 - **Merge Sort (o(n))**
   - Subdivisé le tableau en petite partie
   - 
   - CS : o(n) 
 - **Heap Sort**
  - Représenter sous forme d'un binary tree
  - 
 - **Seletor Sort**
  - Pas le plus optimisé
 - **Insertion Sort o(n²)**
  - 
### Multithreading
  - Partage le cache du cpu 
  - Multithread (concurrencielle / parallelisme)
  - Bloquer les variables (en cours d'utilisation) - Au niveau du kernel
  - Bug = deadlock : fn avec du threading - débloquer la variable mais pas débloquer à un endroit

- 3 exos - xml/html (balise) - regex?
- examen rh si réussi
- 2h avec un dev odoo sur les réponses coderbyte
- help -fn on console

## Migration (DB)
- 2 états (Upgrade / Downgrade)
- revenir à un état
- Contient la structure de la DB
- Attention quand on rename une col, on perd nos data -> Use op.alter_column() dans le fichier de migration
- /!\ Ajouter ces classes dans le fichier __init__.py et les imports
### Commands
- python -m alembic init alembic   
- python -m alembic revision --autogenerate -m "Add Customer Table"
- python -m alembic upgrade head 
- python -m alembic downgrade -1  
- python -m alembic current 
- python -m alembic revision

## venv
- python -m venv venv
- \venv\script\activate
- pip install sqlalchemy alembic psyopg2-binary