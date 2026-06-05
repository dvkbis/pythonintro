package models.perso;

import models.game.Position;
import tools.Dice;

public abstract class Personnage {
    private int endurance;
    private int force;
    private int pv;
    private int currentLife;
    private int x;
    private int y;


    public Personnage(int endurance, int force) {
        this.endurance = endurance;
        this.force = force;
        this.pv = this.currentLife = calculerBonus(endurance) + endurance;
    }

    public Personnage(int endurance, int force, int x, int y) {
        this(endurance, force);
        this.x = x;
        this.y = y;
    }


    public int getEndurance() {
        return endurance;
    }


    public int getForce() {
        return force;
    }


    public int getPv() {
        return pv;
    }


    public int getCurrentLife() {
        return currentLife;
    }

    public void setCurrentLife(int currentLife) {
        this.currentLife = currentLife;
    }

    public boolean isAlive(){
        return currentLife > 0;
    }

    public void submitDamages(int damage){
        currentLife -= damage;
    }

    public int frappe(Personnage ennemie, Dice dice){
        int result = dice.roll();
        result += calculerBonus(getForce());

        ennemie.submitDamages(result);
        //currentLife -= result;

        return result;
    }

    public int getY() {
        return y;
    }

    public void setY(int y) {
        this.y = y;
    }

    public int getX() {
        return x;
    }

    public void setX(int x) {
        this.x = x;
    }

    public Position getPosition(){
        return new Position(x, y);
    }

    public void setPosition(Position position){
        x = position.x();
        y = position.y();
    }

    @Override
    public String toString() {
        return "Personnage{" +
                "endurance=" + endurance +
                ", force=" + force +
                ", pv=" + pv +
                '}';
    }


    private static  int calculerBonus(int value) {
        if(value < 5){
            return -1;
        }else if(value < 10){
            return  0;
        } else if(value < 15){
            return 1;
        }
        return 2;
    }

    public String getName() {
        return this.getClass().getSimpleName().toUpperCase();
    }
}
