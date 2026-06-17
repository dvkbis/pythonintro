from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.models.base import Base

class ProductType(Base):
    __tablename__ = "product_type"

    id = Column(Integer, primary_key = True)
    name = Column(String(50), nullable=False, unique=True)
    description = Column(String(255))

    products = relationship("Product", back_populates = "product_type")

    def __repr__(self):
        return f"<ProductType {self.name}>"