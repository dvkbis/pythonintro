from db.db_connect import DBConnect
from model.hero import Hero

class HeroRepository:

    def __init__(self):
        self.db = DBConnect()

    def create_table(self):
        with self.db.conn.cursor() as cur:
            cur.execute("""CREATE TABLE IF NOT EXISTS hero(
                            endurance INT,
                            force INT,
                            pv INT,
                            current_life INT,
                            x INT,
                            y INT
                        );""")   
    def find_all(self):
        with self.db.conn.cursor() as cur:
            cur.execute("SELECT * FROM hero")
            return cur.fetchall()       

    def insert(self, hero):
        if not isinstance(hero, Hero):
            raise ValueError("Bad instance")
        with self.db.conn.cursor() as cur:
            cur.execute("""INSERT INTO hero (endurance, force, pv, current_life, x, y) 
                        VALUES (%s, %s, %s, %s, %s, %s)
                        """,
                        (hero.endurance, hero.force, hero.pv, hero.current_life, hero.x, hero.y))
    def remove_all(self):
        with self.db.conn.cursor() as cur:
            cur.execute("DELETE FROM hero")
