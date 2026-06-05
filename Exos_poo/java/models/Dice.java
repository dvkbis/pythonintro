package tools;

import java.security.SecureRandom;
import java.util.ArrayList;
import java.util.List;


public enum Dice {
    DiceThree(3),
    DiceFour(4),
    DiceSix(6);

    private int maximum;
    private int minimum;
    private SecureRandom rand;

    Dice(int maximum){
        this.maximum = maximum;
        this.minimum = 1;
        this.rand = new SecureRandom();
    }


    public int roll(){
        return rand.nextInt(this.maximum) + this.minimum;
    }

    public List<Integer> roll(int nLancer, int best){
        ArrayList<Integer> list = new ArrayList<>();

        for (int i = 0; i < nLancer; i++) {
            list.add(roll());
        }
        list.sort(Integer::compareTo);

        return list.reversed().stream().limit(best).toList();

    }



}


