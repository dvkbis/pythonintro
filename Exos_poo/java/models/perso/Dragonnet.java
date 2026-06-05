package models.perso;

import models.game.Butin;

public class Dragonnet extends Monster implements DepecableInterface{
    public static final int BONUS_ENDU = 1;



    public Dragonnet(int endurance, int force, int x, int y) {
        super(endurance, force, Butin.generate(true, true), x, y);
    }

    @Override
    public String toString() {
        return "[DRAGONNET]" + super.toString();
    }

    @Override
    public int depecer() {
        if(getCurrentLife() <= 0) {
            int cuir = getButin().getCuir();
            getButin().setCuir(0);
            return cuir;
        }
        return 0;
    }

    @Override
    public int getEndurance() {
        return super.getEndurance() + BONUS_ENDU;
    }
}
