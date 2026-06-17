from sqlalchemy.orm import Session
from app.models.stock import Stock

class StockRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, stock: Stock) -> Stock:
        self.db.add(stock)
        self.db.commit()
        self.db.refresh(stock)
        return stock

    def read_by_id(self, id: int):
        return self.db.get(Stock, id)
    
    def read_all(self):
        return self.db.query(Stock).all()
    
    def update(self, id: int, stock: Stock) -> Stock:
        existing = self.read_by_id(id)
        if existing:
            existing.quantity = stock.quantity
            
            self.db.commit()
            self.db.refresh(existing)
        return existing
    
    def delete(self, id: int) -> Stock:
        existing = self.read_by_id(id)
        if existing:
            self.db.delete(existing)
            self.db.commit()

            return existing
        return None


