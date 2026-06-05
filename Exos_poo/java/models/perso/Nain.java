package models.perso;

public class Nain extends Hero{

    public final int BONUS_ENDU = 2;

    public Nain(int endurance, int force) {
        super(endurance, force);
    }



    @Override
    public int getEndurance() {
        return super.getEndurance() + BONUS_ENDU;
    }



}
