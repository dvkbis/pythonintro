from sqlalchemy.orm import Session
from app.models.product import Product

class ProductRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, product: Product) -> Product:
        self.db.add(product)
        self.db.commit()
        self.db.refresh(product)
        return product

    def read_by_id(self, id: int):
        return self.db.get(Product, id)
    
    def read_all(self):
        return self.db.query(Product).all()
    
    def update(self, id: int, product: Product) -> Product:
        existing = self.read_by_id(id)
        if existing:
            existing.name = product.name
            existing.description = product.description
            existing.price = product.price
            existing.product_type_id = product.product_type_id
            
            self.db.commit()
            self.db.refresh(existing)
        return existing
    
    def delete(self, id: int) -> Product:
        existing = self.read_by_id(id)
        if existing:
            self.db.delete(existing)
            self.db.commit()

            return existing
        return None


