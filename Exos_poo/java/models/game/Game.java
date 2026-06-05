package models.game;

import models.perso.*;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

import static tools.Dice.DiceSix;
import static tools.Dice.DiceThree;

public class Game {
    private final static char HERO_PLAYER = 'H';
    private final static char MONSTER_LOUP = 'L';
    private final static char MONSTER_DRAGONNET = 'D';
    private final static char MONSTER_ORQUE = 'O';
    private final static int TAILLE_CARTE = 15;
    private final static int SPACE_BETWEEN_CHARACTER = 2;
    private final int nbMonstersMax;

    public enum MonsterType {ORQUE, LOUP, DRAGONNET}
    public enum HeroType {NAIN, HUMAIN}
    public enum Statut {MOUVEMENT, COMBAT}


    private final ArrayList<Combat> combats;
    private final Hero hero;

    public final Carte carte;
    public final HashMap<Position, Monster> monsterMap = new HashMap<>();

    private Statut currentStatut;
    private int nbFightWon;


    public Game(HeroType typeHero, int nbMonsters) {
        this.nbMonstersMax = nbMonsters;
        this.combats = new ArrayList<>();
        this.hero = createHero(typeHero);
        carte = new Carte(TAILLE_CARTE);
    }

    public int getNbFightWon() {
        return nbFightWon;
    }

    public Hero getHero() {
        return hero;
    }

    private static int rollCharacteristic(){
        return DiceSix.roll(6, 3).stream().reduce(Integer::sum).orElse(0);
    }
    public static Monster createMonster(MonsterType monster, Position pos) {
        int endurance = rollCharacteristic();
        int force = rollCharacteristic();

        int x = pos.x();
        int y = pos.y();
        return switch (monster){
            case ORQUE -> new Orque(endurance, force, x, y);
            case LOUP -> new Loup(endurance, force, x, y);
            case DRAGONNET -> new Dragonnet(endurance, force, x, y);

        };
    }

    public static Hero createHero(HeroType hero) {
        int endurance = rollCharacteristic();
        int force = rollCharacteristic();

        return switch (hero){
            case HUMAIN -> new Humain(endurance, force);
            case NAIN -> new Nain(endurance, force);
        };
    }

    public void startGame() throws ImpossiblePlacementException{
        currentStatut = Statut.MOUVEMENT;
        nbFightWon = 0;
        hero.setX(TAILLE_CARTE / 2);
        hero.setY(TAILLE_CARTE / 2);

        carte.createElement(hero.getPosition(), HERO_PLAYER);

        for(int i = 0; i < nbMonstersMax; i++){
            generateMonster();
        }
    }


    public void generateMonster() throws ImpossiblePlacementException {
       MonsterType monsterType = generateMonsterType(); // générer un type de monstre aléatoire

       Position position = carte.insertElementRandomly(getLetterFor(monsterType),SPACE_BETWEEN_CHARACTER, 1000 ); // place dans la carte
        if(position == null)
            throw  new ImpossiblePlacementException();

       monsterMap.put(position, createMonster(monsterType, position)); // insére dans les données
    }

    private char getLetterFor(MonsterType monsterType) {
        return switch (monsterType){
            case ORQUE -> MONSTER_ORQUE;
            case LOUP -> MONSTER_LOUP;
            case DRAGONNET -> MONSTER_DRAGONNET;
        };
    }

    private MonsterType generateMonsterType(){

        return switch (DiceThree.roll()){
            case 1 -> MonsterType.ORQUE;
            case 2 -> MonsterType.DRAGONNET;
            default -> MonsterType.LOUP;
        };
    }

    // EVENT
    // BOUGER {Deplacement}
    // COMBATTRE { STRIKE }
    // RAMASSER {

    public void makeAction(MakeAction makeAction) throws ImpossiblePlacementException {

//        if(makeAction instanceof ActionMove)
//            movePlayer(((ActionMove) makeAction).getDirection());
//        else if(makeAction instanceof  ActionFight)
//            getNextCombat();
    }
    public boolean movePlayer(Carte.Direction direction) throws ImpossiblePlacementException {
        if(currentStatut != Statut.MOUVEMENT)
            return false;

       boolean isHeroMoved = carte.move(hero.getPosition(), direction);

       if(!isHeroMoved) return false;

       hero.setPosition(Carte.Direction.changeDirection(hero.getPosition(), direction));
       List<Position> monstersAroundPositions = carte.lookAround(hero.getPosition());

        for (Position monsterPosition : monstersAroundPositions) {
            combats.add( new Combat(hero, monsterMap.get(monsterPosition)));
        }
        if(!combats.isEmpty())
            currentStatut = Statut.COMBAT;

        return true;
    }

    public Combat getNextCombat(){
        if(currentStatut == Statut.COMBAT){
            while(!combats.isEmpty() && combats.getFirst().isOver()){
                combats.removeFirst();
            }
            return !combats.isEmpty() ? combats.getFirst() : null;
        }
        return null;
    }


    public boolean hasNext() {
        if(!hero.isAlive()) return false;
        if(!combats.isEmpty() && combats.getFirst().isOver()){
            nbFightWon++;
            carte.removeElement(combats.getFirst().getMonster().getPosition());
            combats.removeFirst();
            currentStatut = Statut.MOUVEMENT;
            hero.regenerate();
        }
        return true;
    }


    public boolean hasEnnemy() {
        return !combats.isEmpty();
    }

    public void printCarte(){
        carte.afficherCarte();
    }

//    private void supprEnnemy(Personnage p){
//        carte.supprimerElement(p.getX(), p.getY());
//    }



}
