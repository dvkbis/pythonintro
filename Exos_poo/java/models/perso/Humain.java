package models.perso;

public class Humain extends Hero {

    public static final int BONUS_FORCE = 1;
    public static final int BONUS_ENDU = 1;

    public Humain(int endurance, int force) {
        super(endurance, force);
    }

    @Override
    public int getForce() {
        return super.getForce() + BONUS_FORCE;
    }

    @Override
    public int getEndurance() {
        return super.getEndurance() + BONUS_ENDU;
    }


}
