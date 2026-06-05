package models.game;

import models.perso.DepecableInterface;
import models.perso.Hero;
import models.perso.Monster;
import models.perso.Personnage;
import tools.Dice;

import java.util.ArrayList;

import static tools.Dice.DiceFour;

public class Combat {
    public static class CombatInfo{
        String opponent;
        String defender;
        int damage;
        int lifeDefender;
        int lifeOpponent;
        int diceValue;

        public CombatInfo(String opponent, String defender, int damage, int lifeDefender, int lifeOpponent, int diceValue) {
            this.opponent = opponent;
            this.defender = defender;
            this.damage = damage;
            this.lifeDefender = lifeDefender;
            this.lifeOpponent = lifeOpponent;
            this.diceValue = diceValue;
        }

        public String getDescription(){
            return opponent.toUpperCase() + " frappe " + defender.toUpperCase()  +
                    " pour " + damage + " dégat(s). [Restant : " + lifeDefender + "]";
        }

    }

    private final Hero hero;
    private final Monster monster;
    private int tour;
    private ArrayList<CombatInfo> combatInfos;


    public Combat(Hero hero, Monster monster) {
        this.hero = hero;
        this.monster = monster;
        this.tour = 0;
        combatInfos = new ArrayList<>();
    }

    public Hero getHero() {
        return hero;
    }

    public Monster getMonster() {
        return monster;
    }

    public boolean isOver(){
        return !hero.isAlive() || !monster.isAlive();
    }

    public CombatInfo next(){
        CombatInfo combatInfo = null;
        if(!isOver()){
            tour ++;
            if(tour % 2 == 1) {
                int dmg = hero.frappe(monster, DiceFour);
                combatInfo = new CombatInfo(hero.getName(), monster.getName(), dmg, hero.getCurrentLife(), monster.getCurrentLife(), 0);

            }else {
                int dmg = monster.frappe(hero, DiceFour);
                combatInfo = new CombatInfo(monster.getName(), hero.getName(), dmg, monster.getCurrentLife(), hero.getCurrentLife(), 0);
            }
        }
        return combatInfo;
    }


    public Personnage getWinner(){
        if(!isOver()) return null;

        return hero.isAlive() ? hero : monster;
    }

    public String getRecompense(){
        if(!isOver()) return null;

        if(getWinner() == hero){
            int or = monster.fouiller();
            int cuir = 0;
            if(monster instanceof DepecableInterface depecableInterface){
                cuir = depecableInterface.depecer();
            }

            hero.addButin(new Butin(or, cuir));
            return " >> BUTIN : " + or + " or , " + cuir + " cuir(s).";
        }
        return "";
    }

    @Override
    public String toString() {
        return "Combat{" +
                "hero=" + hero +
                ", monster=" + monster +
                ", tour=" + tour +
                ", combatInfos=" + combatInfos +
                '}';
    }
}
