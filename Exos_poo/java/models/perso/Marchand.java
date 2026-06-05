package models.perso;

import java.util.HashMap;
import java.util.Map;

public class Marchand {

    Map<ItemCost, Integer> items = new HashMap<>();

    public Marchand(){

    }

    public boolean removeItem(String name, int n){
//        if(items.containsKey(name) && items.get(name) <= n){
//            items.replace(name, items.get(name) - n);
//            return true;
//        }

        return false;
    }

    public record ItemCost(
        String name,
        int cost,
        String money
    ){
        // Protection, 10 cuirs
        // Potion de soins, 10 ors
    }

}
