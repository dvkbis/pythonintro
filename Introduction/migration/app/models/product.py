from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.models.base import Base

class Product(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key = True)
    name = Column(String(100), nullable= False)
    description = Column(String(255))
    price = Column(Float, nullable= False)

    product_type_id = Column(Integer, ForeignKey("product_type.id"), nullable=False)
    
    created_at = Column(DateTime, default= datetime.now)
    product_type = relationship("ProductType", back_populates= "products")
    
    stock = relationship("Stock", back_populates="products", uselist= False)
    # orders = relationship("Order", back_populates="product")
    orders = relationship("Order", secondary="product_order", back_populates="products")
    
    def __repr__(self):
        return f"<Product {self.name}>"