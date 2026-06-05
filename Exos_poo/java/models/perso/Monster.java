package models.perso;

import models.game.Butin;
import tools.Dice;

public abstract class Monster extends Personnage{

    private final Butin butin;

    public Monster(int endurance, int force, Butin butin, int x, int y) {
        super(endurance, force, x, y);
        this.butin = butin;
    }

    public Butin getButin() {
        return butin;
    }


    public int fouiller(){
        if(getCurrentLife() <= 0){
            int or = butin.getOr();
            butin.setOr(0);
            return or;
        }
        return 0;
    }

    @Override
    public int frappe(Personnage ennemie, Dice dice) {
        return super.frappe(ennemie, dice);
    }

    @Override
    public String toString() {
        return "Monster{" + super.toString() +
                ", butin=" + butin +
                '}';
    }
}
