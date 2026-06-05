package models.perso;

import models.game.Butin;
import tools.Dice;

public abstract class Hero extends Personnage{

    private int cuir;
    private int or;


    public Hero(int endurance, int force) {
        super(endurance, force);
        or = 0;
        cuir = 0;
    }

    public void regenerate(){
        setCurrentLife(getPv());
    }

    @Override
    public String toString() {
        return "Hero{" + super.toString() +
                ", cuir=" + cuir +
                ", or=" + or +
                '}';
    }

    @Override
    public int frappe(Personnage ennmie, Dice dice) {
        return super.frappe(ennmie, dice);
    }

    public int getCuir() {
        return cuir;
    }

    public int getOr() {
        return or;
    }

    protected void setCuir(int cuir) {
        this.cuir = cuir;
    }

    protected void setOr(int or) {
        this.or = or;
    }

    public void addButin(Butin butin) {
        cuir += butin.getCuir();
        or += butin.getOr();
    }


    public String getDescription() {
        return getClass().getSimpleName().toUpperCase() + " ( end=" + getEndurance() + ", for=" + getForce() + ", pv= " + getPv() + ")";
    }
}
