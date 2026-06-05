package models.perso;

import models.game.Butin;

public class Orque extends Monster{
    public static final int BONUS_FORCE = 1;


    public Orque(int endurance, int force, int x, int y) {
        super(endurance, force, Butin.generate(true, false), x, y);
    }

    @Override
    public int getForce() {
        return super.getForce() + BONUS_FORCE;
    }

    @Override
    public String toString() {
        return "[ORC]" + super.toString();
    }
}
