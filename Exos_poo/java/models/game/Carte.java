package models.game;

import java.util.*;

public class Carte {


    public enum Direction{
        UP, RIGHT, DOWN, LEFT;

        public static Position changeDirection(Position position, Direction direction){
            return switch (direction){
                case UP -> new Position(position.x() -1 , position.y());
                case DOWN -> new Position(position.x() + 1, position.y() );
                case LEFT -> new Position(position.x() , position.y() - 1);
                case RIGHT -> new Position(position.x(), position.y() + 1);
            };
        }
    }

    private static final char VIDE = '.';
    private final char[][] carte;
    private final int TAILLE;

    public Carte(int taille){
        this.TAILLE = taille;
        carte = initMap(taille);

    }

    // Initialiser le tableau avec des cases vides
    public char[][] initMap(int taille) {
        char[][] initCarte = new char[taille][taille];
        for (int i = 0; i < taille; i++) {
            for (int j = 0; j < taille; j++) {
                initCarte[i][j] = VIDE;
            }
        }
        return initCarte;
    }

//    public boolean placerElement(char Element, int x, int y){
//        if(carte[x][y] == VIDE){
//            carte[x][y] = Element;
//            return true;
//        }
//        return false;
//    }

    public boolean move(Position from, Direction direction){
        if(from == null || direction == null)
            return false;

        Position to = Direction.changeDirection(from, direction);

        return move(from, to);
    }

    public boolean move(Position from, Position to){
        if(isElement(from) && isInsideCarte(to) && !isElement(to)){
            carte[to.x()][to.y()] = carte[from.x()][from.y()];
            carte[from.x()][from.y()] = VIDE;
            return true;
        }
        return false;
    }


    // Placer les éléments de manière aléatoire en respectant la contrainte
    public Position insertElementRandomly(char element, int space, int nbTry) throws ImpossiblePlacementException {
        Random random = new Random();
        int count = 0;
        boolean findPosition = false;
        Position position = null;

        while (count++ < nbTry && !findPosition){
            int x = random.nextInt(TAILLE);
            int y = random.nextInt(TAILLE);

            if(peutPlacerElement(x, y, space)){
                position = new Position(x, y);
                findPosition = true;
            }
        }

        return createElement(position, element) ? position : null;
    }

    public boolean createElement(Position position, char element) {
        if(position == null || isElement(position))
            return false;

        carte[position.x()][position.y()] = element;
        return true;
    }

    public void removeElement(Position position){
        if(isElement(position))
            carte[position.x()][position.y()] = VIDE;
    }

    // Vérifier si un élément peut être placé à la position (x, y)
    private boolean peutPlacerElement(int x, int y, int space) {
        if (carte[x][y] != VIDE) return false; // Case déjà occupée

        // Vérifier les cases dans un rayon de 2 autour de (x, y)
        for (int i = -space; i <= space; i++) {
            for (int j = -space; j <= space; j++) {
                int nx = x + i;
                int ny = y + j;

                // S'assurer que les indices sont dans les limites du tableau
                if (isInsideCarte(nx, ny)) {
                    if (carte[nx][ny] != VIDE) {
                        return false; // Trop proche d'un autre élément
                    }
                }
            }
        }

        return true;
    }

    // Afficher le tableau
    public void afficherCarte() {
        for (int i = 0; i < TAILLE; i++) {
            for (int j = 0; j < TAILLE; j++) {
                System.out.print(carte[i][j] + " ");
            }
            System.out.println();
        }
    }

    public boolean isInsideCarte(Position position) {
        if(position == null) return false;
        return isInsideCarte(position.x(), position.y());
    }

    public boolean isInsideCarte(int x, int y){
        return x >= 0 && x < TAILLE && y >= 0 && y < TAILLE;
    }

    public boolean isElement(Position position){
        if(position == null) return false;
        int x = position.x();
        int y = position.y();
        return isInsideCarte(x, y) && carte[x][y] != VIDE;
    }

    public List<Position> lookAround(Position position){
        List<Position> positions = new ArrayList<>();
        for (Direction direction : Direction.values()) {
            Position posToCheck = Direction.changeDirection(position, direction);
            if(isElement(posToCheck))
                positions.add(posToCheck);
        }
        return positions;
    }

    public char[][] getCarte() {
        char[][] copy = new char[TAILLE][TAILLE];
        for (int i = 0; i < carte.length; i++) {
            for (int k = 0; k < carte[i].length; k++) {
                copy[i][k] = carte[i][k];
            }
        }
        return copy;
    }
}
