from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.models.base import Base

class Stock(Base):
    __tablename__ = "stock"
    
    id = Column(Integer, primary_key= True)

    product_id = Column(Integer, ForeignKey("product.id"), nullable= False, unique= True)
    quantity = Column(Integer, nullable= False, default=0, server_default="0")
    last_update = Column(DateTime, default = datetime.now, onupdate= datetime.now)

    product = relationship("Product", back_populates="stock", uselist=False)

    def __repr__(self):
        return f"<Stock product_id = {self.product_id}, {self.quantity}>"