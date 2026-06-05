package models.game;

import java.util.HashMap;

import static tools.Dice.DiceFour;
import static tools.Dice.DiceSix;

public class Butin {
    public int cuir;
    public int or;


    public Butin(int or, int cuir){
        this.or = or;
        this.cuir = cuir;
    }


    public static Butin generate(boolean haveOr, boolean haveCuir){
        int cuir = haveCuir ? DiceFour.roll() : 0;
        int or = haveOr ? DiceSix.roll() : 0;

        return new Butin(or, cuir);
    }

    public int getCuir() {
        return cuir;
    }

    public int getOr() {
        return or;
    }

    public void setCuir(int cuir) {
        this.cuir = cuir;
    }

    public void setOr(int or) {
        this.or = or;
    }

    @Override
    public String toString() {
        return "Butin{" +
                "cuir=" + cuir +
                ", or=" + or +
                '}';
    }
}
