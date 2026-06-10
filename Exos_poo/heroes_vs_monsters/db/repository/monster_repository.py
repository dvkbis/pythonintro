from model.monster import Monster
from db.db_connect import DBConnect

class MonsterRepository:
    def __init__(self):
        self.db = DBConnect()

    def create_table(self):
        with self.db.conn.cursor() as cur:
            cur.execute("""CREATE TABLE IF NOT EXISTS monster(
                            endurance INT,
                            force INT,
                            pv INT,
                            current_life INT,
                            x INT,
                            y INT
                        );""")
    def find_all(self):
        with self.db.conn.cursor() as cur:
            cur.execute("SELECT * FROM monster")
            return cur.fetchall()       

    def insert(self, monster):
        if not isinstance(monster, Monster):
            raise ValueError("Bad instance")
        with self.db.conn.cursor() as cur:
            cur.execute("""INSERT INTO monster (endurance, force, pv, current_life, x, y) 
                        VALUES (%s, %s, %s, %s, %s, %s)
                        """,
                        (monster.endurance, monster.force, monster.pv, monster.current_life, monster.x, monster.y))
    def remove_all(self):
        with self.db.conn.cursor() as cur:
            cur.execute("DELETE FROM monster")