package models.game;
public class ActionMove implements MakeAction{
    private Carte.Direction direction;

    public ActionMove(Carte.Direction direction) {
        this.direction = direction;
    }

    public Carte.Direction getDirection() {
        return direction;
    }
}
