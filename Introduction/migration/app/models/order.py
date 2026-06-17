from sqlalchemy import Column, Integer, ForeignKey, DateTime, Enum
from sqlalchemy.orm import relationship
from app.models.base import Base
from datetime import datetime

class Order(Base):
    __tablename__ = "customer_order"

    id = Column(Integer, primary_key=True)
    quantity = Column(Integer, nullable= False, default= 1, server_default="1")
    state = Column(
        Enum("PENDING", "PAID", "SHIPPED", "CANCELLED", 
             name="order_state", 
             native_enum= False), nullable= False)
    # product_id = Column(Integer, ForeignKey("product.id"), nullable= False)

    created_at = Column(DateTime, default= datetime.now)
    updated_at = Column(DateTime, default = datetime.now, onupdate= datetime.now)

    #product = relationship("Product", back_populates="orders")
    products = relationship("Product", secondary="product_order", back_populates="orders")
    def __repr__(self):
        return f"<Order order_id = {self.id}, {self.quantity}, {self.state}>"