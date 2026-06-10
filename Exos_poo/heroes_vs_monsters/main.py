from model.human import Human
from model.wolf import Wolf
from model.dice import Dice
from model.combat import Combat
from model.hero import Hero
from model.monster import Monster
from db.db_connect import DBConnect
from db.repository.hero_repository import HeroRepository
from db.repository.monster_repository import MonsterRepository

human = Human(12,12,12,12,0,0)
wolf = Wolf(12,12,12,12,1,1)
combat = Combat(human, wolf)
# while(not combat.is_over()):
#    combat.next_combat()
#    input("Press Enter to continue...")

db_connect = DBConnect()
hero_repo = HeroRepository()
monster_repo = MonsterRepository()
# db_connect.create_hero_table()
# connect.create_monster_table()
# hero = Hero(10, 2, 10, 4,0,0)
# # connect.insert_hero(hero)
# print(connect.find_all_hero())
monster_repo.insert(Monster(9,12,9,9,2,2))
monster_repo.insert(Monster(4,2,4,2,1,2))
print(monster_repo.find_all())
monster_repo.remove_all()
print(monster_repo.find_all())

   # with self.db.conn.cursor() as cur:
