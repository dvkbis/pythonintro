from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.orm import relationship
from app.models.base import Base
from datetime import datetime

class Customer(Base):
    __tablename__ = "customer"

    id = Column(Integer, primary_key= True)
    first_name = Column(String(50), nullable= False)
    last_name = Column(String(50), nullable= False)
    email = Column(String(50), nullable= False)
    address = Column(String(255), nullable= False)
    phone = Column(String(15))

    created_at = Column(DateTime, default=datetime.now)

    def __repr__(self):
        return f"<Customer id = {self.id}, {self.first_name}, {self.last_name}>"