package models.perso;


import models.game.Butin;

public class Loup extends Monster implements DepecableInterface{


    public Loup(int endurance, int force, int x, int y) {
        super(endurance, force, Butin.generate(false, true), x, y);
    }

    @Override
    public String toString() {
        return "[LOUP]" + super.toString();
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
}
