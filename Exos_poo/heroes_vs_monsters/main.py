from model.human import Human
from model.wolf import Wolf
from model.dice import Dice
from model.combat import Combat

human = Human(12,12,12,12,0,0)
wolf = Wolf(12,12,12,12,1,1)
combat = Combat(human, wolf)
while(not combat.is_over()):
   combat.next_combat()
   input("Press Enter to continue...")
